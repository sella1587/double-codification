import pandas as pd
from .models import ObjectsFromCao, ConsolidationRule

def consolidate_data():
    # Charger les objets actifs (non archivés)
    objects = ObjectsFromCao.objects.filter(archived_date__isnull=True)
    data = pd.DataFrame.from_records(objects.values())
    print(data)

    # Charger les règles de consolidation
    rules = ConsolidationRule.objects.all()
    config = [
        {
            "property": rule.property_name,
            "sourcespriorites": rule.sources_priorities,
            "DisplayMode": rule.display_mode,
        }
        for rule in rules
    ]

    # Initialiser le DataFrame consolidé
    consolidated_rows = []

    # Regrouper les données par 'name'
    for name, group in data.groupby("name"):
        consolidated_row = {"name": name}

        for rule in config:
            property_name = rule["property"]
            sources_priorities = rule.get("sourcespriorites")
            display_mode = rule.get("DisplayMode", "All")

            if property_name not in group.columns:
                consolidated_row[property_name] = None
                continue

            # Si SourcesPriorites est défini, filtrer les sources par priorité
            if sources_priorities:
                sources_priorities = sources_priorities.split(";")
                valid_sources = [s for s in sources_priorities if s in group["source"].values]
            else:
                valid_sources = group["source"].unique()

            # Si aucune source valide n'est trouvée, prendre les valeurs restantes
            if not valid_sources:
                group_sorted = group
            else:
                group_sorted = group.sort_values(
                    by="source", key=lambda x: x.map({s: i for i, s in enumerate(valid_sources)}).fillna(len(valid_sources))
                )

            if display_mode == "First":
                consolidated_row[property_name] = group_sorted.iloc[0][property_name]
            elif display_mode == "All":
                consolidated_row[property_name] = "; ".join(group_sorted[property_name].astype(str).unique())

        consolidated_rows.append(consolidated_row)
    return pd.DataFrame(data)
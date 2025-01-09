from django.db import models

class Object(models.Model):
    uid = models.CharField(max_length=255, unique=True)
    source = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    component_type = models.CharField(max_length=255, null=True, blank=True)
    facteur = models.FloatField(null=True, blank=True)
    archived_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.uid} - {self.name} - {self.source}"


class ConsolidationRule(models.Model):
    property_name = models.CharField(max_length=255)
    sources_priorities = models.TextField(null=True, blank=True)  # Ex: "PID;SPEL;SM3D;USER"
    display_mode = models.CharField(max_length=50, choices=[("First", "First"), ("All", "All")])

    def __str__(self):
        return self.property_name


import pandas as pd
from .models import Object, ConsolidationRule

def consolidate_data():
    # Charger les objets actifs (non archivés)
    objects = Object.objects.filter(archived_date__isnull=True)
    data = pd.DataFrame.from_records(objects.values())

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

    # Retourner un DataFrame consolidé
    return pd.DataFrame(consolidated_rows)


from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import consolidate_data

class ConsolidatedDataView(APIView):
    def get(self, request, *args, **kwargs):
        consolidated_df = consolidate_data()
        consolidated_data = consolidated_df.to_dict(orient="records")
        return Response(consolidated_data)


from django.urls import path
from .views import ConsolidatedDataView

urlpatterns = [
    path('api/consolidated-data/', ConsolidatedDataView.as_view(), name='consolidated-data'),
]



import pandas as pd

# Exemple de données brutes
data = pd.DataFrame([
    {"uid": 1, "name": "A", "source": "UNKNOWN", "component_type": "Valve", "facteur": 0.8, "archived_date": None},
    {"uid": 2, "name": "A", "source": "SPEL", "component_type": "Pump", "facteur": 0.9, "archived_date": None},
    {"uid": 3, "name": "B", "source": "SM3D", "component_type": "Pipe", "facteur": 1.2, "archived_date": None},
    {"uid": 4, "name": "B", "source": "USER", "component_type": "Pipe", "facteur": 1.1, "archived_date": None},
    {"uid": 5, "name": "C", "source": "PID", "component_type": "Tank", "facteur": 0.7, "archived_date": "2024-01-01"},
    {"uid": 6, "name": "C", "source": "SPEL", "component_type": "Tank", "facteur": 0.6, "archived_date": None},
])

# Configuration des règles
config = [
    {
        "property": "component_type",
        "sourcespriorites": "5;5;3;3",
        "DisplayMode": "First",  # Options possibles : "First", "All"
    },
    {
        "property": "facteur",
        "sourcespriorites": "PID;SPEL;SM3D;USER",
        "DisplayMode": "All",
    },
]

# Filtrer les données actives (archived_date = None)
filtered_data = data[data["archived_date"].isnull()]

# Initialiser le DataFrame consolidé
consolidated_rows = []

# Regrouper les données par 'name' pour effectuer la consolidation
for name, group in filtered_data.groupby("name"):
    consolidated_row = {"name": name}

    for rule in config:
        property_name = rule["property"]
        sources_priorities = rule.get("sourcespriorites")
        display_mode = rule.get("DisplayMode", "All")

        if property_name not in group.columns:
            consolidated_row[property_name] = None  # Valeur par défaut si la colonne n'existe pas
            continue

        # Si SourcesPriorites est défini, filtrer les sources par priorité
        if sources_priorities:
            sources_priorities = sources_priorities.split(";")
            valid_sources = [s for s in sources_priorities if s in group["source"].values]
        else:
            valid_sources = group["source"].unique()  # Inclure toutes les sources

        # Si aucune source valide n'est trouvée, prendre les valeurs restantes
        if not valid_sources:
            group_sorted = group
        else:
            # Trier les données du groupe selon les priorités valides
            group_sorted = group.sort_values(
                by="source", key=lambda x: x.map({s: i for i, s in enumerate(valid_sources)}).fillna(len(valid_sources))
            )

        if display_mode == "First":
            # Prendre la première valeur selon la priorité ou l'ordre existant
            consolidated_row[property_name] = group_sorted.iloc[0][property_name]
        elif display_mode == "All":
            # Prendre toutes les valeurs selon la priorité ou l'ordre existant
            consolidated_row[property_name] = "; ".join(group_sorted[property_name].astype(str).unique())

    consolidated_rows.append(consolidated_row)

# Créer un DataFrame consolidé
consolidated_data = pd.DataFrame(consolidated_rows)

# Afficher les données consolidées
print(consolidated_data)

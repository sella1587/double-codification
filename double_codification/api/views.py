from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import consolidate_data

class ConsolidatedDataView(APIView):
    """
    GetConsolidateDatat:
        cette api retourn les données consolidé base sur un fichier de parametre specifique
    """
    def get(self, request, *args, **kwargs):
        consolidated_df = consolidate_data()
        consolidated_data = consolidated_df.to_dict(orient="records")
        return Response(consolidated_data)
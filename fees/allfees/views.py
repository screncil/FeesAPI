from rest_framework.response import Response
from rest_framework.views import APIView
from scraper import FeesScraper

class AllFeesView(APIView):
    
    def get(self, request):
        fees = FeesScraper()
        return Response(fees.getAll())
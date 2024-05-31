from rest_framework.response import Response
from rest_framework.views import APIView
from scraper import FeesScraper

class AllFeesView(APIView):
    
    def get(self, request):
        fees = FeesScraper()
        return Response(fees.getAll())
    

class TransportFeesView(APIView):
    
    def get(self, request):
        fees = FeesScraper()
        return Response(fees.type("Транспорт"))
    

class EquipmentFeesView(APIView):

    def get(self, request):
        fees = FeesScraper()
        return Response(fees.type("Обладнання"))
    

class DronesFeesView(APIView):

    def get(self, request):
        fees = FeesScraper()
        return Response(fees.type("Дрони"))
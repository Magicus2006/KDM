from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
#import requests
#from datetime import date
#from requests.structures import CaseInsensitiveDict
#import xml.etree.ElementTree as ET


# Create your views here.
class AventosTypeView(APIView):
    '''
    def get(self, request):
        width = request.data.get('width')
        height = request.data.get('height')
        print(width, height, request.data)
        return Response({"width": width, "height": height})
    '''

    def post(self, request):
        pass

"""class CurrencyAPI(APIView):
    def get(self, request):
        url = "https://cbr.ru/scripts/XML_daily.asp?date-req=05/03/2022"
        result = requests.get(url=url)

        date_req = self.request.query_params.get('date-req')
        if date_req == None:
            t = date.today()
            date_now = t.strftime("%d/%m/%Y")
        else:
            date_now = date_req

        print(result.content)
        json_respon = {}

        try:
            root = ET.fromstring(result.content)
            print(root.tag, root.attrib)

            for childs in root:
                t = {}
                for child in childs:
                    t.update({child.tag: child.text})
                json_respon.update({childs.attrib["ID"]: t})

            print(json_respon)
        except ET.ParseError as e:
            print(e)
            return Response(f'Error: {e}, {e.code} {e.position}')

        return Response(json_respon)"""
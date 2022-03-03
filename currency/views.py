from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from requests.structures import CaseInsensitiveDict
import xml.etree.ElementTree as ET


# Create your views here.


class CurrencyAPI(APIView):
    def get(self, request):
        url = "https://cbr.ru/scripts/XML_daily.asp?date-req=04/03/2022"
        result = requests.get(url=url)

        #print(result.content)
        root = ET.fromstring(result.content)
        print(root.tag, root.attrib)
        json_respon = {}
        for childs in root:
            t = {}
            for child in childs:
                t.update({child.tag: child.text})
            json_respon.update({childs.attrib["ID"]: t})

        print(json_respon)
        return Response(json_respon)
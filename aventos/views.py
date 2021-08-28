from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

class AventosTypeView(APIView):
    '''
    def get(self, request):
        width = request.data.get('width')
        height = request.data.get('height')
        print(width, height, request.data)
        return Response({"width": width, "height": height})
    '''

    def post(self, request):
        width = request.data.get('width')
        height = request.data.get('height')
        thickness = request.data.get('thickness') # Толщина
        handleWeight = request.data.get('handleWeight') # Вес ручки
        density = request.data.get('density') # Плотность

        weightFacade = (width/1000) * (height/1000) * (thickness/1000) * (density*1000)
        weightFacade += handleWeight
        weightFacade = round(weightFacade,2)
        km = round(weightFacade * height,0)

        listAventos = {}
        aventosCalculate = AventosCalculate()
        listAventosHS = aventosCalculate.HS(weightFacade, height)
        listAventosHL = aventosCalculate.HL(weightFacade, height)
        if listAventosHS != None:
            listAventos.update({"HS": listAventosHS})
        if listAventosHL != None:
            listAventos.update({"HL": listAventosHL})
        print(listAventos)
        return Response(listAventos)

class AventosCalculate():
    def HS(self, weightFacade, height):
        listAventos = []
        if height >= 350 and height <= 400:
            if weightFacade >= 2 and weightFacade <= 5:
                listAventos.append("HS1")
            if weightFacade >= 4.25 and weightFacade <= 9.50:
                listAventos.append("HS2")
            if weightFacade >= 8.75 and weightFacade <= 12:
                listAventos.append("HS3")
        elif height >= 401 and height <= 450:
            if weightFacade >= 2 and weightFacade <= 4.75:
                listAventos.append("HS1")
            if weightFacade >= 4 and weightFacade <= 9:
                listAventos.append("HS2")
            if weightFacade >= 8.25 and weightFacade <= 13.50:
                listAventos.append("HS3")
        elif height >= 451 and height <= 500:
            if weightFacade >= 2.50 and weightFacade <= 4.25:
                listAventos.append("HS1")
            if weightFacade >= 3.50 and weightFacade <= 8.50:
                listAventos.append("HS2")
            if weightFacade >= 7.50 and weightFacade <= 14.75:
                listAventos.append("HS3")
        elif height >= 501 and height <= 525:
            if weightFacade >= 2.50 and weightFacade <= 4.25:
                listAventos.append("HS1")
            if weightFacade >= 3.25 and weightFacade <= 7.75:
                listAventos.append("HS2")
            if weightFacade >= 7.25 and weightFacade <= 15.0:
                listAventos.append("HS3")

        elif height >= 526 and height <= 550:
            if weightFacade >= 3 and weightFacade <= 6.75:
                listAventos.append("HS4")
            if weightFacade >= 6 and weightFacade <= 13:
                listAventos.append("HS5")
            if weightFacade >= 11.50 and weightFacade <= 17.25:
                listAventos.append("HS5")
        elif height >= 551 and height <= 600:
            if weightFacade >= 3 and weightFacade <= 6.5:
                listAventos.append("HS4")
            if weightFacade >= 5.5 and weightFacade <= 12.5:
                listAventos.append("HS5")
            if weightFacade >= 10.5 and weightFacade <= 18.5:
                listAventos.append("HS5")
        elif height >= 601 and height <= 650:
            if weightFacade >= 3 and weightFacade <= 6:
                listAventos.append("HS4")
            if weightFacade >= 5.25 and weightFacade <= 11.75:
                listAventos.append("HS5")
            if weightFacade >= 10 and weightFacade <= 19:
                listAventos.append("HS5")
        elif height >= 651 and height <= 675:
            if weightFacade >= 3 and weightFacade <= 5.5:
                listAventos.append("HS4")
            if weightFacade >= 5 and weightFacade <= 11.25:
                listAventos.append("HS5")
            if weightFacade >= 9.75 and weightFacade <= 19:
                listAventos.append("HS5")

        elif height >= 676 and height <= 700:
            if weightFacade >= 3.50 and weightFacade <= 8:
                listAventos.append("HS7")
            if weightFacade >= 6.75 and weightFacade <= 13.50:
                listAventos.append("HS8")
            if weightFacade >= 12.50 and weightFacade <= 21.50:
                listAventos.append("HS9")
        elif height >= 701 and height <= 750:
            if weightFacade >= 3.50 and weightFacade <= 7.75:
                listAventos.append("HS7")
            if weightFacade >= 6.5 and weightFacade <= 13.25:
                listAventos.append("HS8")
            if weightFacade >= 11.5 and weightFacade <= 21.50:
                listAventos.append("HS9")
        elif height >= 750 and height <= 800:
            if weightFacade >= 3.50 and weightFacade <= 7.25:
                listAventos.append("HS7")
            if weightFacade >= 6 and weightFacade <= 12.75:
                listAventos.append("HS8")
            if weightFacade >= 10.50 and weightFacade <= 20.50:
                listAventos.append("HS9")
        else:
            listAventos = None

        return listAventos

    def HL(self, weightFacade, height):
        listAventos = []
        if height >= 300 and height <= 350:
            if weightFacade >= 1.25 and weightFacade <= 4.25:
                listAventos.append("HL01")
            if weightFacade >= 3.5 and weightFacade <= 7.25:
                listAventos.append("HL02")
            if weightFacade >= 6.50 and weightFacade <= 12:
                listAventos.append("HL03")
            if weightFacade >= 11 and weightFacade <= 20:
                listAventos.append("HL04")
        elif height >= 351 and height <= 400:
            if weightFacade >= 1.25 and weightFacade <= 2.5:
                listAventos.append("HL05")
            if weightFacade >= 1.75 and weightFacade <= 5:
                listAventos.append("HL06")
            if weightFacade >= 4.25 and weightFacade <= 9:
                listAventos.append("HL07")
            if weightFacade >= 8 and weightFacade <= 14.75:
                listAventos.append("HL08")
            if weightFacade >= 13.50 and weightFacade <= 20:
                listAventos.append("HL09")
        elif height >= 401 and height <= 550:
            if weightFacade >= 1.75 and weightFacade <= 3.50:
                listAventos.append("HL10")
            if weightFacade >= 2.75 and weightFacade <= 6.75:
                listAventos.append("HL11")
            if weightFacade >= 5.75 and weightFacade <= 11.75:
                listAventos.append("HL12")
            if weightFacade >= 10.5 and weightFacade <= 20:
                listAventos.append("HL13")
        elif height >= 450 and height <= 580:
            if weightFacade >= 2 and weightFacade <= 5.25:
                listAventos.append("HS1")
            if weightFacade >= 4.25 and weightFacade <= 9.25:
                listAventos.append("HS2")
            if weightFacade >= 8.25 and weightFacade <= 16.50:
                listAventos.append("HS3")
        else:
            listAventos = None
        return listAventos
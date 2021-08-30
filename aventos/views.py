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
        weightFacade2 = weightFacade + handleWeight
        weightFacade = round(weightFacade,2)
        km = int(round(weightFacade * height,0))
        km2 = int(round(weightFacade2 * height, 0))

        listAventos = {}
        aventosCalculate = AventosCalculate()
        listAventosHS = aventosCalculate.HS(weightFacade, width, height)
        listAventosHL = aventosCalculate.HL(weightFacade, width, height)
        listAventosHF = aventosCalculate.HF(km, weightFacade, width, height)
        listAventosHK_top = aventosCalculate.HK_top(km2, weightFacade2, width, height)
        listAventosHK_top_TIPON = aventosCalculate.HK_top_TIPON(km2, weightFacade2, width, height)
        listAventosHK = aventosCalculate.HK(km2, weightFacade2, width, height)
        listAventosHK_TIPON = aventosCalculate.HK_TIPON(km2, weightFacade2, width, height)
        listAventosHK_S = aventosCalculate.HK_S(km2, weightFacade2, width, height)
        listAventosHK_S_TIPON = aventosCalculate.HK_S_TIPON(km2, weightFacade2, width, height)
        listAventosHK_XS = aventosCalculate.HK_XS(km2, weightFacade2, width, height)
        listAventosHK_XS_TIPON = aventosCalculate.HK_XS_TIPON(km2, weightFacade2, width, height)
        if listAventosHF != [] and listAventosHF != None:
            listAventos.update({"HF": listAventosHF})
        if listAventosHS != [] and listAventosHS != None:
            listAventos.update({"HS": listAventosHS})
        if listAventosHL != [] and listAventosHL != None:
            listAventos.update({"HL": listAventosHL})
        if listAventosHK_top != [] and listAventosHK_top != None:
            listAventos.update({"HK Top": listAventosHK_top})
        if listAventosHK_top_TIPON != [] and listAventosHK_top_TIPON != None:
            listAventos.update({"HK Top TIP-ON": listAventosHK_top_TIPON})
        if listAventosHK != [] and listAventosHK != None:
            listAventos.update({"HK": listAventosHK})
        if listAventosHK_TIPON != [] and listAventosHK_TIPON != None:
            listAventos.update({"HK TIP-ON": listAventosHK_TIPON})
        if listAventosHK_S != [] and listAventosHK_S != None:
            listAventos.update({"HK-S": listAventosHK_S})
        if listAventosHK_S_TIPON != [] and listAventosHK_S_TIPON != None:
            listAventos.update({"HK-S TIP-ON": listAventosHK_S_TIPON})
        if listAventosHK_XS != [] and listAventosHK_XS != None:
            listAventos.update({"HK-XS": listAventosHK_XS})
        if listAventosHK_XS_TIPON != [] and listAventosHK_XS_TIPON != None:
            listAventos.update({"HK-XS TIP-ON": listAventosHK_XS_TIPON})
        print(listAventos)
        return Response(listAventos)

class AventosCalculate():
    """Класс расчета и выбора комплекта для подъемников Aventos"""

    def HS(self, weightFacade, width, height):
        """
        Фукция возращает комплект подъемника Aventos HS
            weightFacade - Вес фасада
            height - Высота фасада
        """
        if height < 350 or height > 800 or width > 1800:
            return []
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

    def HL(self, weightFacade, width, height):
        """
        Фукция возращает комплект подъемника Aventos HL
            weightFacade - Вес фасада
            height - Высота фасада
        """
        if height < 300 or height > 580 or width > 1800:
            return []
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
    def HF(self, km, weightFacade, width, height):
        """
            Фукция возращает комплект подъемника Aventos HF
                km - Коэффициент мощности
                weightFacade - Вес фасада
                weight - ширина фасада
                height - Высота фасада
        """
        if height < 480 or height > 1040 or width > 1800:
            return []
        listAventos = []
        hinge = 2
        if width >= 1200 and width < 1800:
            hinge = 3
        if weightFacade >= 12 and weightFacade < 20:
            hinge = 3
        if width >= 1800:
            hinge = 4
        if weightFacade >= 20:
            hinge = 4

        if km >= 2600 and km <= 5500:
            if height >= 480 and height <= 570:
                listAventos.append("HF01-"+str(hinge))
            if height >= 560 and height <= 710:
                listAventos.append("HF04-"+str(hinge))
            if height >= 700 and height <= 900:
                listAventos.append("HF07-"+str(hinge))
            if height >= 760 and height <= 1040:
                listAventos.append("HF10-"+str(hinge))
        if km >= 5350 and km <= 10150:
            if height >= 480 and height <= 570:
                listAventos.append("HF02-"+str(hinge))
            if height >= 560 and height <= 710:
                listAventos.append("HF05-"+str(hinge))
            if height >= 700 and height <= 900:
                listAventos.append("HF08-"+str(hinge))
            if height >= 760 and height <= 1040:
                listAventos.append("HF11-"+str(hinge))
        if km >= 9000 and km <= 17250:
            if height >= 480 and height <= 570:
                listAventos.append("HF03-"+str(hinge))
            if height >= 560 and height <= 710:
                listAventos.append("HF06-"+str(hinge))
            if height >= 700 and height <= 900:
                listAventos.append("HF09-"+str(hinge))
            if height >= 760 and height <= 1040:
                listAventos.append("HF12-"+str(hinge))

        return listAventos

    def HK_top(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 420 and km <= 1610:
            listAventos.append("HTS1")
        if km >= 930 and km <= 2800:
            listAventos.append("HTS2")
        if km >= 1730 and km <= 5200:
            listAventos.append("HTS3")
        if km >= 3200 and km <= 9000:
            listAventos.append("HTS4")

        return listAventos

    def HK_top_TIPON(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 420 and km <= 1610:
            listAventos.append("HTTS1")
        if km >= 930 and km <= 2800:
            listAventos.append("HTTS2")
        if km >= 1730 and km <= 5200:
            listAventos.append("HTTS3")
        if km >= 3200 and km <= 9000:
            listAventos.append("HTTS4")

        return listAventos

    def HK(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 480 and km <= 1500:
            listAventos.append("HK1")
        if km >= 750 and km <= 2500:
            listAventos.append("HK2")
        if km >= 1500 and km <= 4900:
            listAventos.append("HK3")
        if km >= 3200 and km <= 9000:
            listAventos.append("HK4")
        return listAventos

    def HK_TIPON(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 480 and km <= 1500:
            listAventos.append("HKT1")
        if km >= 750 and km <= 2500:
            listAventos.append("HKT2")
        if km >= 1500 and km <= 4900:
            listAventos.append("HKT3")
        if km >= 3200 and km <= 9000:
            listAventos.append("HKT4")
        return listAventos

    def HK_S(self, km, weightFacade, width, height):
        if height < 180 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 220 and km <= 500:
            listAventos.append("HKS1")
        if km >= 400 and km <= 1000:
            listAventos.append("HKS2")
        if km >= 680 and km <= 1520:
            listAventos.append("HKS3")
        if km >= 960 and km <= 2215:
            listAventos.append("HKS4")
        return listAventos

    def HK_S_TIPON(self, km, weightFacade, width, height):
        if height < 180 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 220 and km <= 500:
            listAventos.append("HKST1")
        if km >= 400 and km <= 1000:
            listAventos.append("HKST2")
        if km >= 680 and km <= 1520:
            listAventos.append("HKST3")
        if km >= 960 and km <= 2215:
            listAventos.append("HKST4")
        return listAventos

    def HK_XS(self, km, weightFacade, width, height):
        if height < 240 or height > 600 or width > 1800:
            return []
        hinge = 2
        if width >= 900 and width < 1200:
            hinge = 3
        if km >= 1800 and km < 2700:
            hinge = 3
        if width >= 1200:
            hinge = 4
        if km >= 2700:
            hinge = 4
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 200 and km <= 1000:
            listAventos.append("HXS1-"+str(hinge))
        if km >= 500 and km <= 1500:
            listAventos.append("HXS2-"+str(hinge))
        if km >= 800 and km <= 1800:
            listAventos.append("HXS3-"+str(hinge))
        if km >= 400 and km <= 2000:
            listAventos.append("HXS4-"+str(hinge))
        if km >= 1000 and km <= 3000:
            listAventos.append("HXS5-"+str(hinge))
        if km >= 1600 and km <= 3600:
            listAventos.append("HXS6-"+str(hinge))

        return listAventos

    def HK_XS_TIPON(self, km, weightFacade, width, height):
        if height < 240 or height > 600 or width > 1800:
            return []
        hinge = 2
        if width >= 900 and width < 1200:
            hinge = 3
        if km >= 1800 and km < 2700:
            hinge = 3
        if width >= 1200:
            hinge = 4
        if km >= 2700:
            hinge = 4
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 200 and km <= 1000:
            listAventos.append("HXST1-" + str(hinge))
        if km >= 500 and km <= 1500:
            listAventos.append("HXST2-" + str(hinge))
        if km >= 800 and km <= 1800:
            listAventos.append("HXST3-" + str(hinge))
        if km >= 400 and km <= 2000:
            listAventos.append("HXST4-" + str(hinge))
        if km >= 1000 and km <= 3000:
            listAventos.append("HXST5-" + str(hinge))
        if km >= 1600 and km <= 3600:
            listAventos.append("HXST6-" + str(hinge))

        return listAventos
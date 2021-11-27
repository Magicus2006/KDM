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

        weightFacade = (width/1000) * (height/1000) * (thickness/1000) * density
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
        print("AventosHF:", listAventosHF)
        listAventosHK_top = aventosCalculate.HK_top(km2, weightFacade2, width, height)
        listAventosHK_top_TIPON = aventosCalculate.HK_top_TIPON(km2, weightFacade2, width, height)
        listAventosHK = aventosCalculate.HK(km2, weightFacade2, width, height)
        listAventosHK_TIPON = aventosCalculate.HK_TIPON(km2, weightFacade2, width, height)
        listAventosHK_S = aventosCalculate.HK_S(km2, weightFacade2, width, height)
        listAventosHK_S_TIPON = aventosCalculate.HK_S_TIPON(km2, weightFacade2, width, height)
        listAventosHK_XS = aventosCalculate.HK_XS(km2, weightFacade2, width, height)
        listAventosHK_XS_TIPON = aventosCalculate.HK_XS_TIPON(km2, weightFacade2, width, height)
        if listAventosHF != [] and listAventosHF != None:
            listAventos.update({"HF": {"set": listAventosHF, "tipon": False}})

        if listAventosHS != [] and listAventosHS != None:
            listAventos.update({"HS": {"set": listAventosHS, "tipon": False}})

        if listAventosHL != [] and listAventosHL != None:
            listAventos.update({"HL": {"set": listAventosHL, "tipon": False}})

        if listAventosHK_top != [] and listAventosHK_top != None:
            listAventos.update({"HK Top": {"set": listAventosHK_top, "tipon": False}})

        if listAventosHK_top_TIPON != [] and listAventosHK_top_TIPON != None:
            listAventos.update({"HK Top TIP-ON": {"set": listAventosHK_top_TIPON, "tipon": True}})

        if listAventosHK != [] and listAventosHK != None:
            listAventos.update({"HK": {"set": listAventosHK, "tipon": False}})

        if listAventosHK_TIPON != [] and listAventosHK_TIPON != None:
            listAventos.update({"HK TIP-ON": {"set": listAventosHK_TIPON, "tipon": True}})

        if listAventosHK_S != [] and listAventosHK_S != None:
            listAventos.update({"HK-S": {"set": listAventosHK_S, "tipon": False}})

        if listAventosHK_S_TIPON != [] and listAventosHK_S_TIPON != None:
            listAventos.update({"HK-S TIP-ON": {"set": listAventosHK_S_TIPON, "tipon": True}})

        if listAventosHK_XS != [] and listAventosHK_XS != None:
            listAventos.update({"HK-XS": {"set": listAventosHK_XS, "tipon": False}})

        if listAventosHK_XS_TIPON != [] and listAventosHK_XS_TIPON != None:
            listAventos.update({"HK-XS TIP-ON": {"set": listAventosHK_XS_TIPON, "tipon": True}})

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
                listAventos.append({"name": "HS1", "cost": 131.36})  # HS1
            if weightFacade >= 4.25 and weightFacade <= 9.50:
                listAventos.append({"name": "HS2", "cost": 131.36})
            if weightFacade >= 8.75 and weightFacade <= 12:
                listAventos.append({"name": "HS3", "cost": 138.34})
        elif height >= 401 and height <= 450:
            if weightFacade >= 2 and weightFacade <= 4.75:
                listAventos.append({"name": "HS1", "cost": 131.36})
            if weightFacade >= 4 and weightFacade <= 9:
                listAventos.append({"name": "HS2", "cost": 131.36})
            if weightFacade >= 8.25 and weightFacade <= 13.50:
                listAventos.append({"name": "HS3", "cost": 131.36})
        elif height >= 451 and height <= 500:
            if weightFacade >= 2.50 and weightFacade <= 4.25:
                listAventos.append({"name": "HS1", "cost": 131.36})
            if weightFacade >= 3.50 and weightFacade <= 8.50:
                listAventos.append({"name": "HS2", "cost": 131.36})
            if weightFacade >= 7.50 and weightFacade <= 14.75:
                listAventos.append({"name": "HS3", "cost": 131.36})
        elif height >= 501 and height <= 525:
            if weightFacade >= 2.50 and weightFacade <= 4.25:
                listAventos.append({"name": "HS1", "cost": 131.36})
            if weightFacade >= 3.25 and weightFacade <= 7.75:
                listAventos.append({"name": "HS2", "cost": 131.36})
            if weightFacade >= 7.25 and weightFacade <= 15.0:
                listAventos.append({"name": "HS3", "cost": 131.36})

        elif height >= 526 and height <= 550:
            if weightFacade >= 3 and weightFacade <= 6.75:
                listAventos.append({"name": "HS4", "cost": 131.36})
            if weightFacade >= 6 and weightFacade <= 13:
                listAventos.append({"name": "HS5", "cost": 131.36})
            if weightFacade >= 11.50 and weightFacade <= 17.25:
                listAventos.append({"name": "HS5", "cost": 131.36})
        elif height >= 551 and height <= 600:
            if weightFacade >= 3 and weightFacade <= 6.5:
                listAventos.append({"name": "HS4", "cost": 131.36})
            if weightFacade >= 5.5 and weightFacade <= 12.5:
                listAventos.append({"name": "HS5", "cost": 131.36})
            if weightFacade >= 10.5 and weightFacade <= 18.5:
                listAventos.append({"name": "HS5", "cost": 131.36})
        elif height >= 601 and height <= 650:
            if weightFacade >= 3 and weightFacade <= 6:
                listAventos.append({"name": "HS4", "cost": 131.36})
            if weightFacade >= 5.25 and weightFacade <= 11.75:
                listAventos.append({"name": "HS5", "cost": 131.36})
            if weightFacade >= 10 and weightFacade <= 19:
                listAventos.append({"name": "HS5", "cost": 131.36})
        elif height >= 651 and height <= 675:
            if weightFacade >= 3 and weightFacade <= 5.5:
                listAventos.append({"name": "HS4", "cost": 131.36})
            if weightFacade >= 5 and weightFacade <= 11.25:
                listAventos.append({"name": "HS5", "cost": 131.36})
            if weightFacade >= 9.75 and weightFacade <= 19:
                listAventos.append({"name": "HS5", "cost": 131.36})

        elif height >= 676 and height <= 700:
            if weightFacade >= 3.50 and weightFacade <= 8:
                listAventos.append({"name": "HS7", "cost": 131.36})
            if weightFacade >= 6.75 and weightFacade <= 13.50:
                listAventos.append({"name": "HS8", "cost": 131.36})
            if weightFacade >= 12.50 and weightFacade <= 21.50:
                listAventos.append({"name": "HS9", "cost": 131.36})
        elif height >= 701 and height <= 750:
            if weightFacade >= 3.50 and weightFacade <= 7.75:
                listAventos.append({"name": "HS7", "cost": 131.36})
            if weightFacade >= 6.5 and weightFacade <= 13.25:
                listAventos.append({"name": "HS8", "cost": 131.36})
            if weightFacade >= 11.5 and weightFacade <= 21.50:
                listAventos.append({"name": "HS9", "cost": 131.36})
        elif height >= 750 and height <= 800:
            if weightFacade >= 3.50 and weightFacade <= 7.25:
                listAventos.append({"name": "HS7", "cost": 131.36})
            if weightFacade >= 6 and weightFacade <= 12.75:
                listAventos.append({"name": "HS8", "cost": 131.36})
            if weightFacade >= 10.50 and weightFacade <= 20.50:
                listAventos.append({"name": "HS9", "cost": 131.36})
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
                listAventos.append({"name": "HL01", "cost": 131.36})
            if weightFacade >= 3.5 and weightFacade <= 7.25:
                listAventos.append({"name": "HL02", "cost": 131.36})
            if weightFacade >= 6.50 and weightFacade <= 12:
                listAventos.append({"name": "HL03", "cost": 131.36})
            if weightFacade >= 11 and weightFacade <= 20:
                listAventos.append({"name": "HL04", "cost": 131.36})
        elif height >= 351 and height <= 400:
            if weightFacade >= 1.25 and weightFacade <= 2.5:
                listAventos.append({"name": "HL05", "cost": 131.36})
            if weightFacade >= 1.75 and weightFacade <= 5:
                listAventos.append({"name": "HL06", "cost": 131.36})
            if weightFacade >= 4.25 and weightFacade <= 9:
                listAventos.append({"name": "HL07", "cost": 131.36})
            if weightFacade >= 8 and weightFacade <= 14.75:
                listAventos.append({"name": "HL08", "cost": 131.36})
            if weightFacade >= 13.50 and weightFacade <= 20:
                listAventos.append({"name": "HL09", "cost": 131.36})
        elif height >= 401 and height <= 550:
            if weightFacade >= 1.75 and weightFacade <= 3.50:
                listAventos.append({"name": "HL10", "cost": 131.36})
            if weightFacade >= 2.75 and weightFacade <= 6.75:
                listAventos.append({"name": "HL11", "cost": 131.36})
            if weightFacade >= 5.75 and weightFacade <= 11.75:
                listAventos.append({"name": "HL12", "cost": 131.36})
            if weightFacade >= 10.5 and weightFacade <= 20:
                listAventos.append({"name": "HL13", "cost": 131.36})
        elif height >= 450 and height <= 580:
            if weightFacade >= 2 and weightFacade <= 5.25:
                listAventos.append({"name": "HL14", "cost": 131.36})
            if weightFacade >= 4.25 and weightFacade <= 9.25:
                listAventos.append({"name": "HL15", "cost": 131.36})
            if weightFacade >= 8.25 and weightFacade <= 16.50:
                listAventos.append({"name": "HL16", "cost": 131.36})
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
                listAventos.append({"name": "HF01-"+str(hinge), "cost": 131.36})
            if height >= 560 and height <= 710:
                listAventos.append({"name": "HF04-"+str(hinge), "cost": 131.36})
            if height >= 700 and height <= 900:
                listAventos.append({"name": "HF07-"+str(hinge), "cost": 131.36})
            if height >= 760 and height <= 1040:
                listAventos.append({"name": "HF10-"+str(hinge), "cost": 131.36})
        if km >= 5350 and km <= 10150:
            if height >= 480 and height <= 570:
                listAventos.append({"name": "HF02-"+str(hinge), "cost": 131.36})
            if height >= 560 and height <= 710:
                listAventos.append({"name": "HF05-"+str(hinge), "cost": 131.36})
            if height >= 700 and height <= 900:
                listAventos.append({"name": "HF08-"+str(hinge), "cost": 131.36})
            if height >= 760 and height <= 1040:
                listAventos.append({"name": "HF11-"+str(hinge), "cost": 131.36})
        if km >= 9000 and km <= 17250:
            if height >= 480 and height <= 570:
                listAventos.append({"name": "HF03-"+str(hinge), "cost": 131.36})
            if height >= 560 and height <= 710:
                listAventos.append({"name": "HF06-"+str(hinge), "cost": 131.36})
            if height >= 700 and height <= 900:
                listAventos.append({"name": "HF09-"+str(hinge), "cost": 131.36})
            if height >= 760 and height <= 1040:
                listAventos.append({"name": "HF12-"+str(hinge), "cost": 131.36})

        return listAventos

    def HK_top(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 420 and km <= 1610:
            listAventos.append({"name": "HTS1", "cost": 131.36})
        if km >= 930 and km <= 2800:
            listAventos.append({"name": "HTS2", "cost": 131.36})
        if km >= 1730 and km <= 5200:
            listAventos.append({"name": "HTS3", "cost": 131.36})
        if km >= 3200 and km <= 9000:
            listAventos.append({"name": "HTS4", "cost": 131.36})

        return listAventos

    def HK_top_TIPON(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 420 and km <= 1610:
            listAventos.append({"name": "HTTS1", "cost": 131.36})
        if km >= 930 and km <= 2800:
            listAventos.append({"name": "HTTS2", "cost": 131.36})
        if km >= 1730 and km <= 5200:
            listAventos.append({"name": "HTTS3", "cost": 131.36})
        if km >= 3200 and km <= 9000:
            listAventos.append({"name": "HTTS4", "cost": 131.36})

        return listAventos

    def HK(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 480 and km <= 1500:
            listAventos.append({"name": "HK1", "cost": 131.36})
        if km >= 750 and km <= 2500:
            listAventos.append({"name": "HK2", "cost": 131.36})
        if km >= 1500 and km <= 4900:
            listAventos.append({"name": "HK3", "cost": 131.36})
        if km >= 3200 and km <= 9000:
            listAventos.append({"name": "HK4", "cost": 131.36})
        return listAventos

    def HK_TIPON(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 480 and km <= 1500:
            listAventos.append({"name": "HKT1", "cost": 131.36})
        if km >= 750 and km <= 2500:
            listAventos.append({"name": "HKT2", "cost": 131.36})
        if km >= 1500 and km <= 4900:
            listAventos.append({"name": "HKT3", "cost": 131.36})
        if km >= 3200 and km <= 9000:
            listAventos.append({"name": "HKT4", "cost": 131.36})
        return listAventos

    def HK_S(self, km, weightFacade, width, height):
        if height < 180 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 220 and km <= 500:
            listAventos.append({"name": "HKS1", "cost": 131.36})
        if km >= 400 and km <= 1000:
            listAventos.append({"name": "HKS2", "cost": 131.36})
        if km >= 680 and km <= 1520:
            listAventos.append({"name": "HKS3", "cost": 131.36})
        if km >= 960 and km <= 2215:
            listAventos.append({"name": "HKS4", "cost": 131.36})
        return listAventos

    def HK_S_TIPON(self, km, weightFacade, width, height):
        if height < 180 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 220 and km <= 500:
            listAventos.append({"name": "HKST1", "cost": 131.36})
        if km >= 400 and km <= 1000:
            listAventos.append({"name": "HKST2", "cost": 131.36})
        if km >= 680 and km <= 1520:
            listAventos.append({"name": "HKST3", "cost": 131.36})
        if km >= 960 and km <= 2215:
            listAventos.append({"name": "HKST4", "cost": 131.36})
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
            listAventos.append({"name": "HXS1-"+str(hinge), "cost": 131.36})
        if km >= 500 and km <= 1500:
            listAventos.append({"name": "HXS2-"+str(hinge), "cost": 131.36})
        if km >= 800 and km <= 1800:
            listAventos.append({"name": "HXS3-"+str(hinge), "cost": 131.36})
        if km >= 400 and km <= 2000:
            listAventos.append({"name": "HXS4-"+str(hinge), "cost": 131.36})
        if km >= 1000 and km <= 3000:
            listAventos.append({"name": "HXS5-"+str(hinge), "cost": 131.36})
        if km >= 1600 and km <= 3600:
            listAventos.append({"name": "HXS6-"+str(hinge), "cost": 131.36})

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
            listAventos.append({"name":"HXST1-" + str(hinge), "cost": 131.36})
        if km >= 500 and km <= 1500:
            listAventos.append({"name":"HXST2-" + str(hinge), "cost": 131.36})
        if km >= 800 and km <= 1800:
            listAventos.append({"name":"HXST3-" + str(hinge), "cost": 131.36})
        if km >= 400 and km <= 2000:
            listAventos.append({"name":"HXST4-" + str(hinge), "cost": 131.36})
        if km >= 1000 and km <= 3000:
            listAventos.append({"name":"HXST5-" + str(hinge), "cost": 131.36})
        if km >= 1600 and km <= 3600:
            listAventos.append({"name":"HXST6-" + str(hinge), "cost": 131.36})

        return listAventos
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return render(request, 'index.html')

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

        print(km, weightFacade, width, height)

        listAventos = {}
        aventosCalculate = AventosCalculate()
        listAventosHS = aventosCalculate.HS(weightFacade, width, height)
        listAventosHL = aventosCalculate.HL(weightFacade, width, height)
        listAventosHF = aventosCalculate.HF(km, weightFacade, width, height)
        listAventosHK_top = aventosCalculate.HK_top(km2, weightFacade2, width, height)
        listAventosHK_top_TIPON = aventosCalculate.HK_top_TIPON(km2, weightFacade2, width, height)
        '''
        Снято с производства
        listAventosHK = aventosCalculate.HK(km2, weightFacade2, width, height)
        listAventosHK_TIPON = aventosCalculate.HK_TIPON(km2, weightFacade2, width, height)
        '''
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
        '''
        if listAventosHK != [] and listAventosHK != None:
            listAventos.update({"HK": {"set": listAventosHK, "tipon": False}})

        if listAventosHK_TIPON != [] and listAventosHK_TIPON != None:
            listAventos.update({"HK TIP-ON": {"set": listAventosHK_TIPON, "tipon": True}})
        '''
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
                name="HS1"
                print(name, self.costAventosSet(name))
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})  # HS1
            if weightFacade >= 4.25 and weightFacade <= 9.50:
                name="HS2"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 8.75 and weightFacade <= 12:
                listAventos.append({"name": "HS3", "cost": 138.34})
        elif height >= 401 and height <= 450:
            if weightFacade >= 2 and weightFacade <= 4.75:
                name="HS1"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 4 and weightFacade <= 9:
                name="HS2"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 8.25 and weightFacade <= 13.50:
                name="HS3"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 451 and height <= 500:
            if weightFacade >= 2.50 and weightFacade <= 4.25:
                name="HS1"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 3.50 and weightFacade <= 8.50:
                name="HS2"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 7.50 and weightFacade <= 14.75:
                name="HS3"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 501 and height <= 525:
            if weightFacade >= 2.50 and weightFacade <= 4.25:
                name="HS1"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 3.25 and weightFacade <= 7.75:
                name="HS2"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 7.25 and weightFacade <= 15.0:
                name="HS3"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})

        elif height >= 526 and height <= 550:
            if weightFacade >= 3 and weightFacade <= 6.75:
                name="HS4"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 6 and weightFacade <= 13:
                name="HS5"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 11.50 and weightFacade <= 17.25:
                name="HS5"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 551 and height <= 600:
            if weightFacade >= 3 and weightFacade <= 6.5:
                name="HS4"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 5.5 and weightFacade <= 12.5:
                name="HS5"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 10.5 and weightFacade <= 18.5:
                name="HS5"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 601 and height <= 650:
            if weightFacade >= 3 and weightFacade <= 6:
                name="HS4"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 5.25 and weightFacade <= 11.75:
                name="HS5"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 10 and weightFacade <= 19:
                name="HS5"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 651 and height <= 675:
            if weightFacade >= 3 and weightFacade <= 5.5:
                name="HS4"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 5 and weightFacade <= 11.25:
                name="HS5"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 9.75 and weightFacade <= 19:
                name="HS5"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})

        elif height >= 676 and height <= 700:
            if weightFacade >= 3.50 and weightFacade <= 8:
                name="HS7"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 6.75 and weightFacade <= 13.50:
                name="HS8"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 12.50 and weightFacade <= 21.50:
                name="HS9"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 701 and height <= 750:
            if weightFacade >= 3.50 and weightFacade <= 7.75:
                name="HS7"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 6.5 and weightFacade <= 13.25:
                name="HS8"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 11.5 and weightFacade <= 21.50:
                name="HS9"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 750 and height <= 800:
            if weightFacade >= 3.50 and weightFacade <= 7.25:
                name="HS7"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 6 and weightFacade <= 12.75:
                name="HS8"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 10.50 and weightFacade <= 20.50:
                name="HS9"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
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
                name="HL01"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 3.5 and weightFacade <= 7.25:
                name="HL02"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 6.50 and weightFacade <= 12:
                name="HL03"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 11 and weightFacade <= 20:
                name="HL04"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 351 and height <= 400:
            if weightFacade >= 1.25 and weightFacade <= 2.5:
                name="HL05"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 1.75 and weightFacade <= 5:
                name="HL06"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 4.25 and weightFacade <= 9:
                name="HL07"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 8 and weightFacade <= 14.75:
                name="HL08"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 13.50 and weightFacade <= 20:
                name="HL09"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 401 and height <= 550:
            if weightFacade >= 1.75 and weightFacade <= 3.50:
                name="HL10"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 2.75 and weightFacade <= 6.75:
                name="HL11"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 5.75 and weightFacade <= 11.75:
                name="HL12"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 10.5 and weightFacade <= 20:
                name="HL13"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        elif height >= 450 and height <= 580:
            if weightFacade >= 2 and weightFacade <= 5.25:
                name="HL14"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 4.25 and weightFacade <= 9.25:
                name="HL15"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if weightFacade >= 8.25 and weightFacade <= 16.50:
                name="HL16"
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
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
                name = "HF01-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if height >= 560 and height <= 710:
                name = "HF04-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if height >= 700 and height <= 900:
                name = "HF07-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if height >= 760 and height <= 1040:
                name = "HF10-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 5350 and km <= 10150:
            if height >= 480 and height <= 570:
                name = "HF02-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if height >= 560 and height <= 710:
                name = "HF05-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if height >= 700 and height <= 900:
                name = "HF08-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if height >= 760 and height <= 1040:
                name = "HF11-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 9000 and km <= 17250:
            if height >= 480 and height <= 570:
                name = "HF03-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if height >= 560 and height <= 710:
                name = "HF06-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if height >= 700 and height <= 900:
                name = "HF09-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})
            if height >= 760 and height <= 1040:
                name = "HF12-"+str(hinge)
                listAventos.append({"name": name, "cost": self.costAventosSet(name)})

        return listAventos

    def HK_top(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 420 and km <= 1610:
            name="HTS1"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 930 and km <= 2800:
            name="HTS2"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 1730 and km <= 5200:
            name="HTS3"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 3200 and km <= 9000:
            name="HTS4"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})

        return listAventos

    def HK_top_TIPON(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 420 and km <= 1610:
            name="HTTS1"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 930 and km <= 2800:
            name="HTTS2"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 1730 and km <= 5200:
            name="HTTS3"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 3200 and km <= 9000:
            name="HTTS4"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})

        return listAventos

    def HK(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 480 and km <= 1500:
            name="HK1"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 750 and km <= 2500:
            name="HK2"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 1500 and km <= 4900:
            name="HK3"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 3200 and km <= 9000:
            name="HK4"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        return listAventos

    def HK_TIPON(self, km, weightFacade, width, height):
        if height < 205 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 480 and km <= 1500:
            name="HKT1"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 750 and km <= 2500:
            name="HKT2"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 1500 and km <= 4900:
            name="HKT3"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 3200 and km <= 9000:
            name="HKT4"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        return listAventos

    def HK_S(self, km, weightFacade, width, height):
        if height < 180 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 220 and km <= 500:
            name="HKS1"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 400 and km <= 1000:
            name="HKS2"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 680 and km <= 1520:
            name="HKS3"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 960 and km <= 2215:
            name="HKS4"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        return listAventos

    def HK_S_TIPON(self, km, weightFacade, width, height):
        if height < 180 or height > 600 or width > 1800:
            return []
        listAventos = []
        if weightFacade > 18:
            return []
        if km >= 220 and km <= 500:
            name="HKST1"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 400 and km <= 1000:
            name="HKST2"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 680 and km <= 1520:
            name="HKST3"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 960 and km <= 2215:
            name="HKST4"
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
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
            name = "HXS1-"+str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 500 and km <= 1500:
            name = "HXS2-"+str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 800 and km <= 1800:
            name = "HXS3-"+str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 400 and km <= 2000:
            name = "HXS4-"+str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 1000 and km <= 3000:
            name = "HXS5-"+str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 1600 and km <= 3600:
            name = "HXS6-"+str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})

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
            name = "HXST1-" + str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 500 and km <= 1500:
            name = "HXST2-" + str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 800 and km <= 1800:
            name = "HXST3-" + str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 400 and km <= 2000:
            name = "HXST4-" + str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 1000 and km <= 3000:
            name = "HXST5-" + str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})
        if km >= 1600 and km <= 3600:
            name = "HXST6-" + str(hinge)
            listAventos.append({"name": name, "cost": self.costAventosSet(name)})

        return listAventos

    def costAventosSet(self, name):
        price = {
            "HF01-2": 122.62,
            "HF02-2": 128.00,
            "HF02-3": 136.38,
            "HF03-3": 144.07,
            "HF03-4": 152.45,
            "HF04-2": 126.46,
            "HF05-2": 131.84,
            "HF05-3": 140.23,
            "HF06-3": 147.91,
            "HF06-4": 156.29,
            "HF07-2": 134.15,
            "HF08-2": 139.52,
            "HF08-3": 147.91,
            "HF09-2": 147.20,
            "HF09-3": 155.59,
            "HF09-4": 163.97,
            "HF10-2": 139.91,
            "HF11-2": 145.28,
            "HF11-3": 153.67,
            "HF12-2": 152.97,
            "HF12-3": 161.35,
            "HF12-4": 169.73,
            "HS1": 144.68,
            "HS2": 144.68,
            "HS3": 152.36,
            "HS4": 144.68,
            "HS5": 152.36,
            "HS6": 207.43,
            "HS7": 152.36,
            "HS8": 152.36,
            "HS9": 207.43,
            "HL01": 145.18,
            "HL02": 145.18,
            "HL03": 152.86,
            "HL04": 152.86,
            "HL05": 147.49,
            "HL06": 147.49,
            "HL07": 155.17,
            "HL08": 155.17,
            "HL09": 210.24,
            "HL05": 149.79,
            "HL06": 157.74,
            "HL07": 157.47,
            "HL08": 212.55,
            "HL05": 163.62,
            "HL06": 163.62,
            "HL07": 218.69,
            "HTS1": 80.39,
            "HTS2": 80.39,
            "HTS3": 80.74,
            "HTS4": 93.33,
            "HTTS1": 90.36,
            "HTTS2": 90.36,
            "HTTS3": 95.39,
            "HTTS4": 107.98,
            "HKS1": 35.13,
            "HKS2": 38.97,
            "HKS3": 38.97,
            "HKS4": 38.97,
            "HKST1": 40.48,
            "HKST2": 44.65,
            "HKST3": 44.65,
            "HKST4": 44.65,
            "HXS1-2": 25.04,
            "HXS2-2": 25.04,
            "HXS3-2": 25.04,
            "HXS4-2": 40.15,
            "HXS5-2": 40.15,
            "HXS6-2": 40.15,
            "HXS4-3": 45.12,
            "HXS5-3": 45.12,
            "HXS6-3": 45.12,
            "HXS5-4": 50.08,
            "HXS6-4": 50.08,
            "HXST1-2": 27.11,
            "HXST2-2": 27.11,
            "HXST3-2": 27.11,
            "HXST4-2": 43.26,
            "HXST5-2": 43.26,
            "HXST6-2": 43.26,
            "HXST5-3": 46.22,
            "HXST6-3": 46.22,
            "HXST6-4": 49.19,
        }

        if name in price:
            return price[name]
        else:
            return 0.00
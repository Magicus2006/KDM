#import re
from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CalculationTable, CalculationTableWeightFacade, VendorCode
#from django.core import serializers

# EQ("="), GTE(">="), GT(">"), LT("<"), LTE("<=");

class Lifts(APIView):
    #{"handleWeight":0.1,"height":375,"thickness":16,"width":800,"density":760}
    def post(self, request):
        width = request.data.get('width') # Шыринв
        height = request.data.get('height') # Высота
        thickness = request.data.get('thickness')  # Толщина
        handleWeight = request.data.get('handleWeight')  # Вес ручки
        density = request.data.get('density')  # Плотность
        #nameBrand = request.data.get('nameBrand') # Brand

        #  {"handleWeight":0,"height":370,"thickness":16,"width":800,"density":760}
        # Проверяем передали ли параметр nameBrand если нет то ставим по умолчанию DTC
        if(nameBrand := request.data.get('nameBrand')) is None:
            nameBrand = "DTC"

        # Считаем вес фасада
        weightFacade = (width / 1000) * (height / 1000) * (thickness / 1000) * density
        # Вес фасада + двойной вес ручки
        weightFacadeHandle = weightFacade + (handleWeight*2)
        # Считаем индекс нагрузки
        index = height * weightFacadeHandle

        #print(f'{width}х{height}-{thickness} Ручка {handleWeight} Плотность {density} = {index} Вес {weightFacade} Вес с ручкой {weightFacadeHandle}')

        lifts = {}

        # Формируем запрос на подемников считающихся по индексу
        queryset = CalculationTable.objects \
            .select_related('vendorCode') \
            .filter(nameBrand__name=nameBrand)\
            .filter(heightFacadeFrom__lte=height)\
            .filter(heightFacadeTo__gte=height)\
            .filter(indexFrom__lte=index)\
            .filter(indexTo__gte=index)\
            .filter(display=True)

        # Формируем ответ из подемников считающихся по индексу
        for lift in queryset:
            if lift.liftType.name in lifts:
                lifts[lift.liftType.name]["set"].append({"name": lift.vendorCode.vendorCode, "cost": lift.vendorCode.cost/100})
            else:
                lifts.update({lift.liftType.name: {"set": [{"name": lift.vendorCode.vendorCode, "cost": lift.vendorCode.cost/100}], "tipon": lift.liftType.tipon}})

        # Формируем запрос на подемников считающихся по весу
        queryset = CalculationTableWeightFacade.objects\
            .select_related('vendorCode')\
            .filter(nameBrand__name=nameBrand)\
            .filter(weightFacadeFrom__lte=weightFacadeHandle)\
            .filter(weightFacadeTo__gte=weightFacadeHandle)\
            .filter(heightFacadeFrom__lte=height)\
            .filter(heightFacadeTo__gte=height)\
            .filter(display=True)

        # Формируем ответ из подемников считающихся по весу
        for lift in queryset:
            if lift.liftType.name in lifts:
                lifts[lift.liftType.name]["set"].append(
                    {"name": lift.vendorCode.vendorCode, "cost": lift.vendorCode.cost/100})
            else:
                lifts.update({lift.liftType.name: {
                    "set": [{"name": lift.vendorCode.vendorCode, "cost": lift.vendorCode.cost/100}],
                    "tipon": lift.liftType.tipon}})

        #print(queryset)
        return Response(lifts)

def detail(request):
    #print(re.sub(r'(\w{2}\d{2}\w{2})(\d{2}\w{1})', r'\1', 'ST01AL02A'))
    #queryset = CalculationTableWeightFacade.objects \
    #    .select_related('vendorCode') \
    #    .filter(nameBrand__name="DTC") \
    #    .filter(vendorCode__vendorCode__regex='^(\w{6})$').update(display=True)

    """queryset = CalculationTable.objects.select_related('vendorCode')\
        .filter(nameBrand__name="DTC")\
        #.filter(vendorCode__vendorCode__regex='^(\w{6})$').update(display=True)

    for x in queryset:
        lenVendorCode = len(x.vendorCode.vendorCode)
        print(lenVendorCode)
        if lenVendorCode == 9:
            newVendorCode = re.sub(r'(\w{2}\w{2}\w{2})(\d{2}\w{1})', r'\1', x.vendorCode.vendorCode)
            print(newVendorCode)
        elif lenVendorCode == 8:
            newVendorCode = re.sub(r'(\w{2}\w{2}\w{2})(\d{2})', r'\1', x.vendorCode.vendorCode)
            print(newVendorCode)


        #print(x.vendorCode,
        #      x.weightFacadeFrom,
        #      x.weightFacadeTo,
        #      x.heightFacadeFrom,
        #      x.heightFacadeTo,
        #      x.nameBrand,
        #      x.liftType,
        #      x.display)



        #print(newVendorCode)
        try:
            vc = VendorCode(vendorCode=newVendorCode, name=x.vendorCode.name, cost=x.vendorCode.cost, currency=x.vendorCode.currency)
            vc.save()
            q = CalculationTable(vendorCode=vc,
                  indexFrom=x.indexFrom,
                  indexTo=x.indexTo,
                  heightFacadeFrom=x.heightFacadeFrom,
                  heightFacadeTo=x.heightFacadeTo,
                  nameBrand=x.nameBrand,
                  liftType=x.liftType,
                  display=True)

            q.save()
            print(q)
        except:
            print("Fail")
            pass
    """


    return HttpResponse("You're looking at question.") # %d" % queryset.count())
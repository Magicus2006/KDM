from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CalculationTable, CalculationTableWeightFacade
from django.core import serializers

# EQ("="), GTE(">="), GT(">"), LT("<"), LTE("<=");

class Lifts(APIView):
    #{"handleWeight":0.1,"height":375,"thickness":16,"width":800,"density":760}
    def post(self, request):
        width = request.data.get('width')
        height = request.data.get('height')
        thickness = request.data.get('thickness')  # Толщина
        handleWeight = request.data.get('handleWeight')  # Вес ручки
        density = request.data.get('density')  # Плотность

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
            .filter(nameBrand__name="DTC")\
            .filter(heightFacadeFrom__lte=height)\
            .filter(heightFacadeTo__gte=height)\
            .filter(indexFrom__lte=index)\
            .filter(indexTo__gte=index)

        # Формируем ответ из подемников считающихся по индексу
        for lift in queryset:
            if lift.liftType.name in lifts:
                lifts[lift.liftType.name]["set"].append({"name": lift.vendorCode.vendorCode, "cost": lift.vendorCode.cost/100})
            else:
                lifts.update({lift.liftType.name: {"set": [{"name": lift.vendorCode.vendorCode, "cost": lift.vendorCode.cost/100}], "tipon": lift.liftType.tipon}})

        # Формируем запрос на подемников считающихся по весу
        queryset = CalculationTableWeightFacade.objects\
            .select_related('vendorCode')\
            .filter(nameBrand__name="DTC")\
            .filter(weightFacadeFrom__lte=weightFacadeHandle)\
            .filter(weightFacadeTo__gte=weightFacadeHandle)\
            .filter(heightFacadeFrom__lte=height)\
            .filter(heightFacadeTo__gte=height)

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

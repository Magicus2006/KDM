from rest_framework.response import Response
from rest_framework.views import APIView
from lifts.models import CalculationTable, CalculationTableWeightFacade, VendorCode

class ListLifts(APIView):
    def get(self, request):
        nameBrand = "DTC"
        count = 0
        queryset = VendorCode.objects.all()
        lifts = []
        for lift in queryset:
            if lift.cost > 0 and len(lift.vendorCode) == 6:
                count += 1
                #print(count, lift.vendorCode, lift.cost)
                lifts.append({lift.vendorCode: lift.cost})

        print(lifts)
        """queryset = CalculationTable.objects \
            .select_related('vendorCode') \
            .filter(nameBrand__name=nameBrand) \
            .filter(display=True)

        for lift in queryset:
            if lift.vendorCode.cost > 0:
                count += 1
                print(count ,lift.vendorCode.vendorCode, lift.vendorCode.cost, lift.display)


        queryset = CalculationTableWeightFacade.objects \
            .select_related('vendorCode') \
            .filter(nameBrand__name=nameBrand) \
            .filter(display=True)

        for lift in queryset:
            if lift.vendorCode.cost > 0:
                count += 1
                print(count, lift.vendorCode.vendorCode, lift.vendorCode.cost, lift.display)
        """



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


        return Response({"Message": "Hello World!"})

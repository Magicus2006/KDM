from django.contrib import admin
from .models import NameBrend, LiftType, Currency, VendorCode, CalculationTable, CalculationTableWeightFacade

# Register your models here.

admin.site.register(NameBrend)
admin.site.register(LiftType)
admin.site.register(Currency)
@admin.register(VendorCode)
class VendorCodeAdmin(admin.ModelAdmin):
    search_fields = ("vendorCode__startswith", )

@admin.register(CalculationTableWeightFacade)
class CalculationTableWeightFacadeAdmin(admin.ModelAdmin):
    list_display = ("weightFacadeFrom",
                    "weightFacadeTo",
                    "heightFacadeFrom",
                    "heightFacadeTo",
                    "vendorCode",
                    "liftType")

@admin.register(CalculationTable)
class CalculationTableAdmin(admin.ModelAdmin):
    list_display = ("indexFrom",
                    "indexTo",
                    "heightFacadeFrom",
                    "heightFacadeTo",
                    "vendorCode",
                    "liftType")
    list_filter = ("liftType",)

#admin.site.register(CalculationTableWeightFacade)
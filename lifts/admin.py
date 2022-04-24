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
    list_display = ("vendorCode",
                    "weightFacadeFrom",
                    "weightFacadeTo",
                    "heightFacadeFrom",
                    "heightFacadeTo",
                    "liftType",
                    "nameBrand",
                    "display")

@admin.register(CalculationTable)
class CalculationTableAdmin(admin.ModelAdmin):
    list_display = ("vendorCode",
                    "indexFrom",
                    "indexTo",
                    "heightFacadeFrom",
                    "heightFacadeTo",
                    "liftType",
                    "nameBrand",
                    "display")
    list_filter = ("liftType",)

#admin.site.register(CalculationTableWeightFacade)
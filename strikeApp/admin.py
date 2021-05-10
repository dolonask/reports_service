from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Card)
admin.site.register(Source)
admin.site.register(Countries)
admin.site.register(Regions)
admin.site.register(DemandCategories)
admin.site.register(DemandTypes)
admin.site.register(NumberChoices)
admin.site.register(OwnerShipTypes)
admin.site.register(Documents)
from django.contrib import admin
from .models import Gases
# Register your models here.

# admin.site.register(Gases)
# admin.site.unregister(Gases)
@admin.register(Gases)
class GasesAdmin(admin.ModelAdmin):
    # list_display=['id','methane', 'carbondioxide','ammonia',"float_level"]
    list_display=['id','hydrogensulfide',"float_level"]
    model = Gases



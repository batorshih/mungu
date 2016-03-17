from django.contrib import admin
from main.models import Tamgas,Nershil
from main.models import aimag_city,soum_district,bag_khoroo
# Register your models here.


class TamgaAdmin(admin.ModelAdmin):
    list_display = ['name' , 'nershiluud','getimage']
    filter_horizontal = [ 'nershil',]
    search_fields  = [ 'nershil', 'name',]
    

admin.site.register(Tamgas,TamgaAdmin)
admin.site.register(Nershil)
class SoumAdmin(admin.ModelAdmin):
    list_display = ['name','aim','pk']
    list_filter = ('aim',)
    
class BagAdmin(admin.ModelAdmin):
    list_display = ['name','soum','getaim','pk']
    list_filter = ('soum',  )
    def getaim(self, obj):
        return '%s'%(obj.soum.aim)
    getaim.short_description = 'aimag'
    
admin.site.register(aimag_city)
admin.site.register(soum_district,SoumAdmin)
admin.site.register(bag_khoroo,BagAdmin)

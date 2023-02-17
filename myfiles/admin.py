from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','nomi','company_name','date','url','malumot','rasm1']

admin.site.register(Portfolio,AdminPortfolio)

class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi',]

admin.site.register(Type,AdminType)

class AdminServise(admin.ModelAdmin):
    list_display = ['nomi','malumot','rasm']

admin.site.register(Services,AdminServise)

class AdminTeam(admin.ModelAdmin):
    list_display = ['rasm','ismi','lavozimi','malumot','link1','link2','link3','link4']

admin.site.register(Team,AdminTeam)

class AdminMurojaat(admin.ModelAdmin):
    list_display = ['name','mail','title','text','date']

admin.site.register(Murojaat,AdminMurojaat)


class AdminObunaMail(admin.ModelAdmin):
    list_display = ['mail']

admin.site.register(Obunamail,AdminObunaMail)
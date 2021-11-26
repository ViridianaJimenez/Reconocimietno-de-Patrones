from django.contrib import admin
from .models import Tejido, Paciente

# Register your models here.


class TejidoAdmin(admin.ModelAdmin):
    list_display = ('color','temperatura','inflamacion', 'name')
    list_filter=('color','name',)

admin.site.register(Tejido, TejidoAdmin)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Paciente, PacienteAdmin)

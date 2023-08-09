from django.contrib import admin
from servicios.models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'update')

admin.site.register(Servicio, ServicioAdmin)

from django.contrib import admin
from .models import Empleado, Tecnico, Creacion, Productora, Casco
# Register your models here.
admin.site.register(Empleado)
admin.site.register(Tecnico)
admin.site.register(Creacion)
admin.site.register(Productora)
admin.site.register(Casco)


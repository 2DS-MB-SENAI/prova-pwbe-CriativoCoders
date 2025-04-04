from django.contrib import admin
from .models import Medico
from .models import Consulta
admin.site.register(Consulta)
admin.site.register(Medico)
# Register your models here.

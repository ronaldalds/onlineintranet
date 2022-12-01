from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Tipo)
class TipoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Poste)
class PosteAdmin(admin.ModelAdmin):
    pass

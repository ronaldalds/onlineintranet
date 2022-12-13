from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Ligacao)
class LigacaoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Trajeto)
class TrajetoAdmin(admin.ModelAdmin):
    pass

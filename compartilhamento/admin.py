from django.contrib import admin
from django.contrib.admin.models import LogEntry

from . import models


# Register your models here.
@admin.register(models.Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tipo)
class TipoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Rota)
class FtthAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Rede)
class RedeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Aprovacao)
class AprovacaoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Cabo)
class CaboAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Imagem)
class ImagemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ponto)
class PontoAdmin(admin.ModelAdmin):
    pass


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    search_fields = ('object_repr',)
    list_filter = ('action_time', 'content_type',)
    list_display = ('action_time', 'user',
                    'content_type', 'tipo', 'object_repr')
    fields = ('action_time', 'user', 'content_type', 'object_id',
              'object_repr', 'action_flag', 'change_message', )
    readonly_fields = ('action_time', 'user', 'content_type', 'object_id',
                       'object_repr', 'action_flag', 'tipo', 'change_message', )

    def tipo(self, obj):
        if obj.is_addition():
            return u"Adicionado"
        elif obj.is_change():
            return u"Modificado"
        elif obj.is_deletion():
            return u"Deletado"

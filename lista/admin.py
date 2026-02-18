from django.contrib import admin
from .models import tarefa


@admin.register(tarefa)
class TarefaAdmin(admin.ModelAdmin):

    # Campos exibidos na lista
    list_display = ('titulo', 'concluida', 'created_at', 'updated_at')

    # Campo clicável na lista
    list_display_links = ('titulo',)

    # Filtro lateral
    list_filter = ('concluida', 'created_at')

    # Campo de busca
    search_fields = ('titulo',)

    # Organização no formulário
    fields = ('titulo', 'concluida', 'created_at', 'updated_at')

    # Campos somente leitura (útil para auto_now)
    readonly_fields = ('created_at', 'updated_at')

from django.contrib.admin import register, ModelAdmin, TabularInline

from pypro.turmas.models import Turma


class MatriculaInline(TabularInline):
    model = Turma.alunos.through
    extra = 1
    readonly_fields = ('data',)
    autocomplete_fields = ('usuario',)
    ordering = ('-data',)


@register(Turma)
class TurmaAdmin(ModelAdmin):
    inlines = [MatriculaInline]
    list_display = ('nome', 'slug', 'inicio', 'fim')
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)

from django.contrib import admin

from pypro.aperitivos.models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'vimeo_id')
    ordering = ('creation',)
    prepopulated_fields = {'slug': ('titulo',)}

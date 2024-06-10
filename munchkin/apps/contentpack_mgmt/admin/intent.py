from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from apps.contentpack_mgmt.models import Intent, IntentCorpus


class IntentCorpusInline(admin.StackedInline):
    model = IntentCorpus
    show_change_link = True
    extra = 0


@admin.register(Intent)
class IntentAdmin(ModelAdmin):
    list_display = ['content_pack_link', 'name']
    search_fields = ['name']
    list_filter = ['content_pack', 'name']
    list_display_links = ['name']
    ordering = ['id']
    filter_horizontal = []
    inlines = [
        IntentCorpusInline
    ]

    def content_pack_link(self, obj):
        link = reverse("admin:contentpack_mgmt_contentpack_change", args=[obj.content_pack.id])
        return format_html('<a href="{}">{}</a>', link, obj.content_pack)

    content_pack_link.short_description = '扩展包'
from django.contrib import admin

# Register your models here.
from .models import Post, History

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "updated", "timestamp"]
    list_filter = ["updated", "timestamp"]
    list_display_links = ["updated"]
    list_editable = ["title"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('status', 'status_updated_at',
                    'updated_at', 'created_at')

admin.site.register(History, HistoryAdmin)
admin.site.register(Post, PostModelAdmin)

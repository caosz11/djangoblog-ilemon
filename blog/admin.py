from django.contrib import admin

# Register your models here.
from blog.models import Blog, Tag, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ('caption', 'id', 'publish_time')
    list_filter = ('publish_time',)
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)



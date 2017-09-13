from django.contrib import admin

from .models import Post


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, ArticleAdmin)

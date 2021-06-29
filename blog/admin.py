from django.contrib import admin
from . import models


admin.site.register(models.Tag)
admin.site.register(models.Profile)



@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('headline',), }

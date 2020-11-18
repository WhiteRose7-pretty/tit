from django.contrib import admin
from .models import Category, Article, Autor, Comment, PrivacyPolicy


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Autor)
admin.site.register(Comment)
admin.site.register(PrivacyPolicy)
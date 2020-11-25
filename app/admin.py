from django.contrib import admin
from .models import Category, Article, Autor, Comment, PrivacyPolicy, AddCategory, Add
from .models import AdsSetting, SubscriberEmail


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Autor)
admin.site.register(Comment)
admin.site.register(PrivacyPolicy)
admin.site.register(AdsSetting)
admin.site.register(SubscriberEmail)


class AddCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'img_url')
    list_display_links = ('pk', )
    list_editable = ('name', 'slug', 'img_url')
    prepopulated_fields = {'slug': ('name',)}


class AddAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('content',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CategoryAdmin)
admin.site.register(Add, AddAdmin)
admin.site.register(AddCategory, AddCategoryAdmin)


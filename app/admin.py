from django.contrib import admin
from app.models import Category, Article, Autor, Comment, PrivacyPolicy, AddCategory, Add
from app.models import AdsSetting, SubscriberEmail, ContactMessage, FullAccess, FullAccessSubscription, Przelewy24Transaction
from app.models import AdminSetting

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Autor)
admin.site.register(Comment)
admin.site.register(PrivacyPolicy)
admin.site.register(AdsSetting)
admin.site.register(SubscriberEmail)
admin.site.register(FullAccess)
admin.site.register(FullAccessSubscription)


class AddCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug', 'img_url')
    list_display_links = ('pk', )
    list_editable = ('name', 'slug', 'img_url')
    prepopulated_fields = {'slug': ('name',)}


class AddAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('content',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Add, AddAdmin)
admin.site.register(AddCategory, AddCategoryAdmin)
admin.site.register(ContactMessage)
admin.site.register(Przelewy24Transaction)
admin.site.register(AdminSetting)



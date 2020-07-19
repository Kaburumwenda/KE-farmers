from django.contrib import admin

# Register your models here.
from HOME.models import Setting, ContactMessage, FAQ, SettingLang , Language, Adverts


class SettingtAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'update_at','status']
    readonly_fields =('name','subject','email','message','ip')
    list_filter = ['status']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','ordernumber','lang','status'] #,'lang'
    list_filter = ['status','lang'] #,'lang'

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'code','status']
    list_filter = ['status']

class AdvertsAdmin(admin.ModelAdmin):
    list_display = ['title','status', 'image_tag']
    list_filter = ['status']
    readonly_fields = ['image_tag']

class SettingLangAdmin(admin.ModelAdmin):
    list_display = ['title','lang', 'keywords','description'] # ,'lang'
    list_filter = ['lang'] #,'lang'

admin.site.register(Setting,SettingtAdmin)
admin.site.register(SettingLang,SettingLangAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
admin.site.register(FAQ,FAQAdmin)
admin.site.register(Adverts,AdvertsAdmin)
admin.site.register(Language,LanguagesAdmin)



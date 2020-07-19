from django.contrib import admin

# Register your models here.
from UMS.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','currency','language','image_tag'] # ,'currency,'language'

admin.site.register(UserProfile,UserProfileAdmin)
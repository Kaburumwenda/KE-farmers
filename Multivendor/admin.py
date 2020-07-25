from django.contrib import admin

# Register your models here.
from .models import MultivendorProduct,Condition



class MultivendorProductAdmin(admin.ModelAdmin):
    list_display = ['user','title','condition','note', 'update_at','status']
    readonly_fields =('user','firstname','title','ip','condition','address','phone',
    	     'lastname','email','businessname','description','price','discount','amount')
    list_filter = ['status','condition']

admin.site.register(MultivendorProduct, MultivendorProductAdmin)
admin.site.register(Condition)
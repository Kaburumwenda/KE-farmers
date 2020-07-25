from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import MultivendorProduct
from .forms import MultivendorProductForm
from HOME.models import Setting
from PMS.models import Category
from CORE import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request

def vendorproductslist(request):
	pass



@login_required(login_url='/login') # Check login
def multivendorform(request):
    currentlang = request.LANGUAGE_CODE[0:2]
    #category = categoryTree(0,'',currentlang)
    category = Category.objects.all()
    if request.method == 'POST': # check post
        form = MultivendorProductForm(request.POST)
        if form.is_valid():
            data = MultivendorProduct() #create relation with model
            data.firstname = form.cleaned_data['firstname'] # get form input data
            data.lastname = form.cleaned_data['lastname']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.address = form.cleaned_data['address']
            data.businessname = form.cleaned_data['businessname']
            data.title = form.cleaned_data['title']
            data.condition = form.cleaned_data['condition']
            data.price = form.cleaned_data['price']
            data.discount = form.cleaned_data['discount']
            data.amount = form.cleaned_data['amount']
            data.description = form.cleaned_data['description']
            data.ip = request.META.get('REMOTE_ADDR')
            current_user = request.user
            data.user_id=current_user.id
            data.save()  #save data to table
            messages.success(request,"Your Product has ben sent.You will be contacted within 48 hours for further details. Thank you for your interest.")
            return HttpResponseRedirect('/vendors')

    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)
    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)

    form = MultivendorProductForm
    context={'setting':setting,'form':form, 'category':category }
    return render(request, 'multivendorform.html', context)

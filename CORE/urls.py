"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from HOME import views
from POS import views as OrderViews
from UMS import views as UserViews
from Multivendor import views as MultivendorsViews
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
    path('selectcurrency', views.selectcurrency, name='selectcurrency'),
    path('savelangcur', views.savelangcur, name='savelangcur'),
    path('i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    path('currencies/', include('currencies.urls')),
    path(_('admin/'), admin.site.urls),
    path('', views.index, name='home'),
    path('home/', include('HOME.urls')),
    path('product/', include('PMS.urls')),
    path('order/', include('POS.urls')),
    path('user/', include('UMS.urls'), name='user'),
    path('ckeditor/', include('ckeditor_uploader.urls')),


    path(_('about/'), views.aboutus, name='aboutus'),
    path(_('contact/'), views.contactus, name='contactus'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('shopcart/', OrderViews.shopcart, name='shopcart'),
    path('login/', UserViews.login_form, name='login'),
    path('logout/', UserViews.logout_func, name='logout'),
    path('signup/', UserViews.signup_form, name='signup'),
    path('faq/', views.faq, name='faq'),
    path('languages/', views.languages, name='languages'),
    path('currency/', views.currency, name='currency'),
    path('payments/', OrderViews.payments, name='payments'),
    path('vendors/',MultivendorsViews.multivendorform, name='multivendorform'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor'),
    prefix_default_language=False,
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
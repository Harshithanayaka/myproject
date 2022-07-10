"""webProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from offers import views

from webProject.routers import router
from django.urls import include, path
from rest_framework import routers
from offers.views import Userdetailslist
from offers.viewsets import UserdetailsViewSet

router = routers.DefaultRouter()
router.register(
    'list', UserdetailsViewSet, basename='list'
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('new', views.new, name='new'),
    path('npostpaid',views.npostpaid,name='npostpaid'),
    path('ndongle',views.ndongle,name='ndongle'),
    path('update/<int:id>', views.update, name='update'),
    path('upostpaid/<int:id>',views.upostpaid,name='upostpaid'),
    path('udongle/<int:id>',views.udongle,name='udongle'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('dpostpaid/<int:id>', views.dpostpaid, name='dpostpaid'),
    path('ddongle/<int:id>', views.ddongle, name='ddongle'),
    path('register/',views.register,name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('Adminhome/',views.Adminhome,name='Adminhome'),
    path('api/', include(router.urls)),
    # path('list/',views.get,name='get')
]

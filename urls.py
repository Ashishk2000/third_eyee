from django.contrib import admin
from django.urls import path, include
from webapp import views
from django.conf import settings
from django.conf.urls.static import static
from database import views




urlpatterns = [
    path("<int:id>",views.BranchDetails),
    path('livedata/<int:id>',views.DataViaAjax),
] 

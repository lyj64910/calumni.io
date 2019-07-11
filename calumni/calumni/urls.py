from django.contrib import admin
from django.urls import path
from cal import views as cal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cal.home, name="home"),
    path('new/', cal.new, name="new"),
    path('create/', cal.create, name="create"),
]

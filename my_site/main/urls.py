from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', showtasks, name = 'showtasks'),
    path('posttask/', get_task, name = 'get_task'),
]
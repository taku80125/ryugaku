from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.index, name='home'),
    path('money/',views.money, name='money'),
]
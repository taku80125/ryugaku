from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.index, name='home'),
    path('money/',views.money, name='money'),
    path('contact/',views.contact, name='contact'),
    path('language/',views.language, name='language'),
    path('programming/',views.programming, name='programming'),
    path('getback/',views.getback, name='getback'),

]
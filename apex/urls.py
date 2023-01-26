from django.urls import path, register_converter

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:field>/<str:value>', views.return_search_results, name='search'),
    path('profile/<str:uid>', views.return_profile, name='profile'),
    path('create/new', views.create_profile, name='crearte new profile'),
    path('create/opd', views.create_opd, name='crearte new opd'),
    path('update/opd', views.update_opd_record, name='Update OPD'),
    path('dayopd/<str:from_date>/<str:to_date>', views.return_day_opd, name='day_opd')
]
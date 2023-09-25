from django.contrib import admin
from django.urls import path
from lynx import views



urlpatterns = [
    path('', views.home),




    



    path('login/',views.login),
    path('loginIN/',views.loginIN),
    path('search/',views.search),
    # path('excel_data/',views.excel_data),
    # path('jsondata/',views.jsondata),
    path('display_variants/',views.display_variants),
    path('searchnew/',views.searchnew),
    path('searchgene/',views.searchgene),
    # path('codepage/',views.codepage),
    path('dhdds/',views.dhdds),
    path('search_results/', views.search_results, name='search_results'),
    path('prpf3/',views.prpf3),
    path('samd11/',views.samd11),
    path('crb1/',views.crb1),
    path('searchapi/',views.searchapi),
    


    

]



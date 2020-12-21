from django.urls import path
#from .views import SearchProductView
from . import views
urlpatterns = [
    path('user', views.search_youth_user, name='search_youth_user'),

    path('company', views.search_company_user, name='search_company_user'),
]
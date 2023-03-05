from django.urls import path
from processors.views import CountryGDPYoungestAge

urlpatterns = [
    path('gdp_youngest_age/<str:iso_code>/', CountryGDPYoungestAge.as_view()),
]
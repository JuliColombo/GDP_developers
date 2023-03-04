from django.urls import path
from processors.views import CountryGDPYoungestAge

urlpatterns = [
    path('gdp_youngest_age', CountryGDPYoungestAge.as_view()),
]
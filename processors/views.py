from django.http import JsonResponse, HttpResponseBadRequest
from django.db.models import Min
from rest_framework.views import APIView

from readers.models import GrossDomesticProduct, StackOverflowResponse


class CountryGDPYoungestAge(APIView):
    def youngest_age_range(self, min_age):
        match min_age:
            case 0:
                return 'Younger than 5 years'
            case 5:
                return '5 - 10 years'
            case 11:
                return '11 - 17 years'
            case 18:
                return '18 - 24 years'
            case 25:
                return '25 - 34 years'
            case 35:
                return '35 - 44 years'
            case 45:
                return '45 - 54 years'
            case 55:
                return '55 - 64 years'
            case 65:
                return 'Older than 64 years'

    def post(self, request):
        country_iso_code = request.data['iso_code']
        gdp = GrossDomesticProduct.objects.filter(country_iso=country_iso_code.upper()).first()
        if not gdp:
            return HttpResponseBadRequest()
        min_age = StackOverflowResponse.objects.filter(country_name=gdp.country_name).aggregate(min_age_total=Min('min_age_first_code'))['min_age_total']
        youngest_age = self.youngest_age_range(min_age)
        return JsonResponse({'country': gdp.country_name,
                             'gross_domestic_product': gdp.gross_domestic_product,
                             'youngest_age': youngest_age})

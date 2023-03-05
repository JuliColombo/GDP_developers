from django.db import models


class GrossDomesticProduct(models.Model):
    country_name = models.CharField(max_length=100)
    country_iso = models.CharField(max_length=2)
    gross_domestic_product = models.IntegerField()


class StackOverflowResponse(models.Model):
    country_name = models.CharField(max_length=100)
    min_age_first_code = models.IntegerField()
    max_age_first_code = models.IntegerField(null=True)


class ProgrammingLanguageResponse(models.Model):
    name = models.CharField(max_length=30)
    survey_response = models.ForeignKey(StackOverflowResponse, on_delete=models.CASCADE, related_name='languages')

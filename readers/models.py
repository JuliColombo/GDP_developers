from django.db import models


class GDP(models.Model):
    country_name = models.CharField(max_length=100)
    country_iso = models.CharField(max_length=2)
    gross_domestic_product = models.IntegerField()


class StackOverflow(models.Model):
    country_name = models.CharField(max_length=100)
    min_age_first_code = models.IntegerField()
    max_age_first_code = models.IntegerField(null=True)
    languages_raw = models.TextField()
    gdp = models.ForeignKey(GDP, on_delete=models.CASCADE, related_name='survey_responses', null=True, default=None)

    @property
    def languages(self):
        return self.languages_raw.split(";")

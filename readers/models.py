from django.db import models

class StackOverflow(models.Model):
    country_name = models.CharField(max_length=100)
    age_first_code = models.CharField(max_length=30)
    languages_raw = models.TextField()

    @property
    def languages(self):
        return self.languages_raw.split(";")


class GDP(models.Model):
    country_name = models.CharField(max_length=100)
    country_iso = models.CharField(max_length=2)
    gross_domestic_product = models.IntegerField()

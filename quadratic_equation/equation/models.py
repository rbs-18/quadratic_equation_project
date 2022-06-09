from django.db import models


class Equation(models.Model):
    """ Model of equation. """

    coefficient_1 = models.FloatField(null=True, blank=True)
    coefficient_2 = models.FloatField(null=True, blank=True)
    coefficient_3 = models.FloatField(null=True, blank=True)
    root_1 = models.FloatField(null=True, blank=True)
    root_2 = models.FloatField(null=True, blank=True)
    answer = models.CharField(max_length=30)

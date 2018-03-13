from django.db import models
from datetime import datetime


class Currency(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code


class Pair(models.Model):
    currency_first = models.ForeignKey(
                            Currency,
                            on_delete=models.CASCADE,
                            related_name='currency_first',
                            null=True)

    currency_second = models.ForeignKey(
                            Currency,
                            on_delete=models.CASCADE,
                            related_name='currency_second',
                            null=True)

    def __str__(self):
        return "{}-{}".format(self.currency_first, self.currency_second)

    class Meta:
        unique_together = ('currency_first', 'currency_second',)


class Price(models.Model):
    pair = models.ForeignKey(Pair, on_delete=models.CASCADE)
    price = models.FloatField(null=True, blank=True, default=0.0)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "{}: {}".format(self.pair, self.price)
        # return "{}: {} {}".format(self.pair, self.price, self.date)

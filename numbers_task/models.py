from django.db import models

class Number(models.Model):
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.number)
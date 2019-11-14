from django.db import models


class AuCode(models.Model):
    code = models.CharField(max_length=30)
    add_date = models.DateTimeField('date added')

    def __str__(self):
        return self.code


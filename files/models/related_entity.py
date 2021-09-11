import jsonfield
from django.db import models


class RelatedEntity(models.Model):

    barcode = models.CharField(max_length=50, null=True)
    metadata = jsonfield.JSONField()



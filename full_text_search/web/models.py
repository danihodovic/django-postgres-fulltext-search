from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex

class Page(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()

    # New modifications. A field and an index
    content_search = SearchVectorField(null=True)

    class Meta:
        indexes = [GinIndex(fields=["content_search"])]

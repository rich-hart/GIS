from django.db import models

# Create your models here.

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Tag(models.Model):
    instance = models.ForeignKey(
        Base,
        on_delete=models.CASCADE,
        related_name="tags",
        related_query_name="tag",
    )
    name = models.CharField(
        max_length=127,
    #        choices=Type.get_choices(),
        null = True,
        blank = True,
        default=None,
    )
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
        ordering = ['-created']

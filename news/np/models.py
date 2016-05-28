from django.db import models


class Article(models.Model):
    SECTION_CHOICES = (
        ('NZ', 'NZ'),
        ('INTERNATIONAL', 'International'),
        ('TECH', 'Tech'),
        ('SPORT', 'Sport'),
    )

    author = models.CharField(max_length=100)
    title = models.TextField(max_length=140)
    section = models.CharField(max_length=15, choices=SECTION_CHOICES, default='NZ')
    intro = models.CharField(max_length=200)
    text = models.TextField(null=True)
    image = models.URLField(null=True)
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


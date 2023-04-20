from django.db import models


class Season(models.Model):
    season = models.CharField(max_length=6)

    def __str__(self):
        return self.season


class SportItem(models.Model):
    image =  models.ImageField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
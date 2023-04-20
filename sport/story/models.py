from django.db import models


class Story(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.heading

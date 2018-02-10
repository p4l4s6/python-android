from django.db import models

# Create your models here.


class Review(models.Model):
    review_count = models.IntegerField()
    comment = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
from django.db import models

# Create your models here.


class List(models.Model):
    item = models.CharField(max_length=250)
    completed = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + "-" + self.item

    class Meta:
        ordering = ('-added_at',)

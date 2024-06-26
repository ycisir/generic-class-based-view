from django.db import models
from django.urls import reverse

class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=15)

    # def get_absolute_url(self):
    #     return reverse("thanks")

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
    

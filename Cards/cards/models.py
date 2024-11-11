from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    german_sentence = models.TextField()
    hungarian_sentence = models.TextField()
    i_knew_counter = models.IntegerField()
    did_not_knew_counter = models.IntegerField()

    def __str__(self):
        return self.german_sentence
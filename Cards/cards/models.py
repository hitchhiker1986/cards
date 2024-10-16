from django.db import models

# Create your models here.
class Card(models.Model):
    german_sentence = models.TextField()
    hungarian_sentence = models.TextField()
    i_knew_counter = models.IntegerField()
    did_not_knew_counter = models.IntegerField()

    def __str__(self):
        return self.german_sentence
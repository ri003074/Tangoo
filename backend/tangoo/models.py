from django.db import models

# Create your models here.

class Tangoo(models.Model):
    phrase_ja  = models.CharField(max_length=200)
    phrase_en  = models.CharField(max_length=200)
    word_en    = models.CharField(max_length=200)
    supplement = models.TextField(default=None, blank=True, null=True)
    s_counter  = models.IntegerField(default=1)
    c_counter  = models.IntegerField(default=1)

    def __str__(self):
        return self.word_en
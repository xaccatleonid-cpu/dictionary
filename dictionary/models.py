from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Word(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='words')
    original = models.CharField(max_length=255)
    translation = models.TextField()

    def __str__(self):
        return f"{self.original} → {self.translation}"

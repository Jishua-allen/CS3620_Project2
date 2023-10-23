from django.db import models

# Create your models here.

class Story(models.Model):
  title = models.CharField(max_length=100)
  text = models.CharField(max_length=1000)
  def __str__(self):
    return self.title
  
class Word(models.Model):
  story = models.ForeignKey(Story, on_delete=models.CASCADE)
  typeOfWord = models.CharField(max_length=100)
  wordOrder = models.IntegerField()
  def __str__(self):
    return self.typeOfWord + " " + str(self.wordOrder) + " " + self.story.title
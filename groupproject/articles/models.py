from django.db import models
import datetime

class Section(models.Model):
  name = models.CharField(max_length=100, default="")

  def __str__(self):
    return self.name

class Article(models.Model):
  title = models.CharField(max_length=100, default="")
  author = models.CharField(max_length=250, default="")
  section = models.OneToOneField(Section, default="", on_delete=models.CASCADE)
  description = models.TextField(default="")
  pub_date = models.DateTimeField('date_published', auto_now=True)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    self.pub_date = datetime.datetime.now()



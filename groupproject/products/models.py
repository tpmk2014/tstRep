from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
  name = models.CharField('Nazwa produktu', max_length=100)
  caloric_content = models.CharField('Wartość kaloryczna na 100 g prodkuktu', max_length=10)

  def __str__(self):
    return self.name


class Calories(models.Model):
  user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE)
  weight = models.IntegerField(default="100")
  calories_sum = models.IntegerField(default="0")
  date = models.DateTimeField('date_created', auto_now=True)

  def __str__(self):
    return str(self.user)

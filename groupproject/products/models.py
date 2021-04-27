from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Product(models.Model):
  name = models.CharField(max_length=100)
  caloric_content = models.CharField(max_length=10)

  def __str__(self):
    return self.name


class Calories(models.Model):
  user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE)
  weight = models.IntegerField(default="100")
  calories_sum = models.IntegerField(default="0")
  date = models.DateTimeField('date_created')

  def __str__(self):
    return str(self.user)

  def save(self, *args, **kwargs):
    caloric_value = Product.objects.get(name=self.product).caloric_content
    self.calories_sum = str(int(caloric_value) * int(self.weight))
    super(Calories, self).save(*args, **kwargs)
    self.date = timezone.now()
    super(Calories, self).save(*args, **kwargs)

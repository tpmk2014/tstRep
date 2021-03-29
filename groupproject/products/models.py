from django.db import models


class Product(models.Model):
  name = models.CharField('Nazwa produktu', max_length=100)
  caloric_content = models.CharField('Wartość kaloryczna na 100 g prodkuktu', max_length=10)

  def __str__(self):
    return self.name


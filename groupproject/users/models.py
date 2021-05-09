from django.db import models

class Trainer(models.Model):
  photo = models.ImageField(default="", upload_to="trainers_photo")
  first_name = models.CharField(max_length=50, default="")
  second_name = models.CharField(max_length=50, default="", blank=True)
  last_name = models.CharField(max_length=50, default="")
  occupation = models.CharField(max_length=150, default="")
  email = models.EmailField(default="")
  phone_number = models.CharField(max_length=12, default="")
  info = models.TextField(default="")

  def __str__(self):
    return str(self.first_name) + " " + str(self.last_name)



from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from products.forms import ProductForm, CaloriesForm
from products.models import Calories, Product

from users.models import Trainer
from django.core.exceptions import ObjectDoesNotExist

from requests import get
from ip2geotools.databases.noncommercial import DbIpCity
import requests, json
from translate import Translator

openweathermap_api_key = "dd86f6b5b099f8d3b79ea6d6919eecd4"

def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('users:dashboard')
  else:
    form = AuthenticationForm()
  context = {'form': form}
  return render(request, "users/login.html", context)


def registration_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('users:dashboard')
  else:
    form = UserCreationForm()
  context = {'form': form}
  return render(request, 'users/registration.html', context)


@login_required
def logout_view(request):
  logout(request)
  return redirect('pages:home')


@login_required
def dashboard_view(request):
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  ip = get('https://api.ipify.org').text
  response = DbIpCity.get(ip, api_key='free')
  city_name = response.city
  translator = Translator(to_lang="pl")


  complete_url = base_url + "appid=" + openweathermap_api_key + "&q=" + city_name
  response = requests.get(complete_url)
  json_response = response.json()

  if json_response["cod"] != "404":
    json_main = json_response["main"]
    json_weather = json_response["weather"][0]

    current_temperature = int(json_main["temp"]) - 273
    temperature_feels_like = int(json_main["feels_like"]) - 273
    current_pressure = json_main["pressure"]
    current_humidity = json_main["humidity"]
    wind_speed = json_response["wind"]["speed"]
    weather = str(json_weather["description"])
    weather_pl = translator.translate(weather)
    if "weather condition" in weather_pl:
      weather_pl = weather_pl.replace("weather condition", "")
    clouds = json_response["clouds"]["all"]
  else:
    print(" City Not Found ")

  dashboard_template = "users/dashboard.html"
  context = {"city_name": city_name, "temperature": current_temperature, "feels_like": temperature_feels_like, "pressure": current_pressure, "humidity": current_humidity, "wind_speed": wind_speed, "weather": weather_pl,"clouds": clouds}
  return render(request, dashboard_template, context)


@login_required
def bmi_calculator_view(request):
  context = {}
  template = "users/bmi_calculator.html"
  return render(request, template, context)


@login_required
def articles_view(request):
  trainers = Trainer.objects.all()
  context = {'trainers': trainers}
  template = "users/articles.html"
  return render(request, template, context)


@login_required
def my_calories_view(request):
  message = ""
  user_calories = Calories.objects.filter(user=request.user).order_by("-date")
  product_form = ProductForm()
  calories_form = CaloriesForm()
  # Adding products to base
  if request.method == 'POST':
    product_form = ProductForm(request.POST)
    if product_form.is_valid():
      name = product_form.cleaned_data['name']
      caloric_content = product_form.cleaned_data['caloric_content']
      try:
        Product.objects.get(name=name.lower(), caloric_content=caloric_content)
        message = "Produkt już istnieje w bazie"
      except ObjectDoesNotExist:
        Product.objects.create(name=name.lower(), caloric_content=caloric_content)
        message = "Produkt został dodany do bazy"
    else:
      product_form = ProductForm()
  # Adding products to user list
  if request.method == 'POST':
    calories_form = CaloriesForm(request.POST)
    if calories_form.is_valid():
      product = calories_form.cleaned_data['product']
      weight = calories_form.cleaned_data['weight']
      product = product.lower()
      try:
        db_product = Product.objects.get(name=product)
        Calories.objects.create(user=request.user, product=db_product, weight=weight)
        message = "Produkt został dodany"
      except ObjectDoesNotExist:
        message = "Produkt nie istnieje w bazie"
    else:
      calories_form = CaloriesForm()
  context = {'product_form': product_form, 'user_calories': user_calories, 'calories_form': calories_form, 'message': message}
  template = "users/user_calories.html"
  return render(request, template, context)


@login_required
def change_user_password_view(request):
  context = {}
  template = "users/change_password.html"
  return render(request, template, context)

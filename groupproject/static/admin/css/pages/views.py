from django.shortcuts import render
from categories.models import Category
from faq.models import Faq
from courses.models import Course, Lesson
from users.forms import CustomSignupForm
from logotypes.models import Logotype

def index(request):
    categories = Category.objects.all()
    faqs = Faq.objects.all()
    form = CustomSignupForm
    logotypes = Logotype.objects.all()
    num_courses = Course.objects.all().count()
    courses = Course.objects.all()
    promoted_course = Course.objects.get(is_promoted=True)
    lessons = Lesson.objects.filter(course=promoted_course)
    lesson = lessons[0]
    
    return render(request, 'pages/index.html', {'categories': categories, 'faqs': faqs, 'form': form, 'num_courses': num_courses, 'logotypes': logotypes, 'courses': courses, 'promoted_course': promoted_course, 'lesson': lesson})

    
# function for staticpages
def staticpage(request):
	form  = None
	if request.path == '/o-nas':
		form = CustomSignupForm
		staticpage_template = 'pages/about_us.html'
	elif request.path == '/cennik':
		staticpage_template = 'pages/pricing.html'
	elif request.path == '/regulamin':
 		staticpage_template = 'pages/terms_of_service.html'
	elif request.path == '/kontakt':
		staticpage_template = 'pages/contact_us.html'
	elif request.path == '/prywatnosc':
		staticpage_template = 'pages/privacy.html'

	return render(request, staticpage_template, {'form': form})









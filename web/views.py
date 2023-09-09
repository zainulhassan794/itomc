from django.shortcuts import render 
from django.views.generic import ListView , DetailView 
from .models import Free_Tutorials , Paid_Courses



# Home Page
# class Home_View(ListView):
# 	# model = Post
# 	template_name = "index.html"
# 	ordering = ['-id']


# def home(request):
# 	return render(request, "index.html", {})


# Home Page
class Home_View(ListView):
	model = Free_Tutorials
	template_name = "index.html"
	ordering = ['-id']

# Free Tutorial Page
class Free_View(DetailView):
	model = Free_Tutorials
	template_name = "free_view.html"


class P_Courses(ListView):
	model = Paid_Courses
	template_name = "paid_courses.html"


class P_Courses_View(DetailView):
	model = Paid_Courses
	template_name = "paid_courses_view.html"

def tools_view(request):
	return render(request , "tools.html" , {})

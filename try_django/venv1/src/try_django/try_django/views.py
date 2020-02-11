# Model View Template(MVT)
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
#Dont Repeat Yourself=DRY


def home_page(request):

	#doc="<h1>{title}</h1>".format(title=my_title)
	#django_rendered_doc="<h1>{{title}}</h1>".format(title=my_title)
	my_title="Hello there!!"
	context = {"title": "my_title"}
	if request.user.is_authenticated:
		context={"title":my_title, "my_list":[1,2,3,4,5]}
	return render(request,"home.html",context)
	# template_name="title.txt"
	# template_obj=get_template(template_name)
	# rendered_string= template_obj.render(context)
	# print(rendered_string)
	
	

def about_page(request):
	return render(request,"about.html",{"title":"About us"})

def contact_page(request):
	return render(request,"hello_world.html",{"title":"Contact us"})

def example_page(request):
	context={"title":"Example"}
	template_name="hello_world.html"
	template_obj= get_template(template_name)
	rendered_item= template_obj.render(context)
	return HttpResponse(rendered_item)
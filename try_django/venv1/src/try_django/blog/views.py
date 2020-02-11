from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .models import BlogPost

# obj=BlogPost.objects.get(id=1)

def blog_post_detail_page(request, post_id):
	try:
		obj= BlogPost.objects.get(id=post_id) #query->datatbase-->data-->django renders it
	except BlogPost.objects.DoesNotExist:
		raise Http404
	except ValueError:
		raise Http404

	template_name= "blog_post_detail.html"
	context={"object":obj}
	return render(request, template_name, context)
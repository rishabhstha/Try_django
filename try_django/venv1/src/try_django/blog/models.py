from django.db import models

# Create your models here.
# models allow us to store datat in the database in a very specific way
class BlogPost(models.Model):
	title= models.TextField()
	content=models.TextField(null=True, blank=True)


from django.db import models

# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length= 200)
	title_author = models.ForeignKey('auth.User',on_delete = models.CASCADE)
	title_body = models.TextField(max_length= 500 )

	def __str__(self):
		return self.title
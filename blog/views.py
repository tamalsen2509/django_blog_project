from django.shortcuts import render
from django.views.generic import ListView , DetailView

from . models import BlogPost

class BlogListView(ListView):
	model = BlogPost
	template_name = 'home.html'


class BlogDetailView(DetailView):
	model = BlogPost
	template_name = 'post_detail.html'
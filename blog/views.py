__author__ = 'caosz'
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Blog, Category, Tag
from django.http import Http404

def blog_list(request):
    blog_list = Blog.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render_to_response('blog_list.html', {'blogs': blog_list, 'categories': categories, 'tags': tags})


def blog_article(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
        categories = Category.objects.all()
        tags = Tag.objects.all()
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response('blog_article.html', {'blog': blog, 'slug': slug, 'categories': categories, 'tags': tags})


def category(request, slug):
    cut_category = get_object_or_404(Category, slug=slug)
    blogs = cut_category.blog_set.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render_to_response('blog_list.html', {'blogs': blogs, 'categories': categories, 'tags': tags})


def tag(request, slug):
    cut_tag = get_object_or_404(Tag, slug=slug)
    blogs = cut_tag.blog_set.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render_to_response('blog_list.html', {'blogs': blogs, 'categories': categories, 'tags': tags})

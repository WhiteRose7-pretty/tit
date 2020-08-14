from django.shortcuts import render
from .models import Article, Comment
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'app/home.html')



def article(request, slug):
    object = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(owner=object)

    context = {'object': object}
    return render(request, 'app/article.html', context)
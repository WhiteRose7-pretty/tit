from django.shortcuts import render
from .models import Article, Comment
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'app/home.html')



def article(request, slug):
    object = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(owner=object, display=True)
    content_display = False
    if object.premium:
        if request.user.is_authenticated:
            if request.user.premium:
                content_display = True
    else:
        content_display = True

    context = {'object': object,
               'content_display': content_display,
               'comments': comments,}
    return render(request, 'app/article.html', context)



def comment(request):
    data = request.POST
    article_id = data.get('article_id', False)
    article_obj = Article.objects.get(pk=article_id)
    comment_obj = Comment()
    comment_obj.name = data.get('full_name', False)
    comment_obj.content = data.get('content', False)
    comment_obj.owner = article_obj
    if request.user.is_authenticated:
        comment_obj.user = request.user
    comment_obj.save()
    return HttpResponseRedirect('/artykul/' + article_obj.slug + '/#comment_list')


from django.shortcuts import render
from .models import Article, Comment, Category, PrivacyPolicy
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from simple_cms.models import HomePage
import html2text
from datetime import datetime



def home(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()

    context = {'categories': categories,
               'object': home_page}
    return render(request, 'app/home.html', context)



def article(request, slug):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    request.session['latest_reed'] = slug
    object = get_object_or_404(Article, slug=slug)
    comments = Comment.objects.filter(owner=object, display=True)
    content_display = False
    if object.premium:
        if request.user.is_authenticated:
            if request.user.premium:
                content_display = True
    else:
        content_display = True
    if not content_display:
        h = html2text.HTML2Text()
        h.escape_all = True
        h.ignore_links = True
        h.ignore_emphasis = True
        h.ignore_images = True
        h.ignore_tables = True
        h.hide_strikethrough = True
        object.content_text = h.handle(object.content)

    context = {'obj': object,
               'slug': slug,
               'categories': categories,
               'object': home_page,
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



def small_ads(request, slug):
    return render(request, 'app/small_ads.html')



def articles(request, slug):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()

    context = {'categories': categories,
               'object': home_page}
    return render(request, 'app/articles.html', context)



def pricing_paper(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()

    context = {'categories': categories,
               'object': home_page}
    return render(request, 'app/pricing_paper.html', context)


def pricing_internet(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()

    context = {'categories': categories,
               'object': home_page}
    return render(request, 'app/pricing_internet.html', context)


def search(request):
    return render(request, 'app/search.html')



def about(request):
    return render(request, 'app/about.html')



def contact(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()

    context = {'categories': categories,
               'object': home_page}
    return render(request, 'app/contact.html', context)



def privacy(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    obj = PrivacyPolicy.objects.last()

    context = {'categories': categories,
               'obj': obj,
               'object': home_page}
    return render(request, 'app/privacy.html', context)



def regulations(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    obj = PrivacyPolicy.objects.last()

    context = {'categories': categories,
               'obj': obj,
               'object': home_page}
    return render(request, 'app/regulations.html', context)

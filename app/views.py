from django.shortcuts import render
from .models import Article, Comment, Category, PrivacyPolicy, Add, AddCategory
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from simple_cms.models import HomePage
import html2text
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def home(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    # numbers
    small_article_numbers = []
    slider_lg_basic_numbers = []
    section_second_left = []
    sm_basic_under_numbers = []
    section_second_numbers = ['1', '2']
    basic_center_numbers = ['1', '2']
    tab_article_numbers = [
        ['1', '2'],
        ['3', '4'],
        ['5', '6'],
    ]
    small_section_second_numbers = [
        ['1', '2'],
        ['3', '4'],
    ]
    section_footer_numbers = [
        ['1', '2', '3', '4'],
        ['5', '6', '7', '8'],
        ['9', '10', '11', '12'],
    ]
    section_footer_title = [
        'Towarzyskie', 'Turystyczne', 'Naukowe',
    ]

    for item in range(1, 8):
        small_article_numbers.append(str(item))

    for item in range(1, 10):
        slider_lg_basic_numbers.append(str(item))

    for item in range(1, 6):
        section_second_left.append(str(item))

    for item in range(1, 6):
        sm_basic_under_numbers.append(str(item))

    context = {'categories': categories,
               'object': home_page,
               'small_article_numbers': small_article_numbers,
               'slider_lg_basic_numbers': slider_lg_basic_numbers,
               'tab_article_numbers': tab_article_numbers,
               'section_second_numbers': section_second_numbers,
               'small_section_second_numbers': small_section_second_numbers,
               'section_second_left_numbers': section_second_left,
               'basic_center_numbers': basic_center_numbers,
               'sm_basic_under_numbers': sm_basic_under_numbers,
               'section_footer_numbers': section_footer_numbers,
               'section_footer_title': section_footer_title,
               }

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
               'comments': comments, }
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


def articles(request, slug=''):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()

    if slug != '':
        article_lists_all = Article.objects.filter(category__slug=slug)
    else:
        article_lists_all = Article.objects.all()

    q_search = request.GET.get('search', '')

    article_lists_all = article_lists_all.filter(Q(title__contains=q_search) | Q(content__contains=q_search))

    cur_category = Category.objects.filter(slug=slug).first()
    page = request.GET.get('page', 1)
    paginator = Paginator(article_lists_all, 3)
    try:
        article_lists = paginator.page(page)
    except PageNotAnInteger:
        article_lists = paginator.page(1)
    except EmptyPage:
        article_lists = paginator.page(paginator.num_pages)

    context = {
        'categories': categories,
        'object': home_page,
        'article_all': article_lists_all,
        'article_lists': article_lists,
        'cur_category': cur_category,
    }

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


def add_list(request, slug):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    add_lists_all = Add.objects.filter(category__slug__exact=slug)
    cur_category = AddCategory.objects.filter(slug=slug).first()

    page = request.GET.get('page', 1)
    paginator = Paginator(add_lists_all, 3)
    try:
        add_lists = paginator.page(page)
    except PageNotAnInteger:
        add_lists = paginator.page(1)
    except EmptyPage:
        add_lists = paginator.page(paginator.num_pages)

    context = {
               'categories': categories,
               'object': home_page,
               'add_lists_all': add_lists_all,
               'add_lists': add_lists,
               'cur_category': cur_category,
               }

    return render(request, 'app/add_lists.html', context)


def add_detail(request, slug):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    request.session['latest_reed'] = slug
    object = get_object_or_404(Add, slug=slug)

    context = {'obj': object,
               'slug': slug,
               'categories': categories,
               'object': home_page,
               }
    return render(request, 'app/add_detail.html', context)


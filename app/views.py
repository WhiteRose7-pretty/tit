from django.core.mail import send_mail
from django.shortcuts import render
from .models import Article, Comment, Category, PrivacyPolicy, Add, AddCategory, AdsSetting, FullAccess, \
    FullAccessSubscription
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from simple_cms.models import HomePage
import html2text
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .forms import NewAddForm, SubscribeForm, ContactForm, Przelewy24PrepareForm
from .models import SubscriberEmail
from app_rama import settings
import requests
import hashlib
from django.contrib.auth.decorators import login_required
from app_rama import settings

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
        'section_6', 'section_7', 'section_8',
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
        article_lists_all = Article.objects.filter(category__slug=slug, add=False)
    else:
        article_lists_all = Article.objects.filter(add=False)

    q_search = request.GET.get('search', False)
    if q_search:
        article_lists_all = article_lists_all.filter(add=False).filter(
            Q(title__contains=q_search) | Q(content__contains=q_search))

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
    contact_frm = ContactForm(request.POST or None)
    if request.method == 'POST':
        obj = contact_frm.save()
        send_mail('Contact Us | ' + obj.name,
                  obj.content,
                  obj.email,
                  [settings.ADMIN_EMAIL, ],
                  fail_silently=True
                  )
        message = "Successfully submitted"

    context = {
        'categories': categories,
        'object': home_page,
        'contact_frm': contact_frm,
    }

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


def add_list(request, slug=''):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    add_lists_all = Add.objects.filter(category__slug__exact=slug).order_by('-featured')
    if slug != '':
        cur_category = AddCategory.objects.filter(slug=slug).first()
    else:
        cur_category = None
    page = request.GET.get('page', 1)
    paginator = Paginator(add_lists_all, 12)
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


def add_create(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    ads_setting = AdsSetting.objects.last()
    array_52 = range(1, 53)
    if request.method == "POST":
        form = NewAddForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            object.words = request.POST.get('words')
            object.price = request.POST.get('price')
            if request.user.is_authenticated:
                object.user = request.user
            object.save()

            return HttpResponseRedirect('/')
    else:
        form = NewAddForm()

    context = {
        'categories': categories,
        'object': home_page,
        'form': form,
        'ads_setting': ads_setting,
        'array_52': array_52,
    }

    return render(request, 'app/add_create.html', context)


def subscribe_email(request):
    if not request.method == 'POST':
        return HttpResponseRedirect('/')
    subscribers = SubscriberEmail.objects.filter(email=request.POST.get('email'))
    if len(subscribers) > 0:
        output = {
            'status': "Already Registered!",
        }
    else:
        frm = SubscribeForm(request.POST)
        if frm.is_valid():
            obj = frm.save()
        output = {
            'status': "Successfullly Registered!",
        }
    return JsonResponse(output)


def payment(request):
    session_id = '12345'
    seller_id = '66809'
    amount = '243'
    crc_key = '8633d0e9f45f18cd'

    crc_hash = "%s|%s|%s|%s" % (
                session_id, seller_id,
                amount, crc_key)

    print(crc_hash)
    m = hashlib.md5()
    m.update(crc_hash.encode())
    crc_code = m.hexdigest()
    print(crc_code)

    context = {
        'session_id': session_id,
        'seller_id': seller_id,
        'amount': amount,
        'crc_code': crc_code,
    }

    return render(request, 'app/payment.html', context)


def full_access(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    context = {
        'categories': categories,
        'object': home_page,
        'article_all': Article.objects.all(),
        'article_lists': FullAccess.objects.all(),
        'cur_category': '',
    }
    return render(request, 'app/full_access.html', context)


@login_required(login_url='/uwierzytelnienie/')
def subscribe(request):
    categories = Category.objects.filter(menu=True)
    home_page = HomePage.objects.filter(date_published__lte=datetime.now()).first()
    id = request.GET.get('id', False)
    user = request.user
    subscription_type = FullAccess.objects.filter(id=id).first()
    subscription = FullAccessSubscription()
    subscription.user = user
    subscription.subscription_type = subscription_type
    subscription.save()

    session_id = 'sub_' + str(subscription.pk)
    price = int(subscription_type.price * 100)

    form_ins = {
        'p24_session_id': session_id,
        'p24_id_sprzedawcy': settings.SELLER_ID,
        'p24_email': user.email,
        'p24_kwota': price,
        'p24_opis': '',
        'p24_klient': user.first_name,
        'p24_adres': user.address,
        'p24_kod': user.zip_code,
        'p24_miasto': user.city,
        'p24_kraj': 'PL',
        'p24_language': 'pl',
        'p24_return_url_ok': 'https://www.tomaszow-tit.pl/prenumeraty/3-miesiace/sign-up',
        'p24_return_url_error': 'https://www.tomaszow-tit.pl/prenumeraty/3-miesiace/sign-up',
        'p24_crc': crc_code(session_id, settings.SELLER_ID, price, settings.CRC_KEY),
    }

    order_form = Przelewy24PrepareForm(form_ins)

    tax_rate = AdsSetting.objects.first().tax_rate
    tax_rule = tax_rate * subscription_type.price
    print(tax_rate)
    print(tax_rule)
    payment_ins = {
        'price': subscription_type.price - tax_rule,
        'tax_rule': tax_rule,
        'total': subscription_type.price,
    }

    context = {
        'categories': categories,
        'object': home_page,
        'order_form': order_form,
        'payment_ins': payment_ins,
    }

    return render(request, 'app/order.html', context)


def crc_code(session_id, seller_id, amount, crc_key):
    crc_hash = "%s|%s|%s|%s" % (
                session_id, seller_id,
                amount, crc_key)

    print(crc_hash)
    m = hashlib.md5()
    m.update(crc_hash.encode())
    crc_code = m.hexdigest()
    print(crc_code)
    return crc_code


def update_user(request):
    user = request.user
    user.surname = request.POST.get('p24_klient')
    user.zip_code = request.POST.get('p24_kod')
    user.address = request.POST.get('p24_adres')
    user.city = request.POST.get('p24_miasto')
    user.save()
    data = {
        'status': True
    }
    return JsonResponse(data)


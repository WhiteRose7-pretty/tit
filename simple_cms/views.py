from django.shortcuts import render
from .forms import NewPostForm, FindArticleForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import HomePage
from django.shortcuts import get_object_or_404



def home(request):
    #query
    query = HomePage.objects.all()

    #form
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            object = HomePage()
            object.name = cd['name']
            object.date_published = cd['date']
            object.save()
            return HttpResponseRedirect(reverse('simple_cms:home'))
    else:
        form = NewPostForm()

    context = {'form': form,
               'query': query}
    return render(request, 'simple_cms/home.html', context)



def edit_page(request, id):
    object = get_object_or_404(HomePage, pk=id)
    if request.method == 'POST':
        form = FindArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            field_name = request.POST.get('field_name')
            #basic section top
            print(field_name)
            if field_name == 'small_article_basic_section_1':
                print(1)
                object.small_article_basic_section_1 = cd['name']
            if field_name == 'small_article_basic_section_2':
                print(2)
                object.small_article_basic_section_2 = cd['name']
            if field_name == 'small_article_basic_section_3':
                object.small_article_basic_section_3 = cd['name']
            if field_name == 'small_article_basic_section_4':
                object.small_article_basic_section_4 = cd['name']
            if field_name == 'small_article_basic_section_5':
                object.small_article_basic_section_5 = cd['name']
            if field_name == 'small_article_basic_section_6':
                object.small_article_basic_section_6 = cd['name']
            if field_name == 'small_article_basic_section_7':
                object.small_article_basic_section_7 = cd['name']
            #basic section center
            elif field_name == 'slider_lg_basic_1':
                object.slider_lg_basic_1 = cd['name']
            elif field_name == 'slider_lg_basic_2':
                object.slider_lg_basic_2 = cd['name']
            elif field_name == 'slider_lg_basic_3':
                object.slider_lg_basic_3 = cd['name']
            elif field_name == 'slider_lg_basic_4':
                object.slider_lg_basic_4 = cd['name']
            elif field_name == 'slider_lg_basic_5':
                object.slider_lg_basic_5 = cd['name']
            elif field_name == 'slider_lg_basic_6':
                object.slider_lg_basic_6 = cd['name']
            elif field_name == 'slider_lg_basic_7':
                object.slider_lg_basic_7 = cd['name']
            elif field_name == 'slider_lg_basic_8':
                object.slider_lg_basic_8 = cd['name']
            elif field_name == 'slider_lg_basic_9':
                object.slider_lg_basic_9 = cd['name']
            #basic section left
            elif field_name == 'slider_sm_basic_1':
                print('Zajebiscie')
                object.slider_sm_basic_1 = cd['name']
            elif field_name == 'slider_sm_basic_2':
                object.slider_sm_basic_2 = cd['name']
            elif field_name == 'slider_sm_basic_3':
                object.slider_sm_basic_3 = cd['name']
            elif field_name == 'slider_sm_basic_4':
                object.slider_sm_basic_4 = cd['name']
            elif field_name == 'slider_sm_basic_5':
                object.slider_sm_basic_5 = cd['name']
            elif field_name == 'slider_sm_basic_6':
                object.slider_sm_basic_6 = cd['name']

            object.save()
            return HttpResponseRedirect(reverse('simple_cms:edit_page', args=[object.id]))
    else:
        form = FindArticleForm()

    context = {'object': object,
               'form': form}
    return render(request, 'simple_cms/edit_page.html', context)
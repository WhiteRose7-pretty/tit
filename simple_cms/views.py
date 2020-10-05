from django.shortcuts import render
from .forms import NewPostForm, FindArticleForm, UploadImageForm, ChangeLabelOnPage
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

    #edit labels
    if request.method == 'POST' and 'submit_section_labels' in request.POST:
        label_form = ChangeLabelOnPage(request.POST)
        if label_form.is_valid():
            cd = label_form.cleaned_data
            object.button_1 = cd['button_1']
            object.button_2 = cd['button_2']
            object.button_3 = cd['button_3']
            object.section_1 = cd['section_1']
            object.section_2 = cd['section_2']
            object.section_3 = cd['section_3']
            object.section_4 = cd['section_4']
            object.section_5 = cd['section_5']
            object.section_6 = cd['section_6']
            object.section_7 = cd['section_7']
            object.section_8 = cd['section_8']
            object.save()
            return HttpResponseRedirect(reverse('simple_cms:edit_page', args=[object.id]))
    else:
        label_form = ChangeLabelOnPage()

    #image edit
    if request.method == 'POST' and 'submit_img' in request.POST:
        form_img = UploadImageForm(request.POST, request.FILES)
        if form_img.is_valid():
            cd = form_img.cleaned_data
            object.img_tomaszow_tit = cd['img']
            object.save()
            return HttpResponseRedirect(reverse('simple_cms:edit_page', args=[object.id]))
    else:
        form_img = UploadImageForm()

    #content edit
    if request.method == 'POST' and 'submit_modal' in request.POST:
        form = FindArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            field_name = request.POST.get('field_name')
            #navbar element
            if field_name == 'navbar_alert_1':
                object.navbar_alert_1 = cd['name']
            if field_name == 'navbar_alert_2':
                object.navbar_alert_2 = cd['name']
            if field_name == 'navbar_alert_3':
                object.navbar_alert_3 = cd['name']
            if field_name == 'navbar_alert_4':
                object.navbar_alert_4 = cd['name']
            if field_name == 'navbar_alert_5':
                object.navbar_alert_5 = cd['name']
            #navbar basic add
            if field_name == 'add_navbar':
                object.add_navbar = cd['name']
            #basic section top
            if field_name == 'small_article_basic_section_1':
                object.small_article_basic_section_1 = cd['name']
            if field_name == 'small_article_basic_section_2':
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
            #section under
            elif field_name == 'section_second_1':
                object.section_second_1 = cd['name']
            elif field_name == 'section_second_2':
                object.section_second_2 = cd['name']
            elif field_name == 'small_section_second_1':
                object.small_section_second_1 = cd['name']
            elif field_name == 'small_section_second_2':
                object.small_section_second_2 = cd['name']
            elif field_name == 'small_section_second_3':
                object.small_section_second_3 = cd['name']
            elif field_name == 'small_section_second_4':
                object.small_section_second_4 = cd['name']
            elif field_name == 'add_navbar_sponsorowane':
                object.add_navbar_sponsorowane = cd['name']
            elif field_name == 'section_second_left_1':
                object.section_second_left_1 = cd['name']
            elif field_name == 'section_second_left_2':
                object.section_second_left_2 = cd['name']
            elif field_name == 'section_second_left_3':
                object.section_second_left_3 = cd['name']
            elif field_name == 'section_second_left_4':
                object.section_second_left_4 = cd['name']
            elif field_name == 'section_second_left_5':
                object.section_second_left_5 = cd['name']
            #basic cneter section
            elif field_name == 'basic_center_1':
                object.basic_center_1 = cd['name']
            elif field_name == 'basic_center_2':
                object.basic_center_2 = cd['name']
            #large basic under
            elif field_name == 'large_basic_under':
                object.large_basic_under = cd['name']
            elif field_name == 'sm_basic_under_1':
                object.sm_basic_under_1 = cd['name']
            elif field_name == 'sm_basic_under_2':
                object.sm_basic_under_2 = cd['name']
            elif field_name == 'sm_basic_under_3':
                object.sm_basic_under_3 = cd['name']
            elif field_name == 'sm_basic_under_4':
                object.sm_basic_under_4 = cd['name']
            elif field_name == 'sm_basic_under_5':
                object.sm_basic_under_5 = cd['name']
            elif field_name == 'sm_basic_under_6':
                object.sm_basic_under_6 = cd['name']
            #footer section
            elif field_name == 'section_footer_1':
                object.section_footer_1 = cd['name']
            elif field_name == 'section_footer_2':
                object.section_footer_2 = cd['name']
            elif field_name == 'section_footer_3':
                object.section_footer_3 = cd['name']
            elif field_name == 'section_footer_4':
                object.section_footer_4 = cd['name']
            elif field_name == 'section_footer_5':
                object.section_footer_5 = cd['name']
            elif field_name == 'section_footer_6':
                object.section_footer_6 = cd['name']
            elif field_name == 'section_footer_7':
                object.section_footer_7 = cd['name']
            elif field_name == 'section_footer_8':
                object.section_footer_8 = cd['name']
            elif field_name == 'section_footer_9':
                object.section_footer_9 = cd['name']
            elif field_name == 'section_footer_10':
                object.section_footer_10 = cd['name']
            elif field_name == 'section_footer_11':
                object.section_footer_11 = cd['name']
            elif field_name == 'section_footer_12':
                object.section_footer_12 = cd['name']


            object.save()
            return HttpResponseRedirect(reverse('simple_cms:edit_page', args=[object.id]))
    else:
        form = FindArticleForm()

    context = {'object': object,
               'form': form,
               'label_form': label_form,
               'form_img': form_img}
    return render(request, 'simple_cms/edit_page.html', context)
from django.db import models
from django.utils.text import slugify
from app.models import Article, Add
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


class HomePage(models.Model):
    #basic
    name = models.CharField(max_length=50, verbose_name='Nazwa strony')
    date_published = models.DateTimeField()
    #navbar
    navbar_alert_1 = models.ForeignKey(Article, related_name='navbar_alert_1', on_delete=models.CASCADE, blank=True, null=True)
    navbar_alert_2 = models.ForeignKey(Article, related_name='navbar_alert_2', on_delete=models.CASCADE, blank=True, null=True)
    navbar_alert_3 = models.ForeignKey(Article, related_name='navbar_alert_3', on_delete=models.CASCADE, blank=True, null=True)
    navbar_alert_4 = models.ForeignKey(Article, related_name='navbar_alert_4', on_delete=models.CASCADE, blank=True, null=True)
    navbar_alert_5 = models.ForeignKey(Article, related_name='navbar_alert_5', on_delete=models.CASCADE, blank=True, null=True)
    add_navbar = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)
    add_navbar_sponsorowane = models.ForeignKey(Article,
                                                related_name='add_navbar_sponsorowane',
                                                on_delete=models.CASCADE,
                                                blank=True, null=True)
    img_tomaszow_tit = ProcessedImageField(upload_to='profile-pictures',
                                           blank=True, null=True,
                                           processors=[ResizeToFill(360, 255)],
                                           format='JPEG',
                                           options={'quality': 100},
                                           verbose_name='Zdjęcie aktualnego wydania')
    #section 1
    small_article_basic_section_1 = models.ForeignKey(Article, related_name='small_article_basic_section_1', on_delete=models.CASCADE, blank=True, null=True)
    small_article_basic_section_2 = models.ForeignKey(Article, related_name='small_article_basic_section_2', on_delete=models.CASCADE, blank=True, null=True)
    small_article_basic_section_3 = models.ForeignKey(Article, related_name='small_article_basic_section_3', on_delete=models.CASCADE, blank=True, null=True)
    small_article_basic_section_4 = models.ForeignKey(Article, related_name='small_article_basic_section_4', on_delete=models.CASCADE, blank=True, null=True)
    small_article_basic_section_5 = models.ForeignKey(Article, related_name='small_article_basic_section_5', on_delete=models.CASCADE, blank=True, null=True)
    small_article_basic_section_6 = models.ForeignKey(Article, related_name='small_article_basic_section_6', on_delete=models.CASCADE, blank=True, null=True)
    small_article_basic_section_7 = models.ForeignKey(Article, related_name='small_article_basic_section_7', on_delete=models.CASCADE, blank=True, null=True)
    #slider name
    slider_sm_basic_1 = models.ForeignKey(Article, related_name='slider_sm_basic_1', on_delete=models.CASCADE, blank=True, null=True)
    slider_sm_basic_2 = models.ForeignKey(Article, related_name='slider_sm_basic_2', on_delete=models.CASCADE, blank=True, null=True)
    slider_sm_basic_3 = models.ForeignKey(Article, related_name='slider_sm_basic_3', on_delete=models.CASCADE, blank=True, null=True)
    slider_sm_basic_4 = models.ForeignKey(Article, related_name='slider_sm_basic_4', on_delete=models.CASCADE, blank=True, null=True)
    slider_sm_basic_5 = models.ForeignKey(Article, related_name='slider_sm_basic_5', on_delete=models.CASCADE, blank=True, null=True)
    slider_sm_basic_6 = models.ForeignKey(Article, related_name='slider_sm_basic_6', on_delete=models.CASCADE, blank=True, null=True)
    #slider_large
    slider_lg_basic_1 = models.ForeignKey(Article, related_name='slider_lg_basic_1', on_delete=models.CASCADE, blank=True, null=True)
    slider_lg_basic_2 = models.ForeignKey(Article, related_name='slider_lg_basic_2', on_delete=models.CASCADE, blank=True, null=True)
    slider_lg_basic_3 = models.ForeignKey(Article, related_name='slider_lg_basic_3', on_delete=models.CASCADE, blank=True, null=True)
    slider_lg_basic_4 = models.ForeignKey(Article, related_name='slider_lg_basic_4', on_delete=models.CASCADE, blank=True, null=True)
    slider_lg_basic_5 = models.ForeignKey(Article, related_name='slider_lg_basic_5', on_delete=models.CASCADE, blank=True, null=True)
    slider_lg_basic_6 = models.ForeignKey(Article, related_name='slider_lg_basic_6', on_delete=models.CASCADE, blank=True, null=True)
    slider_lg_basic_7 = models.ForeignKey(Article, related_name='slider_lg_basic_7', on_delete=models.CASCADE, blank=True, null=True)
    slider_lg_basic_8 = models.ForeignKey(Article, related_name='slider_lg_basic_8', on_delete=models.CASCADE, blank=True, null=True)
    slider_lg_basic_9 = models.ForeignKey(Article, related_name='slider_lg_basic_9', on_delete=models.CASCADE, blank=True, null=True)
    #basic img
    section_second_1 = models.ForeignKey(Article, related_name='section_second_1', on_delete=models.CASCADE, blank=True, null=True)
    section_second_2 =  models.ForeignKey(Article, related_name='section_second_2', on_delete=models.CASCADE, blank=True, null=True)
    small_section_second_1 = models.ForeignKey(Article, related_name='small_section_second_1', on_delete=models.CASCADE, blank=True, null=True)
    small_section_second_2 = models.ForeignKey(Article, related_name='small_section_second_2', on_delete=models.CASCADE, blank=True, null=True)
    small_section_second_3 = models.ForeignKey(Article, related_name='small_section_second_3', on_delete=models.CASCADE, blank=True, null=True)
    small_section_second_4 = models.ForeignKey(Article, related_name='small_section_second_4', on_delete=models.CASCADE, blank=True, null=True)
    #section second left
    section_second_left_1 = models.ForeignKey(Article, related_name='section_second_left_1', on_delete=models.CASCADE, blank=True, null=True)
    section_second_left_2 = models.ForeignKey(Article, related_name='section_second_left_2', on_delete=models.CASCADE, blank=True, null=True)
    section_second_left_3 = models.ForeignKey(Article, related_name='section_second_left_3', on_delete=models.CASCADE, blank=True, null=True)
    section_second_left_4 = models.ForeignKey(Article, related_name='section_second_left_4', on_delete=models.CASCADE, blank=True, null=True)
    section_second_left_5 = models.ForeignKey(Article, related_name='section_second_left_5', on_delete=models.CASCADE, blank=True, null=True)
    #center site
    basic_center_1 = models.ForeignKey(Article, related_name='basic_center_1', on_delete=models.CASCADE, blank=True, null=True)
    basic_center_2 = models.ForeignKey(Article, related_name='basic_center_2', on_delete=models.CASCADE, blank=True, null=True)
    #basic center under
    large_basic_under = models.ForeignKey(Article, related_name='large_basic_under', on_delete=models.CASCADE, blank=True, null=True)
    sm_basic_under_1 = models.ForeignKey(Article, related_name='sm_basic_under_1', on_delete=models.CASCADE, blank=True, null=True)
    sm_basic_under_2 = models.ForeignKey(Article, related_name='sm_basic_under_2', on_delete=models.CASCADE, blank=True, null=True)
    sm_basic_under_3 = models.ForeignKey(Article, related_name='sm_basic_under_3', on_delete=models.CASCADE, blank=True, null=True)
    sm_basic_under_4 = models.ForeignKey(Article, related_name='sm_basic_under_4', on_delete=models.CASCADE, blank=True, null=True)
    sm_basic_under_5 = models.ForeignKey(Article, related_name='sm_basic_under_5', on_delete=models.CASCADE, blank=True, null=True)
    #footer section
    section_footer_1 = models.ForeignKey(Article, related_name='section_footer_1', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_2 = models.ForeignKey(Article, related_name='section_footer_2', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_3 = models.ForeignKey(Article, related_name='section_footer_3', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_4 = models.ForeignKey(Article, related_name='section_footer_4', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_5 = models.ForeignKey(Article, related_name='section_footer_5', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_6 = models.ForeignKey(Article, related_name='section_footer_6', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_7 = models.ForeignKey(Article, related_name='section_footer_7', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_8 = models.ForeignKey(Article, related_name='section_footer_8', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_9 = models.ForeignKey(Article, related_name='section_footer_9', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_10 = models.ForeignKey(Article, related_name='section_footer_10', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_11 = models.ForeignKey(Article, related_name='section_footer_11', on_delete=models.CASCADE, blank=True, null=True)
    section_footer_12 = models.ForeignKey(Article, related_name='section_footer_12', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_published']


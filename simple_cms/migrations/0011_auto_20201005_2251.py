# Generated by Django 2.2.4 on 2020-10-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_cms', '0010_homepage_add_navbar_sponsorowane'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='button_1',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_2',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name='homepage',
            name='button_3',
            field=models.CharField(blank=True, max_length=11),
        ),
        migrations.AddField(
            model_name='homepage',
            name='center_section_1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='center_section_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='center_section_3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='footer_section_1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='footer_section_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='footer_section_3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_first_1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_first_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_first_3',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

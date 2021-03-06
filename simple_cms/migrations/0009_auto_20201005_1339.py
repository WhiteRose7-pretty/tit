# Generated by Django 2.2.4 on 2020-10-05 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simple_cms', '0008_auto_20201005_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='basic_center_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basic_center_2', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_footer_10',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_footer_10', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_footer_12',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_footer_12', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_footer_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_footer_2', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_footer_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_footer_4', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_footer_7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_footer_7', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_second_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_second_2', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_second_left_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_second_left_1', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='section_second_left_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section_second_left_5', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sm_basic_under_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sm_basic_under_1', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='sm_basic_under_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sm_basic_under_5', to='app.Article'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='small_section_second_4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='small_section_second_4', to='app.Article'),
        ),
    ]

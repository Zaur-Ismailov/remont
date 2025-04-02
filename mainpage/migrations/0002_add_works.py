from __future__ import unicode_literals

from django.db import migrations


def forwards_func(apps, schema_editor):
    Work = apps.get_model("mainpage", "Work")

    works_to_insert = [
        Work(name='Грунтовка стен', cost_per_sqm=100, time_per_sqm=0.25),
        Work(name='Покраска стен', cost_per_sqm=500, time_per_sqm=0.5),
        Work(name='Укладка плитки', cost_per_sqm=1200, time_per_sqm=1.2),
        Work(name='Установка натяжного потолка', cost_per_sqm=800, time_per_sqm=0.8),
        Work(name='Укладка ламината', cost_per_sqm=400, time_per_sqm=1.0),
        Work(name='Укладка керамогранита', cost_per_sqm=800, time_per_sqm=1.4),
    ]

    Work.objects.bulk_create(works_to_insert)


def reverse_func(apps, schema_editor):
    Work = apps.get_model("mainpage", "Work")

    work_names_to_delete = [
        'Грунтовка стен',
        'Покраска стен',
        'Укладка плитки',
        'Установка натяжного потолка',
        'Укладка ламината',
        'Укладка керамогранита',
    ]

    Work.objects.filter(name__in=work_names_to_delete).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial')
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]

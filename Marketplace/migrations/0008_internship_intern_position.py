# Generated by Django 2.0.1 on 2018-08-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0007_remove_article_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='intern_position',
            field=models.CharField(default='', max_length=150),
        ),
    ]

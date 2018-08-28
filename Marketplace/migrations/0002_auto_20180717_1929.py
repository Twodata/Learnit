# Generated by Django 2.0.1 on 2018-07-17 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True, default='http://learnit.com', null=True)),
                ('skillset', models.CharField(blank=True, max_length=500, null=True)),
                ('quote', models.CharField(max_length=250)),
                ('picture', models.ImageField(blank=True, default='profile_picture', null=True, upload_to='profile_picture')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='market',
            name='website',
            field=models.URLField(blank=True, default='http://learnit.com', null=True),
        ),
    ]

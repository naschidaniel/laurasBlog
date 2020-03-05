# Generated by Django 3.0.2 on 2020-03-04 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=200)),
                ('datePosted', models.DateTimeField(default=django.utils.timezone.now)),
                ('mainImage', models.ImageField(upload_to='')),
                ('mainImageAlt', models.CharField(blank=True, max_length=100)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogCategory')),
            ],
            options={
                'ordering': ['-datePosted'],
            },
        ),
    ]

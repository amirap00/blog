# Generated by Django 4.0 on 2022-03-26 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0009_alter_article_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='pub_date',
        ),
    ]

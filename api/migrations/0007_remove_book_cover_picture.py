# Generated by Django 4.1.5 on 2023-02-11 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_book_category_alter_book_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_picture',
        ),
    ]

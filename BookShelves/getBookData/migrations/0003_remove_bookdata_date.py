# Generated by Django 4.1.4 on 2024-04-01 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getBookData', '0002_alter_bookdata_author_alter_bookdata_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdata',
            name='date',
        ),
    ]

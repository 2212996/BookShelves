# Generated by Django 4.1.4 on 2024-03-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'bookdata',
                'db_table': 'bookdata',
            },
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title_body',
            field=models.TextField(max_length=500),
        ),
    ]

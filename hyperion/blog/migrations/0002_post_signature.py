# Generated by Django 4.2.4 on 2023-08-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='signature',
            field=models.CharField(default='Charity is awesome', max_length=140),
        ),
    ]

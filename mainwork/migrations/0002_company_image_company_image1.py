# Generated by Django 4.0.2 on 2022-03-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwork', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(default='slide-2', upload_to='kuyik'),
        ),
        migrations.AddField(
            model_name='company',
            name='image1',
            field=models.ImageField(default='slide-2', upload_to='kuyik'),
        ),
    ]

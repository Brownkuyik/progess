# Generated by Django 4.0.2 on 2022-03-08 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwork', '0005_rename_about_aboutdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='why',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='why us')),
                ('defe', models.CharField(help_text='small talk', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='whypoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('point', models.TextField()),
            ],
        ),
    ]
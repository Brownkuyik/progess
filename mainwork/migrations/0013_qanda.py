# Generated by Django 4.0.2 on 2022-03-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwork', '0012_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='QandA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quest', models.TextField(help_text='Ask questions')),
                ('ans', models.TextField(help_text='What are the answers')),
            ],
        ),
    ]

# Generated by Django 4.0.2 on 2022-03-08 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainwork', '0011_alter_testimonial_office_alter_testimonial_who'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('who', models.CharField(help_text='Name of the person', max_length=300)),
                ('office', models.CharField(help_text='Office occupied by him', max_length=200)),
                ('image', models.ImageField(upload_to='teams')),
            ],
        ),
    ]
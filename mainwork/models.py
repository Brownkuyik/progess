from django.db import models

# Create your models here.

class company(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    number1 = models.IntegerField()
    email = models.EmailField()
    email1 = models.EmailField()
    address = models.CharField(max_length=200, help_text='company location')
    cont = models.CharField(max_length=50, default='CONTACT')
    hm = models.CharField(max_length=50, default='HOME')
    ab = models.CharField(max_length=50, default='ABOUT')
    ser = models.CharField(max_length=50, default='SERVICES')
    tes = models.CharField(max_length=50, default='TESTIMONIALS')
    te = models.CharField(max_length=50, default='OUR TEAM')
    pr = models.CharField(max_length=50, default='OUR COMPETING PRICES')
    image = models.ImageField(upload_to='kuyik', default='slide-2')
    image1 = models.ImageField(upload_to='kuyik', default='slide-2')


    def __str__(self):
        return f'{self.name} located at {self.address}'

    class Meta:
        verbose_name_plural = "Company"



class slight(models.Model):
    head = models.CharField(max_length=150, help_text='what is the company about')
    text = models.TextField(help_text='explain in short')
    image = models.ImageField(upload_to='slight')

class AboutDetails(models.Model):
    desc = models.CharField(max_length=300, help_text='what is the company about')
    fact = models.TextField()
    fact1 = models.TextField()
    fact2 = models.TextField()
    how = models.TextField(help_text='who and who founded the firm')

class whyus(models.Model):
    text = models.TextField(help_text='why us')
    defe = models.CharField(max_length=200, help_text='small talk')


class whypoint(models.Model):
    number=models.IntegerField()
    head = models.CharField(max_length=100, help_text='what', default='efficiency')
    point= models.TextField()


class serviceDetail(models.Model):
    what= models.CharField(max_length=80, help_text='what they offer')
    how = models.TextField(help_text='description of what they do.')

class testimonial(models.Model):
    who = models.CharField(max_length=100, help_text='who made the comment')
    office = models.CharField(max_length=100, help_text='what office is he')
    image = models.ImageField(upload_to='testimony')
    what = models.TextField(help_text='what did he say about the company')

    def __str__(self):
        return f'{self.who} which is the {self.office} made this comment about us here.'

class team(models.Model):
    who = models.CharField(max_length=300, help_text='Name of the person')
    office = models.CharField(max_length=200, help_text='Office occupied by him')
    image = models.ImageField(upload_to='teams')

    def __str__(self):
        return f'{self.who} which is the {self.office} is one of us.'


class QandA(models.Model):
    quest = models.TextField(help_text='Ask questions')
    ans = models.TextField(help_text='What are the answers')


class comment(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200, default='your thought')
    phone = models.IntegerField()
    email = models.EmailField()
    text = models.TextField(max_length=10000,)
    im = models.ImageField(upload_to='comment')

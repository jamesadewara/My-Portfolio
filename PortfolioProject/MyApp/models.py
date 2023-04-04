from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth import get_user, user_logged_in
from . import utility

def testimony_img_path(instance, filename):
    return f"img/testimonials/{instance.person}.png"

def profile_img_path(instance, filename):
    return f"img/profile_1.png"

def logo_img_path(instance, filename):
    return f"img/logo.png"

# Create your models here.

################## HOME MODEL #####################
class Home(models.Model):
    name = models.CharField(max_length = 150)
    picture = models.ImageField(upload_to = profile_img_path)
    details = models.CharField(max_length = 300)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"{self.name}"
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.picture.url))
################## END MODEL #####################

################## ABOUT MODEL #####################
class MySkill(models.Model):
    specialization = models.CharField(max_length = 300)
    grade = models.IntegerField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"{self.specialization}"

class Fact(models.Model):
    icon = models.SlugField()
    counter_end = models.IntegerField(default = 234)
    title = models.CharField(max_length = 150)
    text = models.CharField(max_length = 350)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"{self.title}"

class About(models.Model):
    picture = models.ImageField(upload_to = "img/")
    detail = models.TextField()
    title = models.CharField(max_length = 300)
    birthday = models.DateField()
    website = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    city = models.CharField(max_length = 150)
    age = models.IntegerField()
    degree = models.SlugField()
    email = models.EmailField()
    freelance = models.SlugField()
    details = models.TextField()
    about_my_skill = models.TextField()
    skills = models.ManyToManyField(MySkill, related_name="myskills")
    facts_about_me = models.TextField()
    facts = models.ManyToManyField(Fact, related_name="myfacts")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"About"
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.picture.url))
################## END MODEL #####################

################## RESUME MODEL ####################
class ResumeList(models.Model):
    text = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"{self.text}"
 
class ResumeDetail(models.Model):
    title = models.CharField(max_length = 250)
    name = models.CharField(max_length = 250, null = True, blank = True)
    description = models.TextField()
    duration = models.CharField(max_length = 25, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    list = models.ManyToManyField(ResumeList, )
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"Resume Details"

class ResumeArea(models.Model):
    title = models.CharField(max_length = 150)
    detail = models.ManyToManyField(ResumeDetail, )
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"Resume Area"

class Resume(models.Model):
    about = models.TextField()
    area = models.ManyToManyField(ResumeArea)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"Resume"
################## END MODEL #####################
 
################# PORTFOLIO MODEL ##################
class MyPortfolio(models.Model):
    portfolio_group = models.ForeignKey("PortfolioGroup", on_delete = models.CASCADE)
    name = models.CharField(max_length = 300)
    image = models.ImageField(upload_to = "img/portfolio/")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"Portfolio"
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="80" />' % (self.image.url))

class PortfolioGroup(models.Model):
    title = models.SlugField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"{self.title}"
################## END MODEL #####################

################## SERVICE MODEL ###################
class MyService(models.Model):
    title = models.CharField(max_length = 150)
    icon = models.SlugField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"{self.title}"
     
class Service(models.Model):
    about = models.TextField()
    my_service = models.ManyToManyField(MyService, related_name = "myservice")
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"Services"
################## END MODEL #####################

################## TESTIMONY MODEL #################
class Testimonial(models.Model):
    comment = models.TextField()
    person = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = testimony_img_path)
    profession = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"Testimonials"
################## END MODEL #####################

################## CONTACT MODEL ##################
class SocialLink(models.Model):
    icon = models.SlugField()
    link = models.CharField(max_length = 300)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"{self.link}"

class Contact(models.Model):
    location = models.CharField(max_length = 100)
    email = models.EmailField()
    call = models.CharField(max_length = 100)
    map_code = models.TextField(null = True, blank = True)
    social_links = models.ManyToManyField(SocialLink,)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"Contact"
################## END MODEL #####################
 
################## SETTINGS MODEL ################
class Setting(models.Model):
    title = models.CharField(max_length = 50)
    logo = models.ImageField(upload_to = logo_img_path)
    copyrights = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"Settings"
################## END MODEL #####################

from django.contrib import admin
from . import models

# Register your models here.
#           Home
class HomeAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Home
    def has_add_permission(self, request):
        try:
            if models.Home.objects.all().count() > 0:
                return False
            else:
                return True
        except:
            return True
        
    def has_delete_permission(self, request,*args, **kwargs):
        return False, models.Home.objects.all()
    
admin.site.register(models.Home, HomeAdmin)
#           About
class AboutAdmin(admin.ModelAdmin):
    class Meta:
        model = models.About
    def has_add_permission(self, request):
        try:
            if models.About.objects.all().count() > 0:
                return False
            else:
                return True
        except:
            return True
        
    def has_delete_permission(self, request,*args, **kwargs):
        return False, models.About.objects.all()
    
admin.site.register(models.About, AboutAdmin)
# about dependecies
admin.site.register([
    models.MySkill,
    models.Fact
    ])

#          Resume
class ResumeAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Resume
    def has_add_permission(self, request):
        try:
            if models.Resume.objects.all().count() > 0:
                return False
            else:
                return True
        except:
            return True
        
    def has_delete_permission(self, request,*args, **kwargs):
        return False, models.Resume.objects.all()
    
admin.site.register(models.Resume, ResumeAdmin)
# resume dependecies
admin.site.register([
    models.ResumeList,
    models.ResumeArea,
    models.ResumeDetail
])


#          Portfolio
admin.site.register([
    models.MyPortfolio,
    models.PortfolioGroup
    ])

#          Service
class ServiceAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Service
    def has_add_permission(self, request):
        try:
            if models.Service.objects.all().count() > 0:
                return False
            else:
                return True
        except:
            return True
        
    def has_delete_permission(self, request,*args, **kwargs):
        return False, models.Service.objects.all()
    
admin.site.register(models.Service, ServiceAdmin)
# portfolio dependecy
admin.site.register(models.MyService)

#          Contact
class ContactAdmin(admin.ModelAdmin):
    list_filter = ["location",  "call", "email"]
    list_display = ["location",  "call", "email"]
    search_fields = []
    
    
    class Meta:
        model = models.Contact
    def has_add_permission(self, request):
        try:
            if models.Contact.objects.all().count() > 0:
                return False
            else:
                return True
        except:
            return True
    
admin.site.register(models.Contact, ContactAdmin)
# contact dependecy
admin.site.register(models.SocialLink)

#         Testimonials
class TestimonialAdmin(admin.ModelAdmin):
    list_filter = ["comment",  "person", "profession"]
    list_display = ["comment",  "person", "profession"]
    search_fields = ["person"]
    
    class Meta:
        model = models.Testimonial
    
admin.site.register(models.Testimonial, TestimonialAdmin)

#         Settings
class SettingAdmin(admin.ModelAdmin):
    class Meta:
        model = models.Setting
    def has_add_permission(self, request):
        try:
            if models.Setting.objects.all().count() > 0:
                return False
            else:
                return True
        except:
            return True
        
    def has_delete_permission(self, request,*args, **kwargs):
        return False, models.Setting.objects.all()
    
admin.site.register(models.Setting, SettingAdmin)

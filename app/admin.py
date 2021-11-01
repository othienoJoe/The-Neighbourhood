from django.contrib import admin
from app.models import BlogPost, Business, Health, Profile, Update, healthservices, neighborhood

# Register your models here.
admin.site.register(Profile);
admin.site.register(neighborhood);
admin.site.register(BlogPost);
admin.site.register(Business);
admin.site.register(Health);
admin.site.register(healthservices);
admin.site.register(Update);
from django.contrib import admin
from blog.models import * 
# Register your models here.
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Tag)

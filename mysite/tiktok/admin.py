from django.contrib import admin
from .models import Video, Comment, Heart

# Register your models here.
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Heart)

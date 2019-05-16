from django.contrib import admin
from .models import Movie,Comment,Score
# Register your models here.

admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(Score)
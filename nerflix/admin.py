# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from nerflix.models import Movie, Category

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','anio','sort_order','id')
    list_filter = ('anio',)
    list_search = ('name','anio')

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie,MovieAdmin)
admin.site.register(Category,CategoryAdmin)
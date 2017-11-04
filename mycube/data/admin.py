# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Users
from .models import Ratings
from .models import Competitions
from .models import Calendar

admin.site.register(Users)
admin.site.register(Ratings)
admin.site.register(Competitions)
admin.site.register(Calendar)

# Register your models here.

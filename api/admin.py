from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)

admin.site.register(Issue)
admin.site.register(Return)
admin.site.register(Renewal)
from django.contrib import admin
from tutorial.quickstart.models import Dag, Tweet, Follow

# Register your models here.
admin.site.register(Dag)
admin.site.register(Tweet)
admin.site.register(Follow)

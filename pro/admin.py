from django.contrib import admin
from .models import Team,Team_mem,Task

# Register your models here.
admin.site.register(Team)
admin.site.register(Team_mem)
admin.site.register(Task)

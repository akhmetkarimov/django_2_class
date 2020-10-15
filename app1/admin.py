from django.contrib import admin
from app1.models import MyModel

# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'speed', 'model', 'tags')
    list_filter = ('model', )
    search_fields = ('color', 'speed', 'model', 'tags')

admin.site.register(MyModel, MyModelAdmin)

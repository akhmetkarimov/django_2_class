from django.contrib import admin
from app1.models import MyModel, Account, CarType, Genre, Movie

# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'speed', 'model', 'tags', 'car_type')
    list_filter = ('model', )
    search_fields = ('color', 'speed', 'model', 'tags')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_username', 'account_followers', 'account_following')
    search_fields = ('account_username', 'account_description')


class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('genres', )

admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(CarType)
admin.site.register(Genre)
admin.site.register(Movie, MovieAdmin)

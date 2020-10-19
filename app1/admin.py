from django.contrib import admin
from app1.models import MyModel, Account

# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'speed', 'model', 'tags')
    list_filter = ('model', )
    search_fields = ('color', 'speed', 'model', 'tags')

class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_username', 'account_followers', 'account_following')
    search_fields = ('account_username', 'account_description')

admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Account, AccountAdmin)

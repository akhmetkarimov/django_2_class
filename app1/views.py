from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from app1 import models
from app1 import forms
# Create your views here.
class Test:

    def first_page(self):

        # models.MyModel.objects.all() SELECT * FROM tabel_name
        # models.MyModel.objects.filter(color = 123, speed = 123) SELECT * FROM table_name WHERE color = '123' AND speed = '123'

        cars = models.MyModel.objects.all()

        print(dir(models.MyModel.objects.filter()))

        for car in cars:
            car.tags = car.tags.split(',')

        data = {
            "title": "Hello title from view",
            "name": "Yedil A",
            "address":{
                "sub_address": "Sub Address"
            },
            "languages": ["ru", "kz", "en", 'uk', 'kg'],
            "form": forms.MyForm,
            "cars": cars
        }

        # name, surname, skills[array], education[array], socail_networds[array], hashtags[array] 

        return render(self, 'index.html', data)

    def second_page(self):
        return render(self, 'second.html')

    def save_my_model(self):
        if self.method == 'POST':
            color = self.POST.get('color')
            speed = self.POST.get('speed')
            model = self.POST.get('model')
            tags = self.POST.get('tags')
            models.MyModel(color=color, speed=speed, model=model, tags=tags).save()
            return redirect('/')

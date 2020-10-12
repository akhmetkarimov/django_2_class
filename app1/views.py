from django.shortcuts import render
from django.http.response import HttpResponse
from app1 import models

# Create your views here.
class Test:

    def first_page(self):

        data = {
            "title": "Hello title from view",
            "name": "Yedil A",
            "address":{
                "sub_address": "Sub Address"
            },
            "language": ["ru", "kz", "en"]
        }

        # name, surname, skills[array], education[array], socail_networds[array], hashtags[array] 

        return render(self, 'index.html', data)

    def second_page(self):
        return render(self, 'second.html')
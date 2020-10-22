from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from app1 import models
from app1 import forms
import requests
# Create your views here.
class Test:

    def first_page(self):

        # models.MyModel.objects.all() SELECT * FROM tabel_name
        # models.MyModel.objects.filter(color = 123, speed = 123) SELECT * FROM table_name WHERE color = '123' AND speed = '123'
        # models.MyModel.objects.select_related('car_type') INNER JOIN
        # 

        cars = models.MyModel.objects.all()

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

    def update_my_model(self):
        if self.method == 'POST':
            pk = self.POST.get('pk')
            color = self.POST.get('color')
            speed = self.POST.get('speed')
            model = self.POST.get('model')
            tags = self.POST.get('tags')

            # models.MyModel.objects.filter(pk=pk).update(color=color, speed=speed, model=model, tags=tags)

            car = models.MyModel.objects.get(pk=pk)
            car.color = color
            car.speed = speed
            car.model = model
            car.tags = tags

            car.save()

            return redirect('/')

    def delete_my_model(self, pk):
        models.MyModel.objects.get(pk=pk).delete()
        return redirect('/')

    def edit_my_model(self, pk):
        car = models.MyModel.objects.get(pk=pk)
        
        data = {
            "car": car
        }

        return render(self, 'second.html', data)


def myparser(request, inst_account):
    instagram_account = requests.get('https://www.instagram.com/'+inst_account+'/?__a=1').json()
    description = instagram_account['graphql']['user']['biography']
    account = instagram_account['graphql']['user']['username']
    followers = instagram_account['graphql']['user']['edge_followed_by']['count']
    following = instagram_account['graphql']['user']['edge_follow']['count']
    posts = instagram_account['graphql']['user']['edge_owner_to_timeline_media']['count']

    output = "<h1>"+account+"</h1> <p>"+description+"</p> <ul><li> Followers: "+str(followers)+"</li><li> Following: "+str(following)+"</li><li> Posts: "+str(posts)+"</li></ul>"
    
    models.Account(account_username=account, account_description=description, account_followers=followers, account_following=following, account_posts=posts).save()
    
    return output


def enter_account(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        out = myparser(request, account)
        return HttpResponse(out)

def getMovies(request):
    movies = models.Movie.objects.prefetch_related('genres')

    models.Movie.objects.get()

    data = {
        "movies": movies,
    }

    return render(request,'movies.html', data)
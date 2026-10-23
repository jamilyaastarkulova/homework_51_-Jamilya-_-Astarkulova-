from django.shortcuts import render, redirect
from random import choice
nums = [1, 2, 3]


class Cat:
    def __init__(self, name=None, age=1, fullness=40, happiness=40, status='free'):
        self.name = name
        self.age = age
        self.fullness = fullness
        self.happiness = happiness
        self.status = status

cat = Cat()

def info_view(request):
    global cat
    if request.method == 'POST':
        cat_image = '/static/img/happy_cat.png'
        if 0 <= cat.happiness < 30:
            cat_image = '/static/img/angry_cat.jpg'
        elif 30 < cat.happiness < 60:
            cat_image = '/static/img/sad_cat.jpg'
        else:
            cat_image = '/static/img/happy_cat.png'

        if cat.fullness > 100:
            cat_image = '/static/img/sad_cat.jpg'
            cat.happiness -= 30

        action = request.POST.get('action')
        if action == 'play':
            num = choice(nums)
            cat.fullness -= 10
            if num == 1:
                cat.happiness = 0
            else:
                if cat.status == 'free':
                    cat.happiness += 15
                else:
                    cat.happiness -= 5

        elif action == 'feed':
            cat.fullness += 15
            cat.happiness += 5
        elif action == 'sleep':
            if cat.status == 'free':
                cat.status = 'busy'
            else:
                cat.status = 'free'

        if cat.fullness < 0:
            cat.fullness = 0
        if cat.happiness < 0:
            cat.happiness = 0

    context = {
            'name': cat.name,
            'age': cat.age,
            'fullness': cat.fullness,
            'happiness': cat.happiness
        }

    return render(request, 'info.html', context)
    #return render(request, 'info.html', {'name': name})

def main_view(request):
    global cat
    name_cat = request.GET.get('name')
    if name_cat:
        cat.name = name_cat

        return redirect('info')

    return render(request, 'main.html')
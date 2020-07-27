from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html')

def error(requests):
    return render(requests, '404.html')

def blank(requests):
    return render(requests, 'blank.html')

def buttons(requests):
    return render(requests, 'buttons.html')

def cards(requests):
    return render(requests, 'cards.html')

def charts(requests):
    return render(requests, 'charts.html')

def password(requests):
    return render(requests, 'forgot-password.html')

def login(requests):
    return render(requests, 'login.html')

def register(requests):
    return render(requests, 'register.html')

def tables(requests):
    return render(requests, 'tables.html')

def animation(requests):
    return render(requests, 'utilities-animation.html')

def border(requests):
    return render(requests, 'utilities-border.html')

def color(requests):
    return render(requests, 'utilities-color.html')

def other(requests):
    return render(requests, 'utilities-other.html')

def mypage(requests):
    return render(requests, 'mypage.html')

def notice(requests):
    return render(requests, 'notice.html')

def suggest_vote(requests):
    return render(requests, 'suggest_vote.html')

def suggest_other(requests):
    return render(requests, 'suggest_other.html')

def main(requests):
    return render(requests, 'main.html')
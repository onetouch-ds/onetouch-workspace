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

# 투표 페이지
def participate(requests):
    return render(requests, 'participating-vote.html')

# 마이 페이지
def mypage(requests):
    return render(requests, 'mypage.html')

# 공지사항
def notice(requests):
    return render(requests, 'notice.html')

# 투표에 관한 건의사항
def suggest_vote(requests):
    return render(requests, 'suggest_vote.html')

# 기타 건의사항
def suggest_other(requests):
    return render(requests, 'suggest_other.html')

# 메인 페이지
def main(requests):
    return render(requests, 'main.html')
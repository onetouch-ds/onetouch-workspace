from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math

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

# 마이 페이지
def mypage(requests):
    return render(requests, 'mypage.html')

# 공지사항
def notice(requests):
    table_list = Notice.objects.all()
    page = requests.GET.get('page', 1)

    paginator = Paginator(table_list, 10) # 한 페이지에 10 개씩 데이터를 보이게 해 줌
    try:
        tables = paginator.page(page)
    except PageNotAnInteger:
        tables = paginator.page(1)
    except EmptyPage:
        tables = paginator.page(paginator.num_pages)

    page_numbers_range = 5

    pageGroup = math.ceil(int(page) / page_numbers_range)
    start_block = (pageGroup - 1) * page_numbers_range
    end_block = start_block + page_numbers_range

    paginator_range = paginator.page_range[start_block:end_block]

    context = {
        'tables' : tables,
        'paginator_range' : paginator_range,
    }

    return render(requests, 'notice.html', context)

# 투표에 관한 건의사항
def suggest_vote(requests):
    suggest_vote_list = SuggestVote.objects.all()
    paginator = Paginator(suggest_vote_list, 10) # 한 페이지에 10 개씩 데이터를 보이게 해 줌
    page = requests.GET.get('page', 1)
    try:
        suggest_votes = paginator.page(page)
    except PageNotAnInteger:
        suggest_votes = paginator.page(1)
    except EmptyPage:
        suggest_votes = paginator.page(paginator.num_pages)

    page_numbers_range = 5

    pageGroup = math.ceil(int(page) / page_numbers_range)
    start_block = (pageGroup - 1) * page_numbers_range
    end_block = start_block + page_numbers_range

    # max_index = len(paginator.page_range)
    # current_page = int(page) if page else 1
    # start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
    # end_index = start_index + page_numbers_range

    # if end_index >= max_index:
    #     end_index = max_index

#    paginator_range = paginator.page_range[start_index:end_index]
    paginator_range = paginator.page_range[start_block:end_block]

    context = {
        'suggest_votes' : suggest_votes,
        'paginator_range' : paginator_range,
    }

    return render(requests, 'suggest_vote.html', context)

# 기타 건의사항
def suggest_other(requests):
    suggest_ohter_list = SuggestOther.objects.all()
    paginator = Paginator(suggest_ohter_list, 10) # 한 페이지에 10 개씩 데이터를 보이게 해 줌
    page = requests.GET.get('page', 1)

    try:
        suggest_others = paginator.page(page)
    except PageNotAnInteger:
        suggest_others = paginator.page(1)
    except EmptyPage:
        suggest_others = paginator.page(paginator.num_pages)

    page_numbers_range = 5

    pageGroup = math.ceil(int(page) / page_numbers_range)
    start_block = (pageGroup - 1) * page_numbers_range
    end_block = start_block + page_numbers_range

    paginator_range = paginator.page_range[start_block:end_block]

    context = {
        'suggest_others' : suggest_others,
        'paginator_range' : paginator_range,
    }

    return render(requests, 'suggest_other.html', context)

# 메인 페이지
def main(requests):
    return render(requests, 'main.html')

# 참여 가능한 투표 페이지
def participate(requests):
    return render(requests, 'participating-vote.html')

#참여 가능한 투표 페이지 -학교
def participate_school(requests):
    return render(requests, 'participating-vote_school.html')

#참여 가능한 투표 페이지 -학부
def participate_college(requests):
    return render(requests, 'participating-vote_college.html')   

#참여 가능한 투표 페이지 -학고
def participate_dept(requests):
    return render(requests, 'participating-vote_dept.html')       

# 참여 완료한 투표 페이지
def completion_participate(requests):
    return render(requests, 'completion-participating.html')

# 참여 완료한 투표 페이지-학교
def completion_participate_school(requests):
    return render(requests, 'completion-participating_school.html')

# 참여 완료한 투표 페이지-학부
def completion_participate_college(requests):
    return render(requests, 'completion-participating_college.html')

# 참여 완료한 투표 페이지-학과
def completion_participate_dept(requests):
    return render(requests, 'completion-participating_dept.html')

# 학교 투표 페이지
def school_vote(requests):
    school_vote_list = SchoolVote.objects.all()
    paginator = Paginator(school_vote_list, 3) # 한 페이지에 3 개씩 데이터를 보이게 해 줌
    page = requests.GET.get('page', 1)

    try:
        school_votes = paginator.page(page)
    except PageNotAnInteger:
        school_votes = paginator.page(1)
    except EmptyPage:
        school_votes = paginator.page(paginator.num_pages)

    page_numbers_range = 5

    pageGroup = math.ceil(int(page) / page_numbers_range)
    start_block = (pageGroup - 1) * page_numbers_range
    end_block = start_block + page_numbers_range

    paginator_range = paginator.page_range[start_block:end_block]

    context = {
        'school_votes' : school_votes,
        'paginator_range' : paginator_range,
    }

    return render(requests, 'school_vote.html', context)

# 단과대/학부 투표 페이지
def college_vote(requests):
    undergraduate_vote_list = UndergraduateVote.objects.all()
    paginator = Paginator(undergraduate_vote_list, 3) # 한 페이지에 3 개씩 데이터를 보이게 해 줌
    page = requests.GET.get('page', 1)

    try:
        undergraduate_votes = paginator.page(page)
    except PageNotAnInteger:
        undergraduate_votes = paginator.page(1)
    except EmptyPage:
        undergraduate_votes = paginator.page(paginator.num_pages)

    page_numbers_range = 5

    pageGroup = math.ceil(int(page) / page_numbers_range)
    start_block = (pageGroup - 1) * page_numbers_range
    end_block = start_block + page_numbers_range

    paginator_range = paginator.page_range[start_block:end_block]

    context = {
        'undergraduate_votes' : undergraduate_votes,
        'paginator_range' : paginator_range,
    }

    return render(requests, 'college_vote.html', context)

# 학과 투표 페이지
def department_vote(requests):
    major_vote_list = MajorVote.objects.all()
    paginator = Paginator(major_vote_list, 3) # 한 페이지에 3 개씩 데이터를 보이게 해 줌
    page = requests.GET.get('page', 1)

    try:
        major_votes = paginator.page(page)
    except PageNotAnInteger:
        major_votes = paginator.page(1)
    except EmptyPage:
        major_votes = paginator.page(paginator.num_pages)

    page_numbers_range = 5

    pageGroup = math.ceil(int(page) / page_numbers_range)
    start_block = (pageGroup - 1) * page_numbers_range
    end_block = start_block + page_numbers_range

    paginator_range = paginator.page_range[start_block:end_block]

    context = {
        'major_votes' : major_votes,
        'paginator_range' : paginator_range,
    }

    return render(requests, 'department_vote.html', context)

# 투표 만들기 페이지
def make_vote(requests):
    return render(requests, 'make_vote.html')

# 학교-투표하기 페이지
def school_voting(requests):
    return render(requests, 'school-voting.html')

# 학교-공약 페이지
def school_pledge(requests):
    return render(requests, 'school-pledge.html')

# 학부-투표하기 페이지
def college_voting(requests):
    return render(requests, 'college-voting.html')

# 학부-공약 페이지
def college_pledge(requests):
    return render(requests, 'college-pledge.html')

# 학과-투표하기 페이지
def department_voting(requests):
    return render(requests, 'department-voting.html')

# 학과-공약 페이지
def department_pledge(requests):
    return render(requests, 'department-pledge.html')

# 투표 결과 페이지
def result(requests):
    return render(requests, 'vote_result.html')

# 새로 만든 로그인 페이지
def login_new(requests):
    return render(requests, 'login_new.html')

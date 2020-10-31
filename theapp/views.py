from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import math
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth


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


# 공지사항 내용
def notice_content(requests,pk):
    notice = get_object_or_404(Notice, pk=pk)
    return render(requests, 'notice_content.html', {'notice':notice})

# 투표 건의사항 내용
def suggest_vote_content(requests,pk):
    sgvote = get_object_or_404(SuggestVote, pk=pk)
    return render(requests, 'suggest_vote_content.html', {'sgvote':sgvote}) 

# 기타 건의사항 내용
def suggest_other_content(requests,pk):
    sgother = get_object_or_404(SuggestOther, pk=pk)
    return render(requests, 'suggest_other_content.html', {'sgother':sgother})           

 #건의사항 작성 투표
def new_suggest_vote(requests):
    if requests.method =='POST':
        form = SuggestVoteForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('suggest-vote')
    else:
        form = SuggestVoteForm()
    return render(requests, 'new_suggest_vote.html', {'form':form})  

 #건의사항 작성 기타
def new_suggest_other(requests):
    if requests.method =='POST':
        form = SuggestOtherForm(requests.POST)
        if form.is_valid():
            form.save()
            return redirect('suggest-other')
    else:
        form = SuggestOtherForm()
    return render(requests, 'new_suggest_other.html', {'form':form})     

# 메인 페이지
def main(requests):
    return render(requests, 'main.html')

# 참여 가능한 투표 페이지
def participate(requests):
    school_vote=SchoolVote.objects.all()
    college_vote=UndergraduateVote.objects.all()
    major_vote=MajorVote.objects.all()

    context={
        'school_vote':school_vote,
        'college_vote':college_vote,
        'major_vote':major_vote,
    }
    return render(requests, 'participating-vote.html',context)

#참여 가능한 투표 페이지 -학교
def participate_school(requests):
    school_vote=SchoolVote.objects.all()
    return render(requests, 'participating-vote_school.html',{'school_vote':school_vote})

#참여 가능한 투표 페이지 -학부
def participate_college(requests):
    college_vote=UndergraduateVote.objects.all()
    return render(requests, 'participating-vote_college.html',{'college_vote':college_vote})   

#참여 가능한 투표 페이지 -학과
def participate_dept(requests):
    major_vote=MajorVote.objects.all()
    return render(requests, 'participating-vote_dept.html',{'major_vote':major_vote})       

# 참여 완료한 투표 페이지
def completion_participate(requests):
    school_vote=SchoolVote.objects.all()
    college_vote=UndergraduateVote.objects.all()
    major_vote=MajorVote.objects.all()

    context={
        'school_vote':school_vote,
        'college_vote':college_vote,
        'major_vote':major_vote,
    }
    return render(requests, 'completion-participating.html',context)

# 참여 완료한 투표 페이지-학교
def completion_participate_school(requests):
    school_vote=SchoolVote.objects.all()
    return render(requests, 'completion-participating_school.html',{'school_vote':school_vote})

# 참여 완료한 투표 페이지-학부
def completion_participate_college(requests):
    college_vote=UndergraduateVote.objects.all()
    return render(requests, 'completion-participating_college.html',{'college_vote':college_vote})

# 참여 완료한 투표 페이지-학과
def completion_participate_dept(requests):
    major_vote=MajorVote.objects.all()
    return render(requests, 'completion-participating_dept.html',{'major_vote':major_vote})

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
def school_voting(requests, pk):
    school_vote = get_object_or_404(SchoolVote, pk=pk)
    return render(requests, 'school-voting.html', {'school_vote':school_vote})

def school_result(requests, pk):
    school_vote = get_object_or_404(SchoolVote, pk=pk)
    return render(requests, 'school-result.html',{'school_vote':school_vote})

# 학교-공약 페이지
def school_pledge(requests):
    return render(requests, 'school-pledge.html')

# 학부-투표하기 페이지
def college_voting(requests, pk):
    undergraduate_vote = get_object_or_404(UndergraduateVote, pk=pk)
    return render(requests, 'college-voting.html', {'undergraduate_vote':undergraduate_vote})

# 학부-공약 페이지
def college_pledge(requests):
    return render(requests, 'college-pledge.html')

# 학과-투표하기 페이지
def department_voting(requests, pk):
    dept_vote = get_object_or_404(MajorVote, pk=pk)
    return render(requests, 'department-voting.html', {'dept_vote':dept_vote})

# 학과-공약 페이지
def department_pledge(requests):
    return render(requests, 'department-pledge.html')

# 투표 결과 페이지
def result(requests):
    return render(requests, 'vote_result.html')

# 새로 만든 로그인 페이지
def login_new(requests):
    if requests.method == 'POST':    # POST 방식으로 들어온 지 확인
        username = requests.POST['username'] # 사용자로부터 전달 받은 유저 이름을 넣음
        password = requests.POST['password'] # 사용자로부터 전달 받은 패스워드를 넣음
        user = auth.authenticate(requests, username=username, password=password) # 전달받은 변수를 유저 변수에 넣어줌
        if user is not None:    # 유저가 존재한다면
            auth.login(requests, user)   # 이 유저가 존재하므로 로그인 해줌 
            return redirect('main')     # 메인 페이지로 이동
        else:
            return render(requests, 'login_new.html')    # 존재하지 않으면 로그인 페이지에 남아있게됨
    else:        
        return render(requests, 'login_new.html')   # POST방식이 아닐 경우 로그인 페이지에 남아있게 됨
    

def signup(request):
    if request.method == "POST":    # 요청방식이 POST방식인지 확인
        if request.POST['password1'] == request.POST['password2']:   # 입력한 비밀번호와 비밀번호 확인 부분이 같은지 확인
            user = User.objects.create_user(    # 유저 생성하는 함수
                request.POST['username'],   # 입력 받은 유저이름
                password = request.POST['password1'],    # 입력 받은 패스워드
                email = request.POST['email'],
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name']
            )
            college = request.POST["college"]
            major = request.POST["major"]
            student_id = request.POST["student_id"]
            profile = Profile(user=user, college=college, major=major, student_id=student_id)
            profile.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')   # 그 계정에 로그인을 하라는 요청을 다시 보냄
            return redirect('main')     # 메인으로 사용자가 갈 수 있게 리턴함
    return render(request, 'signup.html')   # 요청 방식이 POST가 아니라면 회원가입 페이지에 머무름


def logout(request):    #로그아웃에 대한 요청이 들어온다면, 
    if request.method == 'POST':
        auth.logout(request)    # auth.logout함수를 작동 => 로그아웃 진행됨
        return redirect('/') # 메인 페이지로 이동
    return render(request, 'main.html')

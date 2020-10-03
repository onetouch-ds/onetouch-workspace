from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)#회원
admin.site.register(Complete)#회원별 완료한 투표 목록

admin.site.register(SchoolVote)#학교투표
admin.site.register(UndergraduateVote)#학부생투표
admin.site.register(MajorVote)#학과투표
admin.site.register(VoteList)#모든 투표 합쳐놓은 것

admin.site.register(Notice)#공지
admin.site.register(SuggestVote)#투표 건의
admin.site.register(SuggestOther)#기타 건의


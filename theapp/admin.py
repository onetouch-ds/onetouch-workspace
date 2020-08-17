from django.contrib import admin
from theapp.models import make_school_vote,make_college_vote, make_dept_vote, Notice

# Register your models here.
admin.site.register(make_school_vote)
admin.site.register(make_college_vote)
admin.site.register(make_dept_vote)
admin.site.register(Notice)
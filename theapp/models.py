from django.db import models

# Create your models here.

class make_school_vote(models.Model):
    school_no = models.AutoField(primary_key=True)
    school_title = models.CharField(max_length=45)
    school_content = models.TextField(max_length=2000)
    school_deadline = models.DateTimeField()
    school_c1_name =  models.CharField(max_length=45)
    school_c2_name =  models.CharField(max_length=45)
    school_c3_name =  models.CharField(max_length=45)
    school_c4_name =  models.CharField(max_length=45)
    school_c5_name =  models.CharField(max_length=45)
    school_c1_ex = models.TextField(max_length=2000)
    school_c2_ex = models.TextField(max_length=2000)
    school_c3_ex = models.TextField(max_length=2000)
    school_c4_ex = models.TextField(max_length=2000)
    school_c5_ex = models.TextField(max_length=2000)

        def __str__(self):
        return self.school_title

class make_college_vote(models.Model):
    college_no = models.AutoField(primary_key=True)
    college_title = models.CharField(max_length=45)
    college_content = models.TextField(max_length=2000)
    college_deadline = models.DateTimeField()
    college_c1_name =  models.CharField(max_length=45)
    college_c2_name =  models.CharField(max_length=45)
    college_c3_name =  models.CharField(max_length=45)
    college_c4_name =  models.CharField(max_length=45)
    college_c5_name =  models.CharField(max_length=45)
    college_c1_ex = models.TextField(max_length=2000)
    college_c2_ex = models.TextField(max_length=2000)
    college_c3_ex = models.TextField(max_length=2000)
    college_c4_ex = models.TextField(max_length=2000)
    college_c5_ex = models.TextField(max_length=2000)

        def __str__(self):
        return self.college_title

class make_dept_vote(models.Model):
    dept_no = models.AutoField(primary_key=True)
    dept_title = models.CharField(max_length=45)
    dept_content = models.TextField(max_length=2000)
    dept_deadline = models.DateTimeField()
    dept_c1_name =  models.CharField(max_length=45)
    dept_c2_name =  models.CharField(max_length=45)
    dept_c3_name =  models.CharField(max_length=45)
    dept_c4_name =  models.CharField(max_length=45)
    dept_c5_name =  models.CharField(max_length=45)
    dept_c1_ex = models.TextField(max_length=2000)
    dept_c2_ex = models.TextField(max_length=2000)
    dept_c3_ex = models.TextField(max_length=2000)
    dept_c4_ex = models.TextField(max_length=2000)
    dept_c5_ex = models.TextField(max_length=2000)

        def __str__(self):
        return self.dept_title                


class notice(models.Model):
    noitce_pk = models.AutoField(primary_key=True)
    notice_title = models.CharField(max_length=45)
    notice_updateday = models.DateTimeField('date published')
    notice_writer = models.CharField(max_length=45)
    notice_count = models.IntegerField()
    notice_content = models.TextField(max_length=2000)


    def __str__(self):
        return self.notice_title
    

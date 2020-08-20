# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

<<<<<<< HEAD
# Create your models here.

class NoticeTable(models.Model):
    num = models.IntegerField()
    title = models.TextField()
    author = models.TextField()
    click = models.IntegerField()
    date = models.DateTimeField()
=======

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Complete(models.Model):
    complete_vote = models.IntegerField()
    member_mb_number = models.ForeignKey('Member', models.DO_NOTHING, db_column='member_mb_number')

    class Meta:
        managed = False
        db_table = 'complete'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MajorVote(models.Model):
    mj_vt_pk = models.IntegerField(primary_key=True)
    mj_vt_name = models.CharField(max_length=45)
    mj_vt_dday = models.DateField()
    mj_category1 = models.CharField(max_length=45, blank=True, null=True)
    mj_category2 = models.CharField(max_length=45, blank=True, null=True)
    mj_category3 = models.CharField(max_length=45, blank=True, null=True)
    mj_category4 = models.CharField(max_length=45, blank=True, null=True)
    mj_category5 = models.CharField(max_length=45, blank=True, null=True)
    mj_vt_result1 = models.CharField(max_length=45, blank=True, null=True)
    mj_vt_result2 = models.CharField(max_length=45, blank=True, null=True)
    mj_vt_result3 = models.CharField(max_length=45, blank=True, null=True)
    mj_vt_result4 = models.CharField(max_length=45, blank=True, null=True)
    mj_vt_result5 = models.CharField(max_length=45, blank=True, null=True)
    mj_final_result = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major_vote'


class Member(models.Model):
    mb_number = models.IntegerField(primary_key=True)
    mb_pw = models.IntegerField()
    mb_undergraduate = models.CharField(max_length=45)
    mb_major = models.CharField(max_length=45)
    mb_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'member'


class Notice(models.Model):
    nt_pk = models.IntegerField(primary_key=True)
    nt_title = models.CharField(max_length=45)
    nt_writer = models.CharField(max_length=45)
    nt_count = models.IntegerField(blank=True, null=True)
    nt_updateday = models.DateField()

    class Meta:
        managed = False
        db_table = 'notice'


class SchoolVote(models.Model):
    sh_vt_pk = models.IntegerField(primary_key=True)
    sh_vt_name = models.CharField(max_length=45)
    sh_vt_dday = models.DateField()
    sh_category1 = models.CharField(max_length=45, blank=True, null=True)
    sh_category2 = models.CharField(max_length=45, blank=True, null=True)
    sh_category3 = models.CharField(max_length=45, blank=True, null=True)
    sh_category4 = models.CharField(max_length=45, blank=True, null=True)
    sh_category5 = models.CharField(max_length=45, blank=True, null=True)
    sh_vt_result1 = models.CharField(max_length=45, blank=True, null=True)
    sh_vt_result2 = models.CharField(max_length=45, blank=True, null=True)
    sh_vt_result3 = models.CharField(max_length=45, blank=True, null=True)
    sh_vt_result4 = models.CharField(max_length=45, blank=True, null=True)
    sh_vt_result5 = models.CharField(max_length=45, blank=True, null=True)
    sh_final_result = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_vote'


class SuggestOther(models.Model):
    sgother_pk = models.IntegerField(primary_key=True)
    sgother_title = models.CharField(max_length=45)
    sgother_writer = models.CharField(max_length=45)
    sgother_count = models.IntegerField(blank=True, null=True)
    sgother_updateday = models.DateField()
    sgother_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suggest_other'


class SuggestVote(models.Model):
    sgvote_pk = models.IntegerField(primary_key=True)
    sgvote_title = models.CharField(max_length=45)
    sgvote_writer = models.CharField(max_length=45)
    sgvote_count = models.IntegerField(blank=True, null=True)
    sgvote_updateday = models.DateField()
    sgvote_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suggest_vote'


class UndergraduateVote(models.Model):
    ud_vt_pk = models.IntegerField(primary_key=True)
    ud_vt_name = models.CharField(max_length=45)
    ud_vt_dday = models.DateField()
    ud_category1 = models.CharField(max_length=45, blank=True, null=True)
    ud_category2 = models.CharField(max_length=45, blank=True, null=True)
    ud_category3 = models.CharField(max_length=45, blank=True, null=True)
    ud_category4 = models.CharField(max_length=45, blank=True, null=True)
    ud_category5 = models.CharField(max_length=45, blank=True, null=True)
    ud_vt_result1 = models.CharField(max_length=45, blank=True, null=True)
    ud_vt_result2 = models.CharField(max_length=45, blank=True, null=True)
    ud_vt_result3 = models.CharField(max_length=45, blank=True, null=True)
    ud_vt_result4 = models.CharField(max_length=45, blank=True, null=True)
    ud_vt_result5 = models.CharField(max_length=45, blank=True, null=True)
    ud_final_result = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'undergraduate_vote'


class VoteList(models.Model):
    school_vote_sh_vt_pk = models.ForeignKey(SchoolVote, models.DO_NOTHING, db_column='school_vote_sh_vt_pk')
    undergraduate_vote_ud_vt_pk = models.ForeignKey(UndergraduateVote, models.DO_NOTHING, db_column='undergraduate_vote_ud_vt_pk')
    major_vote_mj_vt_pk = models.ForeignKey(MajorVote, models.DO_NOTHING, db_column='major_vote_mj_vt_pk')

    class Meta:
        managed = False
        db_table = 'vote_list'
>>>>>>> 1e084498faeb6345ef38af6c6324c8abdfc2f896

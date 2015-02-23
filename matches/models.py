from __future__ import unicode_literals
from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        db_table = 'auth_group_permissions'


class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey('AuthUser')
    message = models.TextField()

    class Meta:
        db_table = 'auth_message'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        db_table = 'django_session'


class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'django_site'

class Team(models.Model):
    _id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    foundation = models.IntegerField(blank=True, null=True)
    logo = models.CharField(max_length=50)
    story = models.TextField()

class Matches(models.Model):
    match_id = models.AutoField(primary_key=True)
    home = models.CharField(max_length=30)
    home_id = models.ManyToManyField(Team, related_name='home_id')
    away = models.CharField(max_length=30)
    away_id = models.ManyToManyField(Team, related_name='away_id')
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)
    home_rating_before = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    home_rating_after = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    away_rating_before = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    away_rating_after = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    match_date = models.DateField(blank=True, null=True)
    tournament = models.CharField(max_length=50, blank=True)
    stadium = models.CharField(max_length=100, blank=True, null=True)
    home_scorers = models.CharField(max_length=1000, blank=True, null=True)
    away_scorers = models.CharField(max_length=1000, blank=True, null=True)
    ref = models.CharField(max_length=40, blank=True, null=True)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    doubtdate = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matches'
        verbose_name_plural = 'Matches'

    def __unicode__(self):
		return "(" + str(self.match_date) + ") " + self.home + " - " + self.away + " - " + str(self.home_score) + ":" + str(self.away_score)

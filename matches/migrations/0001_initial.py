# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AuthGroup'
        db.create_table(u'auth_group', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=80)),
        ))
        db.send_create_signal('matches', ['AuthGroup'])

        # Adding model 'AuthGroupPermissions'
        db.create_table(u'auth_group_permissions', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthGroup'])),
            ('permission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthPermission'])),
        ))
        db.send_create_signal('matches', ['AuthGroupPermissions'])

        # Adding model 'AuthMessage'
        db.create_table(u'auth_message', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthUser'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('matches', ['AuthMessage'])

        # Adding model 'AuthPermission'
        db.create_table(u'auth_permission', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.DjangoContentType'])),
            ('codename', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('matches', ['AuthPermission'])

        # Adding model 'AuthUser'
        db.create_table(u'auth_user', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('is_staff', self.gf('django.db.models.fields.IntegerField')()),
            ('is_active', self.gf('django.db.models.fields.IntegerField')()),
            ('is_superuser', self.gf('django.db.models.fields.IntegerField')()),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('matches', ['AuthUser'])

        # Adding model 'AuthUserGroups'
        db.create_table(u'auth_user_groups', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthUser'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthGroup'])),
        ))
        db.send_create_signal('matches', ['AuthUserGroups'])

        # Adding model 'AuthUserUserPermissions'
        db.create_table(u'auth_user_user_permissions', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthUser'])),
            ('permission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthPermission'])),
        ))
        db.send_create_signal('matches', ['AuthUserUserPermissions'])

        # Adding model 'DjangoAdminLog'
        db.create_table(u'django_admin_log', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('action_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('object_id', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('object_repr', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('action_flag', self.gf('django.db.models.fields.IntegerField')()),
            ('change_message', self.gf('django.db.models.fields.TextField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.DjangoContentType'], null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthUser'])),
        ))
        db.send_create_signal('matches', ['DjangoAdminLog'])

        # Adding model 'DjangoContentType'
        db.create_table(u'django_content_type', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('app_label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('matches', ['DjangoContentType'])

        # Adding model 'DjangoMigrations'
        db.create_table(u'django_migrations', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('applied', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('matches', ['DjangoMigrations'])

        # Adding model 'DjangoSession'
        db.create_table(u'django_session', (
            ('session_key', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('session_data', self.gf('django.db.models.fields.TextField')()),
            ('expire_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('matches', ['DjangoSession'])

        # Adding model 'DjangoSite'
        db.create_table(u'django_site', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('matches', ['DjangoSite'])

        # Adding model 'Matches'
        db.create_table(u'matches', (
            ('match_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('home', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('away', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('home_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('away_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('home_rating_before', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('home_rating_after', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('away_rating_before', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('away_rating_after', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('match_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('tournament', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('stadium', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('home_scorers', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('away_scorers', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('ref', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
        ))
        db.send_create_signal('matches', ['Matches'])


    def backwards(self, orm):
        # Deleting model 'AuthGroup'
        db.delete_table(u'auth_group')

        # Deleting model 'AuthGroupPermissions'
        db.delete_table(u'auth_group_permissions')

        # Deleting model 'AuthMessage'
        db.delete_table(u'auth_message')

        # Deleting model 'AuthPermission'
        db.delete_table(u'auth_permission')

        # Deleting model 'AuthUser'
        db.delete_table(u'auth_user')

        # Deleting model 'AuthUserGroups'
        db.delete_table(u'auth_user_groups')

        # Deleting model 'AuthUserUserPermissions'
        db.delete_table(u'auth_user_user_permissions')

        # Deleting model 'DjangoAdminLog'
        db.delete_table(u'django_admin_log')

        # Deleting model 'DjangoContentType'
        db.delete_table(u'django_content_type')

        # Deleting model 'DjangoMigrations'
        db.delete_table(u'django_migrations')

        # Deleting model 'DjangoSession'
        db.delete_table(u'django_session')

        # Deleting model 'DjangoSite'
        db.delete_table(u'django_site')

        # Deleting model 'Matches'
        db.delete_table(u'matches')


    models = {
        'matches.authgroup': {
            'Meta': {'object_name': 'AuthGroup', 'db_table': "u'auth_group'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'})
        },
        'matches.authgrouppermissions': {
            'Meta': {'object_name': 'AuthGroupPermissions', 'db_table': "u'auth_group_permissions'"},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.AuthPermission']"})
        },
        'matches.authmessage': {
            'Meta': {'object_name': 'AuthMessage', 'db_table': "u'auth_message'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.AuthUser']"})
        },
        'matches.authpermission': {
            'Meta': {'object_name': 'AuthPermission', 'db_table': "u'auth_permission'"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.DjangoContentType']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'matches.authuser': {
            'Meta': {'object_name': 'AuthUser', 'db_table': "u'auth_user'"},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {}),
            'is_staff': ('django.db.models.fields.IntegerField', [], {}),
            'is_superuser': ('django.db.models.fields.IntegerField', [], {}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'matches.authusergroups': {
            'Meta': {'object_name': 'AuthUserGroups', 'db_table': "u'auth_user_groups'"},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.AuthGroup']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.AuthUser']"})
        },
        'matches.authuseruserpermissions': {
            'Meta': {'object_name': 'AuthUserUserPermissions', 'db_table': "u'auth_user_user_permissions'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'permission': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.AuthPermission']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.AuthUser']"})
        },
        'matches.djangoadminlog': {
            'Meta': {'object_name': 'DjangoAdminLog', 'db_table': "u'django_admin_log'"},
            'action_flag': ('django.db.models.fields.IntegerField', [], {}),
            'action_time': ('django.db.models.fields.DateTimeField', [], {}),
            'change_message': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.DjangoContentType']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'object_repr': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.AuthUser']"})
        },
        'matches.djangocontenttype': {
            'Meta': {'object_name': 'DjangoContentType', 'db_table': "u'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'matches.djangomigrations': {
            'Meta': {'object_name': 'DjangoMigrations', 'db_table': "u'django_migrations'"},
            'app': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'applied': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'matches.djangosession': {
            'Meta': {'object_name': 'DjangoSession', 'db_table': "u'django_session'"},
            'expire_date': ('django.db.models.fields.DateTimeField', [], {}),
            'session_data': ('django.db.models.fields.TextField', [], {}),
            'session_key': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'})
        },
        'matches.djangosite': {
            'Meta': {'object_name': 'DjangoSite', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'matches.matches': {
            'Meta': {'object_name': 'Matches', 'db_table': "u'matches'"},
            'away': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'away_rating_after': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'away_rating_before': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'away_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'away_scorers': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'home': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'home_rating_after': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'home_rating_before': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'home_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_scorers': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'match_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'match_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'tournament': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['matches']
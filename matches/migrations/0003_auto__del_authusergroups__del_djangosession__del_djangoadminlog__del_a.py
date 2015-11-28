# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        """
        # Adding model 'Team'
        db.create_table('matches_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('latin', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('foundation', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('logo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('story', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('in_menu', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('matches', ['Team'])

        # Adding field 'Matches.home_link'
        db.add_column(u'matches', 'home_link',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'home_team', null=True, to=orm['matches.Team']),
                      keep_default=False)

        # Adding field 'Matches.away_link'
        db.add_column(u'matches', 'away_link',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'away_team', null=True, to=orm['matches.Team']),
                      keep_default=False)

        # Adding field 'Matches.doubtdate'
        db.add_column(u'matches', 'doubtdate',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)
        """


        # Changing field 'Matches.comment'
        db.alter_column(u'matches', 'comment', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True))

        # Changing field 'Matches.ref'
        db.alter_column(u'matches', 'ref', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Matches.home_scorers'
        db.alter_column(u'matches', 'home_scorers', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True))

        # Changing field 'Matches.stadium'
        db.alter_column(u'matches', 'stadium', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Matches.away_scorers'
        db.alter_column(u'matches', 'away_scorers', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True))

    def backwards(self, orm):
        # Adding model 'AuthUserGroups'
        db.create_table(u'auth_user_groups', (
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthGroup'])),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthUser'])),
        ))
        db.send_create_signal('matches', ['AuthUserGroups'])

        # Adding model 'DjangoSession'
        db.create_table(u'django_session', (
            ('session_key', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('session_data', self.gf('django.db.models.fields.TextField')()),
            ('expire_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('matches', ['DjangoSession'])

        # Adding model 'DjangoAdminLog'
        db.create_table(u'django_admin_log', (
            ('action_flag', self.gf('django.db.models.fields.IntegerField')()),
            ('action_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('change_message', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthUser'])),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.DjangoContentType'], null=True, blank=True)),
            ('object_repr', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('matches', ['DjangoAdminLog'])

        # Adding model 'AuthPermission'
        db.create_table(u'auth_permission', (
            ('codename', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.DjangoContentType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('matches', ['AuthPermission'])

        # Adding model 'AuthGroup'
        db.create_table(u'auth_group', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80, unique=True)),
        ))
        db.send_create_signal('matches', ['AuthGroup'])

        # Adding model 'AuthUser'
        db.create_table(u'auth_user', (
            ('username', self.gf('django.db.models.fields.CharField')(max_length=30, unique=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_active', self.gf('django.db.models.fields.IntegerField')()),
            ('is_staff', self.gf('django.db.models.fields.IntegerField')()),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')()),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('is_superuser', self.gf('django.db.models.fields.IntegerField')()),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')()),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('matches', ['AuthUser'])

        # Adding model 'DjangoContentType'
        db.create_table(u'django_content_type', (
            ('model', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('app_label', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('matches', ['DjangoContentType'])

        # Adding model 'AuthGroupPermissions'
        db.create_table(u'auth_group_permissions', (
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthGroup'])),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('permission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthPermission'])),
        ))
        db.send_create_signal('matches', ['AuthGroupPermissions'])

        # Adding model 'DjangoMigrations'
        db.create_table(u'django_migrations', (
            ('applied', self.gf('django.db.models.fields.DateTimeField')()),
            ('app', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('matches', ['DjangoMigrations'])

        # Adding model 'AuthUserUserPermissions'
        db.create_table(u'auth_user_user_permissions', (
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthUser'])),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('permission', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthPermission'])),
        ))
        db.send_create_signal('matches', ['AuthUserUserPermissions'])

        # Adding model 'DjangoSite'
        db.create_table(u'django_site', (
            ('domain', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('matches', ['DjangoSite'])

        # Adding model 'AuthMessage'
        db.create_table(u'auth_message', (
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.AuthUser'])),
        ))
        db.send_create_signal('matches', ['AuthMessage'])

        # Deleting model 'Team'
        db.delete_table('matches_team')

        # Deleting field 'Matches.home_link'
        db.delete_column(u'matches', 'home_link_id')

        # Deleting field 'Matches.away_link'
        db.delete_column(u'matches', 'away_link_id')

        # Deleting field 'Matches.doubtdate'
        db.delete_column(u'matches', 'doubtdate')


        # Changing field 'Matches.comment'
        db.alter_column(u'matches', 'comment', self.gf('django.db.models.fields.CharField')(default='', max_length=1000))

        # Changing field 'Matches.ref'
        db.alter_column(u'matches', 'ref', self.gf('django.db.models.fields.CharField')(default='', max_length=40))

        # Changing field 'Matches.home_scorers'
        db.alter_column(u'matches', 'home_scorers', self.gf('django.db.models.fields.CharField')(default='', max_length=1000))

        # Changing field 'Matches.stadium'
        db.alter_column(u'matches', 'stadium', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Matches.away_scorers'
        db.alter_column(u'matches', 'away_scorers', self.gf('django.db.models.fields.CharField')(default='', max_length=1000))

    models = {
        'matches.matches': {
            'Meta': {'object_name': 'Matches', 'db_table': "u'matches'"},
            'away': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'away_link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'away_team'", 'null': 'True', 'to': "orm['matches.Team']"}),
            'away_rating_after': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'away_rating_before': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'away_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'away_scorers': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'doubtdate': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'home': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'home_link': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'home_team'", 'null': 'True', 'to': "orm['matches.Team']"}),
            'home_rating_after': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'home_rating_before': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'home_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_scorers': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'match_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'match_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'stadium': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'tournament': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'matches.team': {
            'Meta': {'ordering': "[u'name']", 'object_name': 'Team'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'foundation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menu': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'latin': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'story': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['matches']
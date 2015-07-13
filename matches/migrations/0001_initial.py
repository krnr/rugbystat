# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('match_id', models.AutoField(serialize=False, primary_key=True)),
                ('home', models.CharField(max_length=30)),
                ('away', models.CharField(max_length=30)),
                ('home_score', models.IntegerField(null=True, blank=True)),
                ('away_score', models.IntegerField(null=True, blank=True)),
                ('home_rating_before', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('home_rating_after', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('away_rating_before', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('away_rating_after', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('match_date', models.DateField(null=True, blank=True)),
                ('tournament', models.CharField(max_length=50, blank=True)),
                ('stadium', models.CharField(max_length=100, null=True, blank=True)),
                ('home_scorers', models.TextField(max_length=1000, null=True, blank=True)),
                ('away_scorers', models.TextField(max_length=1000, null=True, blank=True)),
                ('ref', models.CharField(max_length=40, null=True, blank=True)),
                ('comment', models.TextField(max_length=1000, null=True, blank=True)),
                ('doubtdate', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'matches',
                'verbose_name_plural': 'Matches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('foundation', models.IntegerField(null=True, blank=True)),
                ('logo', models.CharField(max_length=50, blank=True)),
                ('story', models.TextField(blank=True)),
                ('in_menu', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='matches',
            name='home_link',
            field=models.ForeignKey(related_name='home_team', to='matches.Team'),
            preserve_default=True,
        ),
    ]

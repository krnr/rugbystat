# -*- coding: utf-8
from __future__ import unicode_literals
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=30)
    latin = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    link = models.URLField(blank=True, null=True)
    foundation = models.IntegerField(blank=True, null=True)
    logo = models.URLField(blank=True, null=True)
    story = models.TextField(blank=True)
    in_menu = models.BooleanField(default=True)

    def __unicode__(self):
        # sample output: Буревестник (СПб) or РК Волгоград to avoid rendering Волгоград (Волгоград)
        return "%s (%s)" % (self.name, self.city) if self.name != self.city else u'РК ' + self.name

    class Meta:
        ordering = ['name']

class Matches(models.Model):
    # the class should be named Match, but...)))
    match_id = models.AutoField(primary_key=True)
    home = models.CharField(max_length=30)
    home_link = models.ForeignKey(Team, blank=True, null=True, related_name='home_team')
    # 'home' - for the name which can be different throughout team's existence
    # 'home_link' - is a key to unique Team class
    away = models.CharField(max_length=30)
    away_link = models.ForeignKey(Team, blank=True, null=True, related_name='away_team')
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)
    home_rating_before = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    home_rating_after = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    away_rating_before = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    away_rating_after = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    match_date = models.DateField(blank=True, null=True)
    # next 5 fields a strings and someday - may be - will become ForeignKeys to classes Player, Stadium, etc...
    tournament = models.CharField(max_length=50, blank=True)
    stadium = models.CharField(max_length=100, blank=True, null=True)
    home_scorers = models.TextField(max_length=1000, blank=True, null=True)
    away_scorers = models.TextField(max_length=1000, blank=True, null=True)
    ref = models.CharField(max_length=40, blank=True, null=True)
    # at present 'comment' field isn't rendered anywhere. just for inner usage
    comment = models.TextField(max_length=1000, blank=True, null=True)
    doubtdate = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'matches'
        verbose_name_plural = 'Matches'
        # ordering with 2 fields, because sometimes there could be 2 matches in one day for one team
        ordering = ['-match_date', '-match_id']

    def get_score(self):
        # returns smth like '32:17' when the result is known and 'в : п' if the result is 1:0
        # i.e. score is unclear but we clearly know who won
        # the function is used in templates
        if self.home_score == 1:
            return u'в : п'
        elif self.away_score == 1:
            return u'п : в'
        else:
            # checking that both fields are filled
            h_score, a_score = self.home_score, self.away_score
            if self.home_score is None:
                h_score = "??"
            if self.away_score is None:
                a_score = "??"
            return "%s:%s" % (str(h_score), str(a_score))

    def __unicode__(self):
		return "(" + str(self.match_date) + ") " + self.home + " - " + self.away + " - " + str(self.home_score) + ":" + str(self.away_score)
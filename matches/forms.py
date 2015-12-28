# -*- coding: utf-8

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from matches.models import Match

class MatchForm(forms.ModelForm):
    """MatchForm is a ModelForm from django"""
    class Meta:
        # tell Django which model should be used to create this form
        model = Match
        fields = ('home', 'home_link', 'away', 'away_link', 'home_score', 'away_score', 'match_date', 'tournament', 'stadium', 'ref', 'home_scorers', 'away_scorers', 'comment', )
        widgets = {
          'match_date': AdminDateWidget(),
          'home_scorers': forms.Textarea(attrs={'rows':4, 'cols':40,'placeholder':"Авторы попыток, реализаций, штрафных..."}),
          'away_scorers': forms.Textarea(attrs={'rows':4, 'cols':40,'placeholder':"Авторы попыток, реализаций, штрафных..."}),
          'home': forms.Textarea(attrs={'rows':4, 'cols':40, 'placeholder': "Название команды"}),
          'away': forms.Textarea(attrs={'rows':4, 'cols':40, 'placeholder': "Название команды"}),
          'comment': forms.Textarea(attrs={'rows':4, 'cols':40}),
        }

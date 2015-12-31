# -*- coding: utf-8
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from matches.models import Match

class MatchForm(forms.ModelForm):
    """MatchForm is a ModelForm from django"""
    
    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        tourn_help = mark_safe(u'Пока для турниров нет отдельной модели, нужно заполнить поле обычным текстом. Полный список турниров - http://krnr.pythonanywhere.com/all_tourn/ (тэги тут не работают).')
        self.fields['home'].help_text = 'Это название команды будет отображаться в списке матчей'
        self.fields['away'].help_text = 'Это название команды будет отображаться в списке матчей'
        self.fields['home_scorers'].help_text = 'Авторы попыток, реализаций, штрафных. Отображается в карточке матча'
        self.fields['away_scorers'].help_text = 'Авторы попыток, реализаций, штрафных. Отображается в карточке матча'
        self.fields['tournament'].help_text = tourn_help

        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update({
                  'class': 'has-popover', 
                  'data-content': help_text, 
                  'data-placement': 'right', 
                  'data-container': 'body'})

    class Meta:
        # tell Django which model should be used to create this form
        model = Match
        fields = ('home_link', 'home', 'away_link', 'away', \
          'home_rating_before', 'home_rating_after', 'away_rating_before', 'away_rating_after', \
          'home_score', 'away_score', 'match_date', 'tournament', 'stadium', 'ref', \
          'home_scorers', 'away_scorers', 'comment', )
        widgets = {
          'match_date': AdminDateWidget(),
          'home_scorers': forms.Textarea(attrs={'rows':4, 'cols':36,}),
          'away_scorers': forms.Textarea(attrs={'rows':4, 'cols':36,}),
          'home': forms.Textarea(attrs={'rows':1, 'cols':36,}),
          'away': forms.Textarea(attrs={'rows':1, 'cols':36,}),
          'home_rating_before': forms.TextInput(attrs={'readonly':True,}),
          'home_rating_after': forms.TextInput(attrs={'readonly':True,}),
          'away_rating_before': forms.TextInput(attrs={'readonly':True,}),
          'away_rating_after': forms.TextInput(attrs={'readonly':True,}),
          'comment': forms.Textarea(attrs={'rows':4, 'cols':36}),
        }

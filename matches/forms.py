# -*- coding: utf-8

from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from matches.models import Match

class MatchForm(forms.ModelForm):
    """MatchForm is a ModelForm from django"""
    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        self.fields['home'].help_text = 'Это название команды будет отображаться в списке матчей'
        self.fields['away'].help_text = 'Это название команды будет отображаться в списке матчей'
        self.fields['home_scorers'].help_text = 'Авторы попыток, реализаций, штрафных. Отображается в карточке матча'
        self.fields['away_scorers'].help_text = 'Авторы попыток, реализаций, штрафных. Отображается в карточке матча'
        self.fields['home_rating_before'] = forms.DecimalField(widget=forms.HiddenInput(attrs={'readonly':True,}))
        self.fields['home_rating_after'] = forms.DecimalField(widget=forms.HiddenInput(attrs={'readonly':True,}))
        self.fields['away_rating_before'] = forms.DecimalField(widget=forms.HiddenInput(attrs={'readonly':True,}))
        self.fields['away_rating_after'] = forms.DecimalField(widget=forms.HiddenInput(attrs={'readonly':True,}))

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
          'home_scorers': forms.Textarea(attrs={'rows':4, 'cols':40,}),
          'away_scorers': forms.Textarea(attrs={'rows':4, 'cols':40,}),
          'home': forms.Textarea(attrs={'rows':1, 'cols':40,}),
          'away': forms.Textarea(attrs={'rows':1, 'cols':40,}),
          'comment': forms.Textarea(attrs={'rows':4, 'cols':40}),
        }

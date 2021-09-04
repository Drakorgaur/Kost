from django import forms


AMOUNT=[('9','9 players'),
        ('11','11 players')]
class PlayersForm(forms.Form):
    players = forms.ChoiceField(choices=AMOUNT, widget=forms.RadioSelect)
    room_name = forms.CharField(strip=False, required=False)
    timer = forms.IntegerField(initial=60)
    timer2 = forms.IntegerField(initial=30, label='2nd Timer')
    fouls = forms.IntegerField(initial=3)
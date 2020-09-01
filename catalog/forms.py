from django import forms
import datetime

class SimpleForm(forms.Form):
    name = forms.CharField(label= "Name*", max_length=350, widget=forms.TextInput(attrs={'style': 'width: 350px; height: 50px; border-radius: 5px;' }))
    email = forms.EmailField(label='Email*', max_length=255, widget=forms.TextInput(attrs={'style': 'width: 350px; height: 50px; border-radius: 5px;' }))
    phone_number = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'style': 'width: 350px; height: 50px; border-radius: 5px;' }))
    date = forms.DateField(initial=datetime.date.today, widget=forms.TextInput(attrs={'style': 'width: 350px; height: 50px; border-radius: 5px;' }))
    time = forms.TimeField(initial=datetime.time, widget=forms.TextInput(attrs={'style': 'width: 350px; height: 50px; border-radius: 5px;' }))
    OPTIONS = (
        ("A La Carte", "A La Carte"),
        ("Catering", "Catering"),
        ("Box Lunch", "Box Lunch"),
    )
    Services = forms.ChoiceField(choices=OPTIONS, widget=forms.Select(attrs={'size':'1', 'style': 'width: 350px; height: 50px;'}))
    appointment_notes = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'width: 1100px; height: 100px; border-radius: 5px;' }),
        help_text='Write here your message!'
    )
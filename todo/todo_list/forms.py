from django import forms


SHOICES = [
    ('high', 'High'),
    ('mid', 'Mid'),
    ('low', 'Low'),
]


class TaskForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Complete your task '}))
    priority = forms.CharField(label='set priority', widget=forms.Select(choices=SHOICES, attrs={'id': 'priority'}))

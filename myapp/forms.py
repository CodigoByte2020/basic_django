from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Título de área', max_length=200, widget=forms.TextInput(attrs={
        'class': 'style_title'}))
    description = forms.CharField(label='Descripción de la tarea', widget=forms.Textarea(attrs={
        'class': 'style_description'}))

from django import forms

class User_form(forms.Form):
    name = forms.CharField(label="Имя")
    email = forms.EmailField(label="Почта")
    topic = forms.CharField(label="Тема")
    description = forms.CharField(label="Комментарий", widget=forms.Textarea)


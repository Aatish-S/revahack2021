from django import forms

class HomeForm(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={"class":"textbox"}))
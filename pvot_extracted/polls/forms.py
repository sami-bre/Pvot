from django import forms


class EmailPostForm(forms.Form):
    first_name = forms.CharField(max_length=25, label='First name', label_suffix='', widget=forms.PasswordInput)
    last_name = forms.CharField(max_length=25, label='Last name', label_suffix='', widget=forms.PasswordInput)
    voter_id = forms.CharField(max_length=25, label='Voter id', label_suffix='', widget=forms.PasswordInput)

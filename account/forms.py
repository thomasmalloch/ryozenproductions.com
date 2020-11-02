from django import forms
from django.contrib.auth.models import User

UserForm_NAME_MAPPING = {
    'first_name': 'First Name:',
    'last_name': 'Last Name:',
    'username': 'Username:',
    'email': 'Email:',
    'password': 'Password:',
    'confirm_password': 'Confirm Password:'
}


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email__iexact=email).exists():
            raise forms.ValidationError("This email has already been used!")

        return email

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Your passwords do not match. Please enter the same password and try again.")

        return cleaned_data

    def add_prefix(self, field_name):
        # look up field name; return original if not found
        field_name = UserForm_NAME_MAPPING.get(field_name, field_name)
        return super(UserForm, self).add_prefix(field_name)


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput())


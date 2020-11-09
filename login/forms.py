from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password, get_password_validators

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

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = self.cleaned_data['email']

        if User.objects.exclude(pk=self.instance.pk).filter(email__iexact=email).exists():
            raise forms.ValidationError("This email has already been used!")

        if password != confirm_password:
            raise forms.ValidationError("Your passwords do not match. Please enter the same password and try again.")

        user = None
        try:
            user = User.objects.create_user(
                username=cleaned_data["email"],
                email=cleaned_data["email"],
                password=cleaned_data["password"],
                first_name=cleaned_data["first_name"],
                last_name=cleaned_data["last_name"])
        except:
            user = None

        if user is not None:
            validate_password(password, user)
        else:
            forms.ValidationError("Something unexpected happened")

        user.delete()
        return cleaned_data

    def add_prefix(self, field_name):
        # look up field name; return original if not found
        field_name = UserForm_NAME_MAPPING.get(field_name, field_name)
        return super(UserForm, self).add_prefix(field_name)


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        try:
            user = User.objects.get(email=cleaned_data["email"])
        except:
            raise forms.ValidationError("Email or password are incorrect")

        user = authenticate(username=user.username, password=cleaned_data["password"])
        if user is None:
            raise forms.ValidationError("Email or password are incorrect")

        cleaned_data["user"] = user
        return cleaned_data

    def add_prefix(self, field_name):
        # look up field name; return original if not found
        field_name = UserForm_NAME_MAPPING.get(field_name, field_name)
        return super(LoginForm, self).add_prefix(field_name)

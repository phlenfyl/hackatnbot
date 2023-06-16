from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from . models import User

ROLE_CHOICES = (
                (" ", "........."), ("student", "Student"), ("staff", "Staff"),
                ("non staff", "Non Staff"), ("non student", "Non Student")
                )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    role = forms.CharField(widget=forms.Select(choices=ROLE_CHOICES))

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["role"].required = True

        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
        self.fields["password1"].label = "Password"
        self.fields["password2"].label = "Confirm Password"

        self.fields["first_name"].widget.attrs.update({"placeholder": "Enter First Name"})
        self.fields["last_name"].widget.attrs.update({"placeholder": "Enter Last Name"})
        self.fields["email"].widget.attrs.update({"placeholder": "Enter Email"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Enter Password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Confirm Password"})

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2", "role"]
        error_messages = {
            "first_name": {"required": "First name is required", "max_length": "Name is too long"},
            "last_name": {"required": "Last name is required", "max_length": "Last Name is too long"},
            "role": {"required": "Role is required"},
        }

    def clean_role(self):
        role = self.cleaned_data.get("role")
        if not role:
            raise forms.ValidationError("Role is required")
        return role
    

class SignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields["email"].widget.attrs.update({"placeholder": "Enter Email"})
        self.fields["password"].widget.attrs.update({"placeholder": "Enter Password"})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(SignInForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user




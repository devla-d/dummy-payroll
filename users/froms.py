from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from users.models import EmployeeID

User = get_user_model()

DESIGNATION = (
    ("MANAGER", "MANAGER"),
    ("ACCOUNTANT", "ACCOUNTANT"),
    ("ADVISOR", "ADVISOR"),
)


class RegisterForm(UserCreationForm):

    fullname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Fullname",
            }
        ),
        label="Fullname",
        required=True,
    )
    email = forms.EmailField(
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "Email",
            }
        ),
        label="Email",
        required=True,
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "xxxxxxxxxx",
            }
        ),
        label="Employee ID",
        required=True,
    )

    password1 = forms.CharField(
        max_length=30,
        min_length=6,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=30,
        min_length=6,
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Comfirm Password",
                "class": "form-control",
            }
        ),
    )

    designation = forms.ChoiceField(
        choices=DESIGNATION,
        widget=forms.Select(
            attrs={"class": "form-select", "aria-label": "Default select example"}
        ),
        label="Designation",
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "fullname",
            "password1",
            "password2",
            "designation",
        ]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not EmployeeID.objects.filter(unique_id__exact=username).exists():
            raise forms.ValidationError("Id code is invalid".capitalize())
        else:
            if User.objects.filter(username__exact=username).exists():
                raise forms.ValidationError(
                    "A user with this id code already exist".capitalize()
                )
        return username


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "xxxxxxxxxx",
            }
        ),
        label="Employee ID",
        required=True,
    )

    password = forms.CharField(
        max_length=30,
        min_length=6,
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "********",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password")

    def clean(self):
        if self.is_valid():
            if not authenticate(
                username=self.cleaned_data["username"],
                password=self.cleaned_data["password"],
            ):
                raise forms.ValidationError("Invalid Username and Password")


class ProfileForm(UserCreationForm):

    fullname = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Fullname",
                "disabled": "true",
            }
        ),
        label="Fullname",
        required=False,
    )
    email = forms.EmailField(
        max_length=80,
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "placeholder": "Email",
                "disabled": "true",
            }
        ),
        label="Email",
        required=False,
    )
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "xxxxxxxxxx",
                "disabled": "true",
            }
        ),
        label="Employee ID",
        required=False,
    )

    designation = forms.ChoiceField(
        choices=DESIGNATION,
        widget=forms.Select(
            attrs={"class": "form-select", "aria-label": "Default select example"}
        ),
        label="Designation",
        required=False,
    )

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "fullname",
            "designation",
        ]

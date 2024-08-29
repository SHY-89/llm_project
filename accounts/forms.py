from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    UserChangeForm, 
    ReadOnlyPasswordHashField,
    PasswordChangeForm,
)
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class MyAuthenticationForm(AuthenticationForm):
    pass

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", )

class MyUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        
    )
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", )
        exclude = ()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = help_text=_(
                "패스워드 수정은 "
                '<a href="{}">여기</a>'
                "를 눌러주세요."
            ).format( f"{reverse('accounts:update_password')}")


class MyPasswordChangeForm(PasswordChangeForm):
    pass
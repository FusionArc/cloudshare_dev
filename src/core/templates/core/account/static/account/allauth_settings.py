ACCOUNT_FORMS = [
    {'login': 'allauth.account.forms.LoginForm'},
    {'signup': 'allauth.account.forms.SignupForm'},
    {'add_email': 'allauth.account.forms.AddEmailForm'},
    {'change_password': 'allauth.account.forms.ChangePasswordForm'},
    {'set_password': 'allauth.account.forms.SetPasswordForm'},
    {'reset_password': 'allauth.account.forms.ResetPasswordForm'},
    {'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm'},
    {'disconnect': 'allauth.socialaccount.forms.DisconnectForm'},
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = True

SOCIALACCOUNT_FORMS = {
    'login': 'allauth.socialaccount.forms.DisconnectForm',
    'signup': 'allauth.socialaccount.forms.SignupForm',
}

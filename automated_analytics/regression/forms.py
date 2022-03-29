from django import forms
from django.core import validators
from regression.models import User

class NewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'












    # name = forms.CharField()
    # lastName =
    # email = forms.EmailField()
    # verify_email = forms.EmailField(label='Re-enter your email')
    # textArea = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)




    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vmail = all_clean_data['verify_email']
    #
    #     if email != vmail:
    #         raise forms.ValidationError("Emails do not match!")

    # Not needed, django has built in validation
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher):
    #         raise forms.ValidationError("Gotcha Bot")
    #     return botcatcher
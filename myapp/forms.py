from django import forms


class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)

class NameForm(forms.Form):
      your_name = forms.CharField(label='Your name', max_length=1



   def clean_message(self):
      username = self.cleaned_data.get("username")

      return username
   # dbuser =   .objects.filter(name=username)

   # if not dbuser:
   #    raise forms.ValidationError("User does not exist in our db!")



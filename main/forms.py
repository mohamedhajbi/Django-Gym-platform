from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from froala_editor.widgets import FroalaEditor
from . import models
class EnquiryForm(forms.ModelForm):
    class Meta:
        model=models.Enquiry
        fields=('full_name','email','detail')

class SignUp(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')      

class ProfileForm(forms.ModelForm):
			class Meta:
				model=User
				fields=('first_name','last_name','email','username')
				

class TrainerLoginForm(forms.ModelForm):
			pwd = forms.CharField(widget=forms.PasswordInput)
			
			class Meta:
				model=models.Trainer
				fields=('username','pwd')  


class TrainerProfileForm(forms.ModelForm):
	class Meta:
		model=models.Trainer
		fields=('full_name','mobile','adress','detail','img')     

class TrainerChangePassword(forms.Form):
	new_password=forms.CharField(max_length=50,required=True)


class ReportForTrainerForm(forms.ModelForm):
		model=models.TrainerSubscriberReport
		fields=('report_for_trainer','report_msg')


class TrainerTaskForm(forms.ModelForm):
	task = forms.CharField(widget=FroalaEditor)
	class Meta:
		model=models.TrainerTask
		fields=('user_ts','task',)
		widgets = {'trainer_ts': forms.HiddenInput()}    

class ReportForUserForm(forms.ModelForm):
	class Meta:
		model=models.TrainerSubscriberReport
		fields=('report_for_user','report_msg','report_from_trainer')
		widgets = {'report_from_trainer': forms.HiddenInput()}     


class ReportForTrainerForm(forms.ModelForm):
	class Meta:
		model=models.TrainerSubscriberReport
		fields=('report_for_trainer','report_msg','report_from_user')
		widgets = {'report_from_user': forms.HiddenInput()}            

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm

from django import forms

from .models import Perfil

class registroForm(UserCreationForm):
	
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(registroForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small></small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-black small"><li>Sua senha não deve conter dados pessoais.</li><li>Sua senha deve conter 8 caracteres ou mais.</li><li>Sua senha não pode conter apenas números.</ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirme sua senha'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small></small></span>'

class atualizarForm(UserChangeForm):

	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}), required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome'}), required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sobrenome'}), required=False)

	password = None

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(atualizarForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small></small></span>'

class senhaForm(SetPasswordForm):

	class Meta:

		model = User
		fields = ['nova_senha1', 'nova_senha2']

	def __init__(self, *args, **kwargs):
		super(senhaForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Nova senha'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-black small"><li>Sua senha não deve conter dados pessoais.</li><li>Sua senha deve conter 8 caracteres ou mais.</li><li>Sua senha não pode conter apenas números.</ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirme sua nova senha'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small></small></span>'

class infoForm(forms.ModelForm):

	celular = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Celular'}), required=False)

	endec1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço 1'}), required=False)
	endec2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço 2'}), required=False)

	cidade = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cidade'}), required=False)
	estado = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'}), required=False)
	cod_postal = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código Postal'}), required=False)

	class Meta:
		model = Perfil
		fields = ('celular', 'endec1', 'endec2', 'cidade', 'estado')	
from django import forms

from .models import EndecEnvio

class envioForm(forms.ModelForm):

    envio_nome_completo = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome completo'}), required=True)

    envio_endec1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço 1'}), required=True)
    envio_endec2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Endereço 2'}), required=True)
    
    envio_cidade = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cidade'}), required=True)
    envio_estado = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Estado'}), required=False)

    envio_cod_postal = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Código Postal'}), required=False)

    class Meta:

        model = EndecEnvio
        fields = ['envio_nome_completo', 'envio_endec1', 'envio_endec2', 'envio_cidade', 'envio_estado', 'envio_cod_postal']

        exclude = ['user', ]
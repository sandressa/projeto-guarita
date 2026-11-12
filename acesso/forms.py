from django import forms

class RegistroAcessoForm(forms.Form):
    qr_code_token = forms.CharField(label="Código do aluno", max_length=100, widget=forms.TextInput(attrs={"placeholder": "Digite ou leia o QR Code", "autofocus": True}))
    tipo = forms.ChoiceField(label="Tipo de acesso", choices=[('ENTRADA', 'Entrada'), ('SAIDA', 'Saida')])
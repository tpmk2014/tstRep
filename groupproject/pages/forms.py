from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label="Email", required=True)
    subject = forms.CharField(label="Temat", required=True)
    message = forms.CharField(label="Wiadomość", widget=forms.Textarea, required=True)
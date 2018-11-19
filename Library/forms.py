from django.forms import ModelForm
from Library.models import Book, Upload
from django import forms


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'description',)


class ContactForm(forms.Form):
    contact_name = forms.CharField()
    contact_email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"


class BookUploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('image',)

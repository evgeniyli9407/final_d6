from django import forms
from p_library.models import Author, Book
from django.forms import formset_factory




class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Author
        fields = '__all__'

AuthorFormSet = formset_factory(AuthorForm)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
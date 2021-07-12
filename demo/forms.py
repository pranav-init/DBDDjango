from django import forms
from .models import Nice, Note

class NiceForm(forms.ModelForm):
    class Meta():
        fields = '__all__'
        model = Note
        widgets = {
            'noteTitle': forms.TextInput(attrs = {
                'class': 'form-note-title', 'type': 'text',
            }),
            'noteContent': forms.Textarea(attrs = {
                'class': 'form-note-content', 'type': 'text',
            
            })  
        }
                            
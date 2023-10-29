from django.forms import ModelForm
from django import forms
from .models import Document

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = ['libelleDoc', 'description','categorie', 'typeDoc', 'docUpload']
        labels = {
            'libelleDoc': 'Titre du document',
            'description': 'Description',
            'categorie': 'Catégorie de document',
            'typeDoc': 'Type de document',
            'docUpload': 'Attacher le document'
        }

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
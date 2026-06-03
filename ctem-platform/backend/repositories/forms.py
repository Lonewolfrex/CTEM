from django import forms
from .models import Repository


class RepositoryForm(forms.ModelForm):

    class Meta:
        model = Repository

        fields = [
            "project",
            "name",
            "git_url",
            "default_branch",
            "is_active",
        ]

        widgets = {
            "project": forms.Select(
                attrs={"class": "form-control"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "git_url": forms.URLInput(
                attrs={"class": "form-control"}
            ),
            "default_branch": forms.TextInput(
                attrs={"class": "form-control"}
            ),
        }
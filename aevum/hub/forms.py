from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CodeSnippet, Event, FocusSession, Note, Profile, SharedLink, Tag, Task


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'full_name', 'course', 'year_level', 'phone', 'bio', 'portfolio_headline',
            'avatar', 'github_username', 'github_repo', 'github_branch', 'github_token'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
            'github_token': forms.PasswordInput(render_value=True),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'color']


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'attachment', 'is_pinned', 'is_public', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 12}),
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['tags'].queryset = Tag.objects.filter(user=user)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'color', 'is_public']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class CodeSnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        fields = ['title', 'language', 'content', 'code_file', 'is_public']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 14, 'placeholder': 'Paste your code here if you do not want to upload a file.'}),
        }


class FocusSessionForm(forms.ModelForm):
    class Meta:
        model = FocusSession
        fields = ['minutes', 'note']


class SharedLinkForm(forms.ModelForm):
    class Meta:
        model = SharedLink
        fields = ['target_type']

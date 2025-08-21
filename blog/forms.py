from django import forms
from .models import Post, Tag

class TagWidget(forms.TextInput):
    """Custom widget to enter comma-separated tags"""
    def format_value(self, value):
        if value and isinstance(value, (list, tuple, set)):
            return ", ".join([t.name for t in value])
        return value

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=TagWidget(attrs={'placeholder': 'Enter tags separated by commas'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        tag_names = [t.strip() for t in self.cleaned_data['tags'].split(",") if t.strip()]
        tag_objs = []
        for name in tag_names:
            tag_obj, _ = Tag.objects.get_or_create(name=name)
            tag_objs.append(tag_obj)
        instance.tags.set(tag_objs)
        return instance

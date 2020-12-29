import django_filters

from django import forms

from cloud_storage.apps.storage.models import File

TYPE_CHOICES = (
    ('Image', 'Image'),
    ('Audio', 'Audio'),
    ('Video', 'Video'),
    ('Document', 'Document'),
    ('Table', 'Table Sheet'),
    ('Presentation', 'Presentation'),
)


class FileFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label="", lookup_expr='icontains',
                                      widget=forms.TextInput(attrs={'autocomplete': 'off'}))
    type = django_filters.ChoiceFilter(label="", empty_label="All Types", choices=TYPE_CHOICES)
    uploaded_at = django_filters.OrderingFilter(
        choices=(
            ('-uploaded_at', 'Newest'),
            ('uploaded_at', 'Oldest'),
        ),

        label="",

        empty_label=None,
    )

    class Meta:
        model = File
        fields = ['title', 'type', 'uploaded_at']
        exclude = ['user', 'file']

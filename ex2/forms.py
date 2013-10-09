from django import forms


class SortingForm(forms.Form):
    input = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 2, 'autofocus': 'autofocus'}),
        initial='10, 2.5, 5, -2',
        help_text='Comma separated numbers',
    )
    output = forms.CharField(widget=forms.Textarea(attrs={'rows': 2,
                                                          'readonly': 'readonly'}))

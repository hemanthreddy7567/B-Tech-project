from django import forms


from manager.models import uploadmodel, viewdetailsmodel


class UploadnewsForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(), required=True, max_length=100)
    category = forms.ChoiceField(choices=[('',''),('International','International'),('Local','Local'),('Politics','Politics'),('Health','Health'),('Science','Science'),('Environtment','Environtment'),('Sport','Sport'),('Lifestyle','Lifestyle'),('Technology','Technology')])
    class Meta:
        model = uploadmodel
        fields = ('category','title','file','description','location')


class viewdetailsform(forms.ModelForm):
    category = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    title = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    #description = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    location = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True)
    # file = forms.FileField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=True, max_length=100)
    review = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)

    class Meta:
        model = viewdetailsmodel
        fields = ('category', 'title', 'description', 'description', 'location','review')
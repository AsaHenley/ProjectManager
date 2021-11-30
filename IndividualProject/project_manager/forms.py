from django import forms
from project_manager.models import Project, Task, BugReport, FeatureRequest

class CreateProject(forms.ModelForm):
    name = forms.CharField(required=False)
    details = forms.CharField(required=False)
    version = forms.CharField(required=False)
    class Meta:
        model = Project
        fields = ['name', 'details', 'version']

class CreateTask(forms.ModelForm):
    PRIORITY = (('high', 'high'),('med', 'med'), ('low', 'low'))
    name = forms.CharField(required=False)
    priority = forms.ChoiceField(choices=PRIORITY, required=False)
    class Meta:
        model = Task
        fields = ['name', 'priority']
    

class CreateBugReport(forms.ModelForm):
    name = forms.CharField(required=False)
    details = forms.CharField(required=False)
    class Meta:
        model = BugReport
        fields = ['name','details']

class CreateFeatureRequest(forms.ModelForm):
    name = forms.CharField(required=False)
    details = forms.CharField(required=False)
    class Meta:
        model = FeatureRequest
        fields = ['name','details']

class Search(forms.Form):
    sort_options = (
        ('name', 'Name'),
        ('date_created', 'Date Created'), 
        ('last_updated', 'Date Updated'),
    )
    search_result = forms.CharField(label='Search', required=False, max_length=100)
    sort = forms.ChoiceField(choices=sort_options, required=False, label='Sort By')
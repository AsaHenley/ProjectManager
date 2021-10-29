from django.contrib import admin
from .models import Project, BugReport, Task, FeatureRequest

admin.site.register(Project)
admin.site.register(BugReport)
admin.site.register(Task)
admin.site.register(FeatureRequest)

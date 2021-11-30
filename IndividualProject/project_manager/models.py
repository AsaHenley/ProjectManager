
from django.db import models
from django.contrib.auth.models import User
import datetime

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(CommonInfo):
    details = models.CharField(max_length=200, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    version = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Task(CommonInfo):
    PRIORITY = (('high', 'high'),('med', 'med'), ('low', 'low'))
    STATUS = (('in_progress', 'in_progress'), ('unstarted', 'unstarted'), ('finished', 'finished'))

    priority = models.CharField(max_length=20, choices=PRIORITY, default='low')
    status = models.CharField(max_length=20, choices=STATUS, default='unstarted')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class BugReport(CommonInfo):
    details = models.CharField(max_length=500, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name  

class FeatureRequest(CommonInfo):
    STATUS = (('unreviewed', 'unreviewed'), ('in_progress', 'in_progress'), ('finished', 'finished'), ('denied', 'denied'))

    details = models.CharField(max_length=500, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='unreviewed')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name      

from django.db import models
import datetime

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(CommonInfo):

    def __str__(self):
        return self.name

class Task(CommonInfo):
    PRIORITY = (('high', 'high'),('med', 'med'), ('low', 'low'))
    STATUS = (('in_progress', 'in_progress'), ('unstarted', 'unstarted'), ('finished', 'finished'))

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    priority = models.CharField(max_length=20, choices=PRIORITY, default='low')
    status = models.CharField(max_length=20, choices=STATUS, default='unstarted')
    estimated_time = models.TimeField()

    def __str__(self):
        return self.name

class BugReport(CommonInfo):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.name  

class FeatureRequest(CommonInfo):
    STATUS = (('unreviewed', 'unreviewed'), ('in_progress', 'in_progress'), ('finished', 'finished'), ('denied', 'denied'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='unreviewed')
    

    def __str__(self):
        return self.name      
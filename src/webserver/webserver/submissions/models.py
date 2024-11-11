from django.db import models
from .utils import validate_file_extension

# Create your models here.
class SubmissionStatus(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Submission(models.Model):
    # todo. I don't want this to be nullable
    # maybe there is a way to setup an "error" status
    # and make that default, but im not sure how to preload
    # data into the submissionstatus model yet
    status = models.ForeignKey(SubmissionStatus, null=True, on_delete=models.SET_NULL)
    file = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    result = models.TextField(blank=True)
    submitted_at = models.DateTimeField(null=True) #null for now. Giving me issues
    completed_at = models.DateTimeField(null=True)
    result = models.TextField(max_length=1024)
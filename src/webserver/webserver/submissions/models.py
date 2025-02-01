from django.db import models
from django.contrib.auth import get_user_model
from .utils import validate_file_extension

# Create your models here.
class SubmissionStatus(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

User = get_user_model()

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
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    model_name = models.TextField(blank=True)
    weighted_error = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t1_all_cells = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t2_blind_cells = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t3_non_blinded_cells = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t4_charging = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t5_80kg_payload = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t5_6_448kg_payload_with_HVAC = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t5_6_448kg_payload = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t5_1000kg_payload = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t7_standard_cycles = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t8_custom_cycles = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t9_n20C = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t9_n10C = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t9_0C = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t9_10C = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t9_25C = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t9_40C = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t10_iSOC_error = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    t11_current_sensor_error = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    all_drive_cycles_average_RMSE = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    all_drive_cycles_average_MAE = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    all_drive_cycles_average_MAXE = models.DecimalField(max_digits=10, decimal_places=3, null=True)

import time
import os
import tempfile
import shutil
import csv
import matlab.engine

from django.utils import timezone
from django.conf import settings
from workers import task
from .models import Submission, SubmissionStatus


def setup_dir(submission_id: str, dir_path: os.PathLike):

    # copy user submission to temp directory
    s: Submission = Submission.objects.get(id=submission_id)
    submission_file_path = s.file.path


    # the file name might not be model, as files with
    # name collisions get renamed, so we should name it model
    # when we copy it
    # /var/tmp_dir12345/model.m
    dst_path = os.path.join(dir_path, 'Model.m')
    shutil.copy(submission_file_path, dst_path)
    print(f"Copied static file: {submission_file_path} to {dst_path}")


    # copy source files and data files

    static_files_path = os.path.join(settings.BASE_DIR, "mlSource", "defaultShort")
    shutil.copytree(static_files_path, dir_path, dirs_exist_ok=True)


def create_settings_csv(out_dir: os.PathLike):
    # get these from submission
    auth_name="test name"
    auth_affiliation="test affiliation"
    auth_email="test email"
    model_name="test model name"

    data = [
        ["Author Name", auth_name],
        ["Author Affiliation", auth_affiliation],
        ["Author Email", auth_email],
        ["Model Name", model_name]
    ]

    with open(os.path.join(out_dir, "Settings.csv"), mode="w", newline="") as file:
         writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
         writer.writerows(data)

@task()
def run_submission(submission_id):
    # first create new dir
    # call setup_dir funciton
    # run model
    # save leaderboard data from csv, store in database
    # store result figures in permenant location
    # let temp dir cleanup

    with tempfile.TemporaryDirectory() as temp_dir:

        print(f"Running submission {submission_id}")
        print(f"temp dir : {temp_dir}")

        setup_dir(submission_id, temp_dir)
        create_settings_csv(temp_dir)
        
        s: Submission = Submission.objects.get(id=submission_id)


        # check how to silence warnings

        try:
            eng = matlab.engine.start_matlab()
            eng.set(eng.groot(), 'DefaultFigureVisible', 'off', nargout=0)


            eng.cd(temp_dir, nargout=0)
            eng.eval("try\nMain_SET;\ncatch e\nfprintf('Error: %s\\n', e.message);\nend", nargout=0)


            print("matlab completed executing")

            # store leaderboard results

            with open(os.path.join(temp_dir, "Leaderboard_entry.csv"), newline='') as f:
                reader = csv.reader(f)
                results_list = list(reader)[1]

                print("****** RESULTS_LIST *****")
                print(results_list)

                s.model_name                    = results_list[3]
                s.weighted_error                = results_list[4]
                s.t1_all_cells                  = results_list[5]
                s.t2_blind_cells                = results_list[6]
                s.t3_non_blinded_cells          = results_list[7]
                s.t4_charging                   = results_list[8]
                s.t5_80kg_payload               = results_list[9]
                s.t5_6_448kg_payload_with_HVAC  = results_list[10]
                s.t5_6_448kg_payload            = results_list[11]
                s.t5_1000kg_payload             = results_list[12]
                s.t7_standard_cycles            = results_list[13]
                s.t8_custom_cycles              = results_list[14]
                s.t9_n20C                       = results_list[15]
                s.t9_n10C                       = results_list[16]
                s.t9_0C                         = results_list[17]
                s.t9_10C                        = results_list[18]
                s.t9_25C                        = results_list[19]
                s.t9_40C                        = results_list[20]
                s.t10_iSOC_error                = results_list[21]
                s.t11_current_sensor_error      = results_list[22]
                s.all_drive_cycles_average_RMSE = results_list[23]
                s.all_drive_cycles_average_MAE  = results_list[24]
                s.all_drive_cycles_average_MAXE = results_list[25]

            s.status = SubmissionStatus.objects.get(name="completed")
            s.completed_at = timezone.now()


            # store files

        except Exception as e:
            print(f"Error in MATLAB execution: {e}")
            s.status = SubmissionStatus.objects.get(name="failed")
            
        finally:
            # Ensure the MATLAB engine quits even if there was an error
            eng.quit()

        s.save()
    
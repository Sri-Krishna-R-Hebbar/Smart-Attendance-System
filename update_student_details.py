import os
import pandas as pd

training_image_path = "D:\\Attendance\\TrainingImage"

studentdetail_path = "D:\\Attendance\\StudentDetails\\studentdetails.csv"

def extract_student_details(training_image_path):
    student_details = []
    for folder_name in os.listdir(training_image_path):
        if os.path.isdir(os.path.join(training_image_path, folder_name)):
            enrollment_number, name = folder_name.split("_", 1)
            student_details.append({'Enrollment': enrollment_number, 'Name': name})
    return pd.DataFrame(student_details)

def save_student_details_to_csv(student_details):
    student_details.to_csv(studentdetail_path, index=False)

student_details = extract_student_details(training_image_path)

save_student_details_to_csv(student_details)

import pandas
from fastapi import UploadFile


class CSVReader:
    THRESHOLD_CLASSIFICATION = 0.42

    PROPERTY_MAP = {
        'Age': 'age',
        'Cholesterol': 'cholesterol',
        'Heart rate': 'heart_rate',
        'Diabetes': 'diabetes',
        'Family History': 'family_history',
        'Smoking': 'smoking',
        'Obesity': 'obesity',
        'Alcohol Consumption': 'alcohol_consumption',
        'Exercise Hours Per Week': 'exercise_hours_per_week',
        'Diet': 'diet',
        'Previous Heart Problems': 'previous_heart_problems',
        'Medication Use': 'medication_use',
        'Stress Level': 'stress_level',
        'Sedentary Hours Per Day': 'sedentary_hours_per_day',
        'Income': 'income',
        'BMI': 'bmi',
        'Triglycerides': 'triglycerides',
        'Physical Activity Days Per Week': 'physical_activity_days_per_week',
        'Sleep Hours Per Day': 'sleep_hours_per_day',
        'Blood sugar': 'blood_sugar',
        'CK-MB': 'ck_mb',
        'Troponin': 'troponin',
        'Gender': 'gender',
        'Systolic blood pressure': 'systolic_blood_pressure',
        'Diastolic blood pressure': 'diastolic_blood_pressure',
        'Unnamed: 0': 'unnamed'
    }

    USEFUL_COLUMN_NAMES = [
        'age',
        'cholesterol',
        'heart_rate',
        'exercise_hours_per_week',
        'stress_level',
        'sedentary_hours_per_day',
        'bmi',
        'triglycerides',
        'physical_activity_days_per_week',
        'sleep_hours_per_day',
        'blood_sugar',
        'systolic_blood_pressure',
        'diastolic_blood_pressure',

        'diabetes',
        'family_history',
        'id',
    ]


    def __init__(self, file: UploadFile):
        super().__init__()
        self._file = file.file
        self.df: pandas.DataFrame
        self.transform_file_to_data_frame()


    def transform_file_to_data_frame(self):
        self.df = pandas.read_csv(self._file)
        self.df = self.df.rename(columns=self.PROPERTY_MAP)

        selecting_column_names = self.get_useful_column_names()
        self.df = self.df[selecting_column_names]


    def get_useful_column_names(self) -> list[str]:
        dropping_column_names = []
        for column_name in self.USEFUL_COLUMN_NAMES:
            if self.df.get(column_name) is not None:
                dropping_column_names.append(column_name)
        return dropping_column_names

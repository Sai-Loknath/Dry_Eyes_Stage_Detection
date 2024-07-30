import pandas as pd
import pandas as pd
from pymongo import MongoClient
dataset = pd.read_csv('original_dataset.csv')
def load_original_data_to_database(file_path):
    df = pd.read_csv(file_path)
    data = df.to_dict(orient='records')
    client = MongoClient("mongodb://localhost:27017/")
    db = client.Dry_Eyes_Detection
    original_data_collection = db.original_data
    original_data_collection.insert_many(data)
    print("Original data loaded successfully.")
load_original_data_to_database(r'C:\Users\Lenovo\Desktop\DRY_EYES_STAGE_DETECTION\datasets\original_dataset.csv')



columns_to_convert = ['Gender', 'How many hours in a day do you spend on your smartphones, laptops, etc?',
                      'Eyes that are sensitive to light?', 'Eyes that feel gritty (itchy and Scratchy) ?',
                      'Painful or Sore eyes?', 'Blurred vision?', 'Poor Vision?', 'Reading?',
                      'Driving at night?', 'Working with a computer or bank machine ATM?', 'Watching TV?',
                      'Windy conditions?', 'Places or areas with low humidity (very dry)?', 'Areas that are air-conditioned?',
                      'Results']

for column in columns_to_convert:
    mapping_dict = {text_value: index for index,
                    text_value in enumerate(dataset[column].unique())}
    dataset[column] = dataset[column].replace(mapping_dict)

columns_to_drop = ['Timestamp', 'Consent', 'Academic Year',
                   'What type of Digital display device do you use?', 'OSDI', 'Unnamed: 21',
                   'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25',
                   'Unnamed: 26', 'Unnamed: 27']
dataset.drop(columns=columns_to_drop, axis=1, inplace=True)
dataset.to_csv('preprocessed_dataset.csv', index=False)
pd.set_option('future.no_silent_downcasting', True)


def load_original_data_to_database(file_path):
    df = pd.read_csv(file_path)
    data = df.to_dict(orient='records')
    client = MongoClient("mongodb://localhost:27017/")
    db = client.Dry_Eyes_Detection
    preprocessed_data_collection = db.preprocessed_data
    preprocessed_data_collection.insert_many(data)
    print("preprocessed data loaded successfully.")
load_original_data_to_database(r"C:\Users\Lenovo\Desktop\VJIT\Projects\Dry_eyes_detection_project\datasets\preprocessed_dataset.csv")
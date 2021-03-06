import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return __model.predict([x])[0]

def get_location_names():
    return __locations

# from 15 index
def load_saved_artifacts():
    print("Loading saved artifacts........start")
    global __data_columns
    global __locations
    global __model

    with open("./static/artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']  ## will contains all columns
        __locations = __data_columns[15:]  ## will contains all location columns

    with open("./static/artifacts/mumbai_price_prediction_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artificats...Done")

if(__name__ == '__main__'):
    load_saved_artifacts()
    print(get_location_names())
    price_1 = get_estimated_price('beturkar pada', 1000, 3)
    print(round(price_1[0], 4))
    print(round(price_1[1], 4))
    price_2 = get_estimated_price('beturkar pada', 1000, 2)
    print(round(price_2[0], 4))
    print(round(price_2[1], 4))
    price_3 = get_estimated_price('Malad East', 1000, 2)
    print(round(price_3[0], 4))
    print(round(price_3[1], 4))

import os
import pandas as pd

# The file allows me to run the Calorie Mama API on food images in a main directory and sub directories. Additionally, it stores the output I want in an excel sheet.

# Gathering all required data
food = {'Restaurant_index': ["yre",2],
        'Image_index': [1, 2],
        'Image_source': [1,2],
        'name': [5,6],
        'food_id': [0,0],
        'group': [6,66],
        'Score': [9,45
        ],
        'totalCarbs': [8,15],
        'totalFat': [5,55],
        'protein': [7,8
        ],
        'calories': [556,7],
        'serving_small': [3,4],
        'serving_medium':[2.33 ,4],
        'serving_large':[0.023,3],
        'serving_kids':[344,5],
        'serving_100g':[3,22],
        'serving_1g':[100,1],
        'serving_1oz':[3983,2],
        'other_nutrients':[3,66]
        }


# Putting all data into a dataframe
df = pd.DataFrame(food, columns = ['Restaurant_index','Image_index','Image_source', 'name', 'food_id', 'group', 'Score','totalCarbs','totalFat',
        'protein',
        'calories',
        'other_nutrients',
        'serving_small',
        'serving_medium',
        'serving_large',
        'serving_kids',
        'serving_100g',
        'serving_1g',
        'serving_1oz'])
print(df)

#df.to_excel (r'D:\Food Image Classification Research\export_dataframe.xlsx', index = False, header=True)
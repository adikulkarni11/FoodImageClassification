# Imports 
import os
import pandas as pd
import subprocess
import sys
from subprocess import PIPE, run, Popen
import json
import sys
import pathlib
import urllib.request
import PIL.Image
from PIL import Image
import cv2
import numpy as np

#Calorie Mama API Key
key = "YOUR KEY HERE"
#JSON TO Python manual converts
true = True
false = False
null = None

# The file allows me to run the Calorie Mama API on food images in a main directory and sub directories. Additionally, it stores the output I want in an excel sheet.

# Constructing Dataframe to store all values
df = pd.DataFrame( columns = ['Restaurant_index', 'Image_index', 'Image_source', 'name', 'food_id', 'group',
                               'Score', 'totalCarbs', 'totalFat', 'protein', 'calories', 'other_nutrients',
                                'serving_small', 'serving_medium', 'serving_large', 'serving_kids', 'serving_100g', 'serving_1g', 'serving_1oz', 'serving_1_serving','serving_cup',
                                 'serving_burger'])

""" We will insert all values as Pd.Series' into the dataframe, which will later be converted to an excel file """

### Creating Pipeline of images to feed to API ###



# Calling the Calorie Mama API

directory = r'D:\Food Image Classification Research\Images Generated\TEST'    # Main directory that includes images. Can be a directory of directories.

imgNum = 0
for root, dirs, files in os.walk(directory):
    for name in files:
        if name.endswith((".jpg")):  # I'm looking for all images (JPEG) in the main directory and sub folders
            imgNum += 1
            print("Image=", name)
            print("folderNum=",root[60:61])
            
            #print(os.path.join(root, name)) 
            #print(os.getcwd())
            #print("root", root)
            os.chdir(root)
            #print("chdir=",os.getcwd())

            result = os.popen("curl -H -i -F media=@"+name+" https://api-2445582032290.production.gw.apicast.io/v1/foodrecognition?user_key="+key).read()
            #print(result)    # Output of curl command. It is a string output need to convert back into JSON
            result_dict = json.loads(result)
            #print(result_dict)

            res = result_dict['results'] # res = number of foods the image has
            #print(len(res),'\n')
            #print(result_dict['results'])

            """ For Complex Images, CalorieMama recognizes that there are multiple things. We need to take that into account."""
            """ Each item here is the guess """

            for item in range(len(result_dict['results'])):
                    #print("item num = ",item)
                    #For each food item, CalorieMama gives its many foods that it thinks it is. We are only considering the first one (highest probability)
                    bestGuess = res[item]['items'][0]
                    ValItemIndex = item
                    ValGroup = res[item]['group']
                    #print("My best guess for this food item is", bestGuess['name'])
                    ValName = bestGuess['name']
                    print("ValName = ",ValName)
                    ValScore = bestGuess['score']
                    ValFoodId = bestGuess['food_id']
                    try:
                      ValTotalCarbs = bestGuess['nutrition']['totalCarbs']
                    except:
                      ValTotalCarbs = 'NA'
                    try:
                      ValTotalFat = bestGuess['nutrition']['totalFat']
                    except:
                      ValTotalFat = 'NA'
                    try:
                      ValProtein = bestGuess['nutrition']['protein']
                    except:
                      ValProtein = 'NA'
                    try:
                      ValCalories = bestGuess['nutrition']['calories']
                    except:
                      ValCalories = 'NA'
                    ValOtherNutrients = 'NA'
                    # Serving sizes in Calorie Mama is a little confusing
                    #print(bestGuess['servingSizes'][0])
                    #print('There are these many serving sizes: ', len(bestGuess['servingSizes']))
                    #print("bestGuess type=", type(bestGuess['servingSizes']))
                    print("bg===",bestGuess['servingSizes'])
                    valServingSmall = valServingMedium = valServingLarge = valServingKids = valServing100g = valServing1g = valServing1oz = val1Serving = valServingCup = valBurger = 'NA'

                    for j in bestGuess['servingSizes']:
                            print("j: ",j)
                            #print(type(j))
                            #print("j is a: ",j['unit']," j serving size is : ",j['servingWeight'])
                            #print(j['unit'])

                            if 'servingWeight' in j:
                              if j['unit'] == '1 serving':
                                      val1Serving = j['servingWeight']
                              else:
                                      pass
                          
                              if j['unit'] == '100 g':
                                      valServing100g = j['servingWeight']
                              else:
                                      pass

                              if j['unit'] == '1 g':
                                      valServing1g = j['servingWeight']
                              else:
                                      pass
                              if j['unit'] == '1 oz':
                                      valServing1oz = j['servingWeight']
                              else:
                                      pass
                              
                              if j['unit'] == '1 serving, large':
                                      valServingLarge = j['servingWeight']
                              else:
                                      pass
                              
                              if j['unit'] == '1 serving, kids':
                                      valServingKids = j['servingWeight']
                              else:
                                      pass

                              if j['unit'] == '1 cup':
                                      valServingCup = j['servingWeight']
                              else:
                                      pass
                              
                              if j['unit'] == '1 serving, medium':
                                      valServingMedium = j['servingWeight']
                              else:
                                      pass
                              
                              if j['unit'] == '1 serving, small':
                                      valServingSmall = j['servingWeight']
                              else:
                                      pass
                              
                              if j['unit'] == '1 burger':
                                      valBurger = j['servingWeight']
                              else:
                                      pass
                            else:
                              val1Serving = '1 unit'

                                  
                    print("df.index", len(df.index))
                    print('Group: ',ValGroup,'Name: ',ValName,' Cal:',ValCalories, 'Protein:' , ValProtein)
                    print("100 bands= " ,valServing100g)
                    image_index = name[:-12]
                    folderNum = root[60:61]
                    image_Source = 'Test'
                    servList = [valServingSmall, valServingMedium, valServingLarge, valServingKids, valServing100g, valServing1g, valServing1oz, val1Serving, valServingCup, valBurger]
                    print("small= ",valServingSmall, "medium = ", valServingMedium, "large= ", valServingLarge, "kids=" , valServingKids, "100g= ",valServing100g, "1g= ", valServing1g, "1oz =", valServing1oz, "1 serving",  val1Serving, "cup = ", valServingCup, " burger= ", valBurger)
                    """ Columns: [Restaurant_index, Image_index, Image_source, name, food_id, group, Score, totalCarbs, totalFat, protein, calories, other_nutrients, serving_small, serving_medium, serving_large, serving_kids, serving_100g, serving_1g, serving_1oz, serving_1_serving, serving_cup, serving_burger] """ 
                    # Gathering all required data and storing into dataframe using loc
                    df.loc[len(df.index)] = [ folderNum, image_index, image_Source, ValName, ValFoodId, ValGroup, ValScore, ValTotalCarbs, ValTotalFat, ValProtein, ValCalories, ValOtherNutrients, valServingSmall,
                                               valServingMedium, valServingLarge, valServingKids, valServing100g, valServing1g, valServing1oz, val1Serving, valServingCup, valBurger]
                    #print(df)

                    

print("imgNum",imgNum)
print("boom",len(df.index))
df.to_excel (r'D:\Food Image Classification Research\export_dataframe.xlsx', index = False, header=True)

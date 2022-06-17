#!/usr/bin/env python
# coding: utf-8

# In[196]:


# Standard Libraries 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix

# To read in csv file
microphone_results = pd.read_csv("audioResultsMicrophone.csv")

# ***Lists required to manipulate and format the data***
incorrect_letters_list = ["B", "C", "D", "E", "G", "P", "T", "V", "Z", "3"]
incorrect_original_characters_list = []
incorrect_feedback_characters_list = []
incorrect_feedback_characters_total_list = []
incorrect_original_characters_total_list = []
average_score_list_each_device = []

# Add brackets within average_score_list_all_tests that are separated by comma
average_score_list_all_tests = [[],[],[],[],[],[]]

# Add more device names if there are more devices
device_names = ["Poly X30", "Neat A20", "Jabra PanaCast 50", "Logitech Rally Bar", "Yealink MeetingBar A20", "Yealink MeetingBar A30"]

# Add more zeroes if there are more letters
incorrect_feedback_count_list = [0,0,0,0,0,0,0,0,0,0]
incorrect_original_count_list = [0,0,0,0,0,0,0,0,0,0]

# Goes through each row and compares original characters with feedback characters
i = 0
for i, row in microphone_results.iterrows():
    for char_count in range(20): # Increase range(n) by 2 if one new test is added
        if row[3][char_count] != row[4][char_count]:
            incorrect_feedback_characters_list.append(row[4][char_count])
            incorrect_feedback_characters_total_list.append(row[4][char_count])
            incorrect_original_characters_list.append(row[3][char_count])
            incorrect_original_characters_total_list.append(row[3][char_count])
    microphone_results[' Incorrect Original Characters'][i] = ', '.join(incorrect_original_characters_list)
    microphone_results[' Incorrect Feedback Characters'][i] = ', '.join(incorrect_feedback_characters_list)
    i += 1
    incorrect_original_characters_list.clear()
    incorrect_feedback_characters_list.clear()
    
    # Add more else-if statements if more devices are added
    if row[0] == device_names[0]:
        average_score_list_all_tests[0].append(row[5])
    elif row[0] == device_names[1]:
        average_score_list_all_tests[1].append(row[5])
    elif row[0] == device_names[2]:
        average_score_list_all_tests[2].append(row[5])
    elif row[0] == device_names[3]:
        average_score_list_all_tests[3].append(row[5])
    elif row[0] == device_names[4]:
        average_score_list_all_tests[4].append(row[5])
    elif row[0] == device_names[5]:
        average_score_list_all_tests[5].append(row[5])
    

display(microphone_results) # Displays nicely formatted table

# Goes through each test (A1, A2, A3, B1...) and creates score average for each device
for device in average_score_list_all_tests:
    average = 0
    for test in device:
        average += test
    average /= len(device)
    average_score_list_each_device.append(average)

# Plots and displays averages
plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15,10)
plt.bar(device_names, average_score_list_each_device, color = ['red', 'orange', 'green', 'blue', 'grey', 'black']) # Add more colors if adding devices
plt.title("Video Conferencing Devices- Audio Comparison")
plt.xlabel("Devices")
plt.ylabel("Average Accuracy Score")
plt.show()

# Point system to calculate an individual letter's error/incorrect score
for letter in incorrect_feedback_characters_total_list:
    if letter == "B":
        incorrect_feedback_count_list[0] += 1
    elif letter == "C":
        incorrect_feedback_count_list[1] += 1
    elif letter == "D":
        incorrect_feedback_count_list[2] += 1
    elif letter == "E":
        incorrect_feedback_count_list[3] += 1
    elif letter == "G":
        incorrect_feedback_count_list[4] += 1
    elif letter == "P":
        incorrect_feedback_count_list[5] += 1
    elif letter == "T":
        incorrect_feedback_count_list[6] += 1
    elif letter == "V":
        incorrect_feedback_count_list[7] += 1
    elif letter == "Z":
        incorrect_feedback_count_list[8] += 1
    else:
        incorrect_count_list[9] += 1
for letter in incorrect_original_characters_total_list:
    if letter == "B":
        incorrect_original_count_list[0] += 1
    elif letter == "C":
        incorrect_original_count_list[1] += 1
    elif letter == "D":
        incorrect_original_count_list[2] += 1
    elif letter == "E":
        incorrect_original_count_list[3] += 1
    elif letter == "G":
        incorrect_original_count_list[4] += 1
    elif letter == "P":
        incorrect_original_count_list[5] += 1
    elif letter == "T":
        incorrect_original_count_list[6] += 1
    elif letter == "V":
        incorrect_original_count_list[7] += 1
    elif letter == "Z":
        incorrect_original_count_list[8] += 1
    else:
        incorrect_original_count_list[9] += 1


# In[194]:


# Plots out frequency of incorrect original letters
plt.style.use("ggplot")
plt.bar(incorrect_letters_list, incorrect_original_count_list)
plt.title("Frequency of Incorrect Original Letters")
plt.xlabel("Incorrect Words")
plt.ylabel("Frequency")
plt.show()


# In[195]:


# Plots out frequency of incorrect feedback letters
plt.style.use("ggplot")
plt.bar(incorrect_letters_list, incorrect_feedback_count_list)
plt.title("Frequency of Incorrect Feedback Letters")
plt.xlabel("Incorrect Words")
plt.ylabel("Frequency")
plt.show()


# In[ ]:


# Plots a confusion matrix to compare the mixture of incorrect original and incorrect feedback characters.
# Darker box indicates that the combination of original and feedback characters is often mixed up for one another.
cf_matrix = confusion_matrix(y_test, y_pred)
ax = sns.heatmap(cf_matrix, annot=True, cmap='Blues')

ax.set_title('Seaborn Confusion Matrix with labels\n\n');
ax.set_xlabel('\nFeedback Characters')
ax.set_ylabel('Original Characters ');

## Ticket labels
ax.xaxis.set_ticklabels(incorrect_letters_list)
ax.yaxis.set_ticklabels(incorrect_letters_list)

## Display the visualization of the Confusion Matrix.
plt.show()


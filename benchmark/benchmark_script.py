#!/usr/bin/env python
# coding: utf-8

# In[1]:

import sys
import pandas as pd
import pickle

def calculate_benchmark(marks_input, marks_initial_input):
    
    with open(marks_input, 'rb') as f:
    	marks = pickle.load(f)
    with open(marks_initial_input, 'rb') as f:
    	marks_initial = pickle.load(f)
    
    score = 0

    for user_id in marks.keys():
        for (movie_id, prediction) in marks.get(user_id):
            if user_id in marks_initial.keys():
                if (movie_id, 4) in marks_initial.get(user_id) \
                    or (movie_id, 5) in marks_initial.get(user_id):
                    if prediction == 1:
                        score += 1 / len(marks.get(user_id))
                        continue
                    else:
                        score -= 1 / len(marks.get(user_id))
                        continue
                if (movie_id, 1) in marks_initial.get(user_id) \
                    or (movie_id, 2) in marks_initial.get(user_id) \
                    or (movie_id, 3) in marks_initial.get(user_id):
                    if prediction == 0:
                        score += 1 / len(marks.get(user_id))
                    else:
                        score -= 1 / len(marks.get(user_id))

    return score/len(marks.keys())
    
args = sys.argv    

print("Your benchmark value: ", calculate_benchmark(args[1], args[2]))


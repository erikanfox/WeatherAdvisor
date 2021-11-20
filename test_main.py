import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from fastapi import FastAPI
import uvicorn
import random
import numpy as np
from main import predictOutfit
from main import getMessage


temp=random.randint(0, 100)
rain=random.randint(0, 1)
snow=random.randint(0, 1)
y=predictOutfit(temp,rain,snow)
assert isinstance(y[0], np.int64)
message= getMessage(y[0],rain,snow)
assert "shirt" in message

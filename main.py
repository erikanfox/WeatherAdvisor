import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from fastapi import FastAPI
import uvicorn

data = pd.read_csv("clothing_weather.csv")
data

app = FastAPI()

@app.get("/")
async def root():
    """Weather Advisor Welcome"""
    return {"message": "Hello, welcome to Weather advisor! Enter a temp, whether there is a chance of rain, and whether there is a chance of snow in the format temp/rain/snow."}

@app.get("/weatheradvisor/{temp}/{rain}/{snow}")
async def weatheradvisor(temp: int,rain:int,snow:int):
    y=predict(temp,rain,snow)
    message=getMessage(y[0], rain, snow)
    return "You should wear {0}".format(message)
    
async def predict(temp: int,rain:int,snow:int): 
    data["rain"] = data["rain"].replace("no", 0)
    data["rain"] = data["rain"].replace("yes", 1)
    data["snow"] = data["rain"].replace("no", 0)
    data["snow"] = data["rain"].replace("yes", 1)

    feature_cols = ['temp_f','rain','snow']
    X = data[feature_cols] # Features
    y = data.overall # Target variabley

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    clf = DecisionTreeClassifier(criterion="entropy", max_depth=4)

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    y_pred = clf.predict([temp,rain,snow])
    #print the predicted outfit code
    return y_pred
    
def getMessage(pred, rain, snow):
    ans=""
    outfit_code = {
        1: "a short sleeve shirt and shorts.",
        2: "a short sleeve shirt and long pants.",
        3: "a short sleeve shirt, shorts and a light jacket or sweatshirt.",
        4: "a short sleeve shirt, long pants, and a light jacket or sweatshirt.",
        5: "a long sleeve shirt, long pants, and a light jacket or sweatshirt.",
        6: "a short sleeve shirt, long pants, and a heavy jacket.",
        7: "a long sleeve shirt or sweater, long pants, and a heavy jacket.",
        8: "a long sleeve shirt and shorts."
    }

    if pred in outfit_code:
        ans=ans+outfit_code[pred]
    else:
        return "an error occurred"
    
    if rain == 1:
        ans=ans+ " You may also want a rain jacket, rain boots, and/or an umbrella."

    if snow == 1:
        ans=ans+ " You should also bring a scarf, gloves, and snow boots!"
    
    return ans
   
if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')

# Weather Advisor

Do you every wonder what the whether is like when picking out clothes? With our app this will never happen again!
![Word Cloud](/Images/Text.png)

## Introduction
In the mornings it can often be challenging to decide what to wear. There are so many different combinations of clothing to choose from to create your outfit for the day. With our service this is all done for you! Our app takes in the temperature along with whether there is a chance of rain or snow to generate an outfir for the user to wear. The app deploys an outfit predictor deciscion tree using a Flask app. The app is deployed using AWS and uses continous delivery using AWS App Runner.

## Project Outline
The service uses a decision tree to generate the outfit advised from a data set we generated. The data is generated based off of outfits that we have worn in different types of weather. It is stored both locally, as well as, in github. Continous delivery is constantly being run and the service is deployed using AWS.

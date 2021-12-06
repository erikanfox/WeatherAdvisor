[![Python 3.8](https://github.com/erikanfox/WeatherAdvisor/actions/workflows/main.yml/badge.svg)](https://github.com/erikanfox/WeatherAdvisor/actions/workflows/main.yml)

# Weather Advisor

Do you every wonder what the whether is like when picking out clothes? With our app this will never happen again!
![Word Cloud](/Images/Text.png)

## Introduction
In the mornings it can often be challenging to decide what to wear. There are so many different combinations of clothing to choose from to create your outfit for the day. With our service this is all done for you! Our app takes in the temperature along with whether there is a chance of rain or snow to generate an outfit for the user to wear. The app deploys an outfit predictor deciscion tree using Fast API. The app is deployed using AWS and uses continous delivery using AWS App Runner.

## Project Outline
The service uses a decision tree to generate the outfit advised from a data set we generated. The data is generated based off of outfits that we have worn in different types of weather. It is stored both locally, as well as, in github. Continous delivery is being performed on the application using AWS App Runner, while continuous integration runs using GitHub Actions.
![Word Cloud](/Images/Flowchart.png)

## How it Works
Our app works by entering the URL below and adding the termperature (in F), whether there is a chance of rain, and whether there is a chance of snow. The temperature is entered as an integer, while the chances of rain or snow is entered as either 0 (for no) or 1 (for yes). The following is an example URL to produce recommended clothing for when it is 60 F, there is a chance of rain, and no chance of snow.

https://mi6q9vhkh7.us-east-2.awsapprunner.com/weatheradvisor/60/1/0

Using the following URL to use the Clothing Recommender App:

https://mi6q9vhkh7.us-east-2.awsapprunner.com/weatheradvisor/Temperature/Chance_of_Rain?/Chance_of_Snow?

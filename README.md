Purpose
-------

This project is for personal improvement and satisfaction. The most
difficult step for (most) data scientists is model deployment. Flask
makes that easy enough with their slick Python library. In this project,
we train a model with lightgbm and create an app that will predict a
house selling price from the following columns:

-   LotArea
-   Neighborhood
-   Condition1
-   Condition2
-   OverallQual
-   OverallCond
-   YearBuilt
-   SaleCondition

There are hundreds (maybe thousands) of kernels on Kaggle that show you
how to train a model that can predict housing prices on this exact
dataset. However, none of them actually deploy the model so that one
could query it and recieve a prediction. That is what this project does.
It is a work in progress, and will be improved upon as I find new
features to add.

The requirements.txt file is pretty lightweight, and only includes the
packages needed for this specific project (plus base Python) so feel
free to copy the environment.

Usage
-----

The web service can receive 3 valid commands:

### POST with json body

The post to the web service should include a body with the following
json schema:

    {
      "LotArea": Integer,
      "Neighborhood": String,
      "Condition1": String,
      "Condition2": String,
      "OverallQual": Integer,
      "OverallCond": Integer,
      "YearBuilt": Integer,
      "SaleCondition": String
    }

This json represends ‘samples’ which we would like to predict. For
example, the following payload:

    {
      "LotArea": 9600,
      "Neighborhood": "Veenker",
      "Condition1": "Feedr",
      "Condition2": "Norm",
      "OverallQual": 6,
      "OverallCond": 8,
      "YearBuilt": 1976,
      "SaleCondition": "Normal"
    }

Will return:

    {
      "SalePrice": 186272.93
    }

### Shutdown

Simply send a GET request to the path /shutdown to shut the app down
gracefully.

### GET

Send a GET request to the root path to recieve a refreshable key. Used
for debugging.

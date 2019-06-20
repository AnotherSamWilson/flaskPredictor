Purpose
-------

This project is for personal improvement and satisfaction. The most
difficult step for (most) data scientists is model deployment. Flask
makes that easy enough with their slick Python library.

You will find two folders. One is for scripts, the other is for
logs/object storage.

The dataset used for prediction is the House Prices dataset you can find
on Kaggle.

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

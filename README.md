# Trading Data Science
This repository does not aim to find best model for particular trading problem (portfolio selection, stock price prediction, etc.) but to illustrate how you can analyze and model this problems. **It requieres you to have previous knowledge in this methods**, since we are not explaining them deeply, this repo just illustrate how to conduct them in python and how you can use it in a finance enviroment.

## Data
You can run the notebooks by downloading the following stocks historical information and having **conda** installed, pmdarima https://github.com/alkaline-ml/pmdarima, pulp, pytorch and Keras (or please install all the necessary libraries from conda):
* Facebook
* Tesla
* Disney
* Kimberly Clark.

All stocks use information from year 2000 all the way to 11th of December 2020.<br>
You will need **alphavantage API** token to download all SP500 stocks from the portfolio_creation notebook. For the reinforcement learning enviroment data was downloaded from **Yahoo Finance from 2014 to December the 30th 2020**.

## Structure
I suggest the following order of study (visualization):
* EDA_example
* time_series_analysis
* portfolio_creation
* trading_reinforcement_learning

The first one gives a good understanding of trading in general, some visualizations and summary statistics you can perform. Time series analysis is an introduction to price prediction models using pure time series. Portfolio creation helps you make smarter decision when deciding about allocationg money, however the stocks predicion componentes are very naive, that is why you can use trading_reinforcement_learning notebook to understand how Deep Reinforcement Learning can be used to develop and autonomous trading strategy. 

## Next steps and improvements
There are a lot of things to add, either on the already created notebook or create any other to make this repo more rich. Kindly make a **pull request**, I will be glad to approve it.
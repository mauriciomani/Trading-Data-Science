# Trading Data Science
This repository does not aim to find best model for particular problem (portfolio selection, stock price prediction, etc.) but to illustrate how you can analyze and model this problems. **It requieres you to have previous knowledge in this methods**, this repo just illustrate how to conduct them in python, but does not aim to teach deeply.

You can run the notebooks by downloading the following stocks historical information and having **conda** installed, pmdarima https://github.com/alkaline-ml/pmdarima and Keras (or please install all the necessary libraries):
* Facebook
* Tesla
* Disney
* Kimberly Clark.

All stocks use information from year 2000 all the way to 11th of December 2020.

## Structure
I suggest the following order of visualization:
* EDA_example
* time_series_analysis
* portfolio_creation
* trading_reinforcement_learning

The first one gives a good understanding of trading in general and some visualizations and summary statistics you can perform. Time series analysis is an introduction to price prediction models. Portfolio creation helps you make smarter decision when deciding about allocationg money, however the stocks predicion componentes are very naive, that is why you can use RL notebook to understand how Deep Reinforcement Learning can be used to develop and autonomous trading strategy. 

## Further work
1. Add linear programming illustration in portfolio selection.

There are a lot of things to add, please add them either on the main notebook or create any addition to make this repo more rich and kindly make a **pull request**, I will be glad to approve it.
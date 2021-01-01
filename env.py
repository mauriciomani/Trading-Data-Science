import numpy as np
import itertools

class Enviroment():
    def __init__(self, data, budget):
        #in order to reduce state space kindly round
        self.data_train = data.dropna().round().to_numpy()
        self.n_step, self.n_stock = self.data_train.shape
        self.budget = budget
        self.action_space = self.n_stock ** 3
        self.state_space = (self.n_stock * 2) + 1
        
        self.current_step = None
        self.stocks_owned = None
        self.stocks_price = None
        #I am separating casg from budget since cash will be changing
        self.cash = None
        self.reward = None
        
    def value(self):
        return np.sum(self.stocks_owned * self.stocks_price) + self.cash
    
    def reset(self):
        """We will suppose that you can get rid of all your positions"""
        obs = []
        self.current_step = 0
        self.stocks_owned = self.n_stock * [0]
        self.stocks_price = self.data_train[self.current_step, :]
        self.cash = self.budget
        obs.extend(self.stocks_owned)
        obs.extend(list(self.stocks_price))
        obs.append(self.cash)
        return(obs)
    
    def step(self, action):
        assert action < self.action_space 
        obs = []
        prev_val = self.value()
        self.current_step += 1
        self.stocks_price = self.data_train[self.current_step, :]
        self.trade(action)
        current_val = self.value()
        self.reward = current_val - prev_val
        #remember is size n but last object is n-1, otherwise you would have out of bounds
        done = self.current_step == self.n_step - 1
        obs.extend(self.stocks_owned)
        obs.extend(list(self.stocks_price))
        obs.append(self.cash)
        return(obs, self.reward, done)
    
    def sell(self, sell_index):
        """
        Sell all the stocks in sell_index. Simple procedure just add to cash the amount extracted from the product of number of stocks times current price and assign 0 stocks to that one. If sell all stocks are sold.
        Params:
            sell_index : list of index of stocks to sell
        Returns:
            None
        """
        for stock in sell_index:
            self.cash += self.stocks_price[stock] * self.stocks_owned[stock]
            self.stocks_owned[stock] = 0
    
    def buy(self, buy_index):
        can_buy = True
        while can_buy:
            #evenly buy stocks from buy_index
            for stock in buy_index:
                if self.cash > self.stocks_price[stock]:
                    self.stocks_owned[stock] += 1 
                    self.cash -= self.stocks_price[stock]
                else:
                    can_buy = False
            
    
    def trade(self, action):
        """
        Positions code as follow: 0: buy; 1: sell, 2: hold
        """
        action_list = list(itertools.product([0, 1, 2], repeat=self.n_stock))
        action_vec = action_list[action]
        #we will store the index of shares that need to be either sell or buy
        sell_index = []
        buy_index = []
        for i, a in enumerate(action_vec):
            if a == 0:
                buy_index.append(i)
            elif a == 2:
                sell_index.append(i)
        
        if sell_index:
            self.sell(sell_index)
        if buy_index:
            self.buy(buy_index)
        
        
    
    
    
    
        
        
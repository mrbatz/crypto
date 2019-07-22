import requests
import time as tm
from matplotlib import pyplot as plt
import numpy as np

x = [] #time
y = [] #price


#makes the bitcoin api call
def get_price():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        price = r['bpi']['USD']['rate']
        return price

    except KeyError:
        print('Something went wrong.')




while True:
    x=np.append(x,tm.time())
    y = np.append(y,get_price())

    plt.scatter(x,y,label='BTC',color='b')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Bitcoin Tracker')
    plt.legend()
    plt.show()

    tm.sleep(30)

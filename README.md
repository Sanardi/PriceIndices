
## Installation 

### pip 

```
pip install PriceIndics
```
 ### From Source (Github)
 
 git clone https://github.com/dc-aichara/Price-Indices.git
 
 cd PriceIndices 
 
 python3 setup.py install
 
 ## Usages 
 
 ```python
from PriceIndices import MarketHistory, Indices

```
## Examples 

```python
>>> history = MarketHistory()

>>> df = history.get_history('bitcoin', '20130428', '20190624')  # Get Market History
>>> df.head()
        Date     Open*      High       Low   Close**       Volume    Market Cap
0 2019-06-23  10696.69  11246.14  10556.10  10855.37  20998326502  192970090355
1 2019-06-22  10175.92  11157.35  10107.04  10701.69  29995204861  190214124824
2 2019-06-21   9525.07  10144.56   9525.07  10144.56  20624008643  180293241528
3 2019-06-20   9273.06   9594.42   9232.48   9527.16  17846823784  169304784791
4 2019-06-19   9078.73   9299.62   9070.40   9273.52  15546809946  164780855869


>>> df =  history.get_price('bitcoin', '20130428', '20190624')  # Get closing price

>>> df.head()
        date     price
0 2019-06-23  10855.37
1 2019-06-22  10701.69
2 2019-06-21  10144.56
3 2019-06-20   9527.16
4 2019-06-19   9273.52


>>> df_bvol = Indices.get_bvol_index(df)  # Calculate Volatility Index
>>> df_bvol.head()
        date     price  BVOL_Index
0 2019-06-22  10701.69    0.636482
1 2019-06-21  10144.56    0.636414
2 2019-06-20   9527.16    0.619886
3 2019-06-19   9273.52    0.608403
4 2019-06-18   9081.76    0.604174

>>> indices.get_bvol_graph(df_bvol)  # Plot Volatility Index 

"""
This will return a plot of BVOL index against time also save volatility index plot in your working directory as 'bvol_index.png'
"""

>>> df_rsi = indices.get_rsi(df)   # Calculate RSI

>>> print(df_rsi.tail())
           date   price  price_change   gain   loss  gain_average  loss_average        RS      RSI_1  RS_Smooth      RSI_2
2217 2013-05-02  105.21          7.46   7.46   0.00      1.532143      2.500000  0.612857  37.998229   0.561117  35.943306
2218 2013-05-01  116.99         11.78  11.78   0.00      2.373571      2.175714  1.090939  52.174596   0.975319  49.375257
2219 2013-04-30  139.00         22.01  22.01   0.00      3.945714      1.981429  1.991348  66.570258   1.869110  65.145981
2220 2013-04-29  144.54          5.54   5.54   0.00      3.878571      1.981429  1.957462  66.187226   2.206422  68.812592
2221 2013-04-28  134.21        -10.33   0.00  10.33      3.878571      2.506429  1.547449  60.745050   1.397158  58.283931

>>> indices.get_rsi_graph(df_rsi)  # Plot RSI

"""
This will return a plot of RSI against time and also save RSI plot in your working directory as 'rsi.png'
"""
>>> df_bb = Indices.get_bollinger_bands(df, 20) # Get Bollinger Bands and plot
>>> df_bb.tail()
           date   price       SMA         SD       pluse     minus
2243 2013-05-02  105.21  115.2345   6.339257  127.913013 -115.2345
2244 2013-05-01  116.99  114.9400   6.097587  127.135174 -114.9400
2245 2013-04-30  139.00  115.7900   8.016499  131.822998 -115.7900
2246 2013-04-29  144.54  116.9175  10.217936  137.353372 -116.9175
2247 2013-04-28  134.21  117.4530  10.842616  139.138233 -117.4530

"""
This will also save Bollingers bands plot in your working directory as 'bollinger_bands.png'
"""

```

### License 
[MIT](https://choosealicense.com/licenses/mit/) © [Dayal Chand Aichara](https://github.com/dc-aichara)


### Disclaimer: 
```
All content provided here, is for your general information only, procured  from third party sources.
I make no warranties of any kind in relation to this content, including but  not limited to accuracy
and updatedness. No part of the content that I provide  constitutes  financial  advice, legal advice 
or any other form of advice meant for your specific reliance for any purpose. Any use or reliance on
my content is solely at your own risk  and  discretion. You should conduct your own research, review, 
analyse and  verify my content  before relying  on them. Trading is a highly risky activity that can 
lead to  major  losses, please  therefore  consult your financial advisor before making any decision.
No content on this Site is meant to be a solicitation or offer.
```

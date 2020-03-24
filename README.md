# Integrated Global Asset Management: Quantitative Country ETF Trading Strategy
WQU Capstone Project

## Authors
* Arturo Aguilar
* Xiaochen Lin
* Wen Jiang

©Arturo Aguilar. ©Xiaochen Lin. ©Wen Jiang. All Rights Reserved.
 
This project is an effort to build a country trading strategy to outperform the MSCI All Country World Index (ACWI). The strategy includes technical, fundamental, economic, market sentiment and alternative factors. There seems to be enough room to build a strategy that generates alpha taking into account each countries’ equity and currency performance. A framework of the trading strategy is shown below.

![factors](/factors.png)

![factor processing](/factor%20processing.png)

## Table of Contents
### Folder:
#### factor data
stores time series data for each factor and each ETF, generated using [process raw data into factor data](/process%20raw%20data%20into%20factor%20data.ipynb) and [process price data into factor data](/process%20price%20data%20into%20factor%20data.ipynb).
#### price data
stores daily ohlcv data for each ETF, generated using [download price data](/download%20price%20data.ipynb).
#### forward return
stores forward 21-trading day return for each ETF, generated using [process price data into forward return](process%20price%20data%20into%20forward%20return.ipynb)
#### raw data
stores raw factor data (has been removed).


## Results
### Developed Markets & Emerging Markets

<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>
<br/><br/>

### U.S. Subcase: Three Factors & Five Factors: 2017 and 2018

US:VOO

S&P 500 Index, representing 500 of the largest U.S. companies. Goal is to closely track the index’s return, which is considered a gauge of overall U.S. stock returns. 

https://investor.vanguard.com/etf/profile/VOO


FF3_factors[['Mkt-RF','SMB','HML']])



FF5_factors[['Mkt-RF','SMB','HML','RMW','CMA']]
 


## References

[1] Marko Kolanovic & Zhen Wei (2013). Systematic Strategies Across Asset Classes. JP Morgan. Available at: https://www.cmegroup.com/education/files/jpm-systematic-strategies-2013-12-11-1277971.pdf (Accessed: February, 2020).

[2] MSCI (2020). MSCI ACWI Index. Available at: https://www.msci.com/acwi (Accessed: February, 2020).

[3] Bloomberg (2020). Market Data. Available at: https://www.bloomberg.com/professional/ (Accessed: February, 2020).

[4] Marcos Lopéz de Prado (2018). Advances in Financial Machine Learning.

[5] MSCI (1998). Barra GEM. Available at: https://www.alacra.com/alacra/help/barra_handbook_GEM.pdf (Accessed: March, 2020).

[6] MSCI (1998). Barra USE3. Available at: http://www.alacra.com/alacra/help/barra_handbook_US.pdf (Accessed: March 2020).

[7] Kenneth R. French (1993). Description of Fama/French 3 Factors. Available at: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_factors.html (Accessed: March, 2020).

[8] Kenneth R. French (2014). Description of Fama/French 5 Factors (2x3). Available at: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_5_factors_2x3.html (Accessed: March 2020).

[9] Andrew Ang (2013). Factor Investing. Available at: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2277397 (Accessed: February 2020).

[10] Markit Economics (2020). PMI by IHS Markit. Available at: https://ihsmarkit.com/products/pmi.html (Accessed: March 2020).

[11] Investopedia (2020). Factor Investing. Available at: https://www.investopedia.com/terms/f/factor-investing.asp (Accessed: March 2020).

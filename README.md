# Integrated Global Asset Management: Quantitative Country ETF Trading Strategy

## Authors
* Arturo Aguilar
* Xiaochen Lin
* Wen Jiang

©Arturo Aguilar. ©Xiaochen Lin. ©Wen Jiang. All Rights Reserved.

## WQU Capstone Project

Our Implementation (Feb 2020 - Apr 2020): [Quantitative Country ETF Trading Strategy](https://github.com/xlinGithub/Quantitative-Country-ETF-Trading-Strategy)

Our Implementation (Dec 2019 - Feb 2020): [Integrated Global Asset Management](https://github.com/wenjiangwj1/Integrated-Global-Equity-Asset-Management)

Our Presentations (Dec 2019 - Apr 2020): [Integrated Global Asset Management](https://drive.google.com/drive/u/2/folders/1gL_FQaxAiupznbdxg7vLuEPTecbatp34)

## Overview
 
This project is an effort to build a country trading strategy to outperform the MSCI All Country World Index (ACWI). The strategy includes technical, fundamental, economic, market sentiment and alternative factors. There seems to be enough room to build a strategy that generates alpha taking into account each countries’ equity and currency performance. A framework of the trading strategy is shown below.

![factors](/factors.png#center)

![factor processing](/factor%20processing.png#center)



## Table of Contents
### Folders:
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

https://github.com/xlinGithub/Quantitative-Country-ETF-Trading-Strategy/blob/master/modeling.ipynb

https://github.com/xlinGithub/Quantitative-Country-ETF-Trading-Strategy/blob/master/quantopian_backtest_ACWI.py

https://github.com/xlinGithub/Quantitative-Country-ETF-Trading-Strategy/blob/master/quantopian_backtest_ACWX.py


### U.S. Daily: Three Factors, Four Factors & Five Factors

#### U.S.:VOO

S&P 500 Index, representing 500 of the largest U.S. companies. Goal is to closely track the index’s return, which is considered a gauge of overall U.S. stock returns. 

Source: https://investor.vanguard.com/etf/profile/VOO

#### U.S.: ACWI

The investment seeks to track the investment results of the MSCI ACWI composed of large- and mid-capitalization developed and emerging market equities.

Source: https://screener.fidelity.com/ftgw/etf/goto/snapshot/snapshot.jhtml?symbols=ACWI

#### International: ACWX

The investment seeks to track the investment results of the MSCI ACWI ex USA Index composed of large- and mid-capitalization non-U.S. equities. 

Source: https://screener.fidelity.com/ftgw/etf/goto/snapshot/snapshot.jhtml?symbols=ACWX

#### AQR Capital Management

AQR is a global investment management firm dedicated to delivering results for our clients.

Source: https://www.aqr.com/Insights/Datasets

#### Three Factors, Four Factors & Five Factors: 2017 and 2018

https://github.com/xlinGithub/Quantitative-Country-ETF-Trading-Strategy/blob/master/US%20Three%2C%20Four%20and%20Five%20Factors%20Models%202017-2018.ipynb

FF3_factors[['Mkt-RF','SMB','HML']])

FF4_factors[['AQR_MKTRF','AQR_SMB','AQR_BAB','AQR_QMJ']]

FF5_factors[['Mkt-RF','SMB','HML','RMW','CMA']]

Elaborating our model with loss function optimization scheme, we obtain our Five Factors Models with Ridge, a Tikhonov regularization,  outperform other Factors Models in ETF return prediction based on the associated market factor exposures. 

## References

[1] Marko Kolanovic & Zhen Wei (2013). Systematic Strategies Across Asset Classes. J.P. Morgan. Available at: https://www.cmegroup.com/education/files/jpm-systematic-strategies-2013-12-11-1277971.pdf (Accessed: February, 2020).

[2] MSCI Inc (2020). MSCI ACWI Index. Available at: https://www.msci.com/acwi (Accessed: February, 2020).

[3] Bloomberg (2020). Market Data. Available at: https://www.bloomberg.com/professional/ (Accessed: February, 2020).

[4] Marcos Lopéz de Prado (2018). Advances in Financial Machine Learning.

[5] MSCI Inc (1998). Barra GEM. Available at: https://www.alacra.com/alacra/help/barra_handbook_GEM.pdf (Accessed: March, 2020).

[6] MSCI Inc (1998). Barra USE3. Available at: http://www.alacra.com/alacra/help/barra_handbook_US.pdf (Accessed: March 2020).

[7] Kenneth R. French (1993). Description of Fama/French 3 Factors. Available at: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_factors.html (Accessed: March, 2020).

[8] Kenneth R. French (2014). Description of Fama/French 5 Factors (2x3). Available at: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_5_factors_2x3.html (Accessed: March 2020).

[9] Andrew Ang (2013). Factor Investing. Available at: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2277397 (Accessed: February 2020).

[10] Markit Economics (2020). PMI by IHS Markit. Available at: https://ihsmarkit.com/products/pmi.html (Accessed: March 2020).
 
[11] Investopedia (2020). Factor Investing. Available at: https://www.investopedia.com/terms/f/factor-investing.asp (Accessed: March 2020).

[12] BlackRock Inc (2020). iShares MSCI ACWI ETF. Available at: https://www.ishares.com/us/products/239600/ishares-msci-acwi-etf (Accessed: March 2020).

[13] Wayne Eckerson (2018). The Flavors of Data Science and Engineering. Eckerson Group. Available at: https://www.eckerson.com/articles/diving-into-dataops-the-underbelly-of-modern-data-pipelines (Accessed: March 2020).

[14] Alberto Gomez (2020). Finamex: Friday's Good Read - Explaining the Recent Failure of Value Investing (Email: January 2020).
[15] AQR Capital Management, Betting Against Beta: Equity Factors, Daily (2020). Factor Investing. Available at: https://www.aqr.com/Insights/Datasets/Betting-Against-Beta-Equity-Factors-Daily (Accessed: March 2020).

[16] AQR Capital Management, Quality Minus Junk: Factors, Daily (2020). Factor Investing. Available at: https://www.aqr.com/Insights/Datasets/Quality-Minus-Junk-Factors-Daily (Accessed: March 2020).
 
[17] Scikit-learn (2020). sklearn.ensemble.RandomForestRegressor. Available at: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html (Accessed: March 2020).

[18] Scikit-learn (2020). sklearn.linear_model.Ridge. Available at: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html (Accessed: March 2020).

[19] Marko Kolanovic & Rajesh T. Krishnamachari (2017). Big Data and AI Strategies - Machine Learning and Alternative Data Approach to Investing. J.P. Morgan. Available at: https://www.cfasociety.org/cleveland/Lists/Events%20Calendar/Attachments/1045/BIG-Data_AI-JPMmay2017.pdf (Accessed: March, 2020).

[20] Andrew Ang, Bob Bass, Sara Shores (2017). Strategic Factor Allocation. BlackRock. Available at: https://files.assettv.com/live/blk-strategic-factor-allocation-2017.pdf (Accessed: March, 2020).
 
[21] Oguz A. Acar (2019). Why Crowdsourcing Often Leads to Bad Ideas. Harvard Business Review. Available at: https://hbr.org/2019/12/why-crowdsourcing-often-leads-to-bad-ideas (Accessed: March, 2020).

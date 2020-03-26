import pandas as pd

rebalance_dates = ['2019-01-02', '2019-02-01', '2019-03-01', 
                   '2019-04-01', '2019-05-01', '2019-06-03', 
                   '2019-07-01', '2019-08-01', '2019-09-03',
                   '2019-10-01', '2019-11-01', '2019-12-02']

def preview(df):
    log.info(' \n %s ' % df.head(10))
    log.info(' \n %s ' % df.tail(10))
    return df

def initialize(context):
    url = 'https://raw.githubusercontent.com/xlinGithub/Quantitative-Country-ETF-Trading-Strategy/9be718b4125d7f33e691b91693486884cfe91f0f/backtest_inputs.csv' # long-only
    # url = 'https://raw.githubusercontent.com/xlinGithub/Quantitative-Country-ETF-Trading-Strategy/1da81303de9cc9b4fd315c7ab90b753831406d5e/backtest_inputs.csv' # long-short
    # url = 'https://raw.githubusercontent.com/xlinGithub/Quantitative-Country-ETF-Trading-Strategy/3317eae891e7ab96af8399f7c8709dbf4c905b77/backtest_inputs.csv' # long-only ex US
    try:
        fetch_csv(url, 
                  date_column='Date',
                  pre_func = preview,
                  date_format='%Y/%m/%d')
    except:
        fetch_csv(url, 
                  date_column='Date',
                  pre_func = preview,
                  date_format='%Y-%m-%d')
    
    context.rebalance_dates = ['2019-01-02', '2019-02-01', '2019-03-01', 
                               '2019-04-01', '2019-05-01', '2019-06-03', 
                               '2019-07-01', '2019-08-01', '2019-09-03',
                               '2019-10-01', '2019-11-01', '2019-12-02']
    
    set_benchmark(symbol('ACWX'))
    set_slippage(slippage.FixedBasisPointsSlippage(basis_points=0.1, volume_limit=1))
    schedule_function(market_rebalance_process, date_rules.every_day(), time_rules.market_close(minutes=180))
    
def market_rebalance_process(context, data):
    # log.info(get_datetime('US/Eastern').date())
    if get_datetime('US/Eastern').date().strftime('%Y-%m-%d') in context.rebalance_dates:
        log.info('rebalance')
        for stock in data.fetcher_assets:
            # log.info(stock)
            # log.info(data.current(stock, 'Weight'))
            order_target_percent(stock, data.current(stock, 'Weight'))
    else:
        pass

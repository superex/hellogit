import pandas as pd
import mplfinance as mpf


def test1():
    df = pd.DataFrame(columns=['Date', 'Volume', 'Open', 'High', 'Low', 'Close'])
    print(df)

    df.loc[len(df.index)] = ['2021-02-01', 70161939, 595.00, 612.00, 587.00, 611.00]
    df.loc[len(df.index)] = ['2021-02-02', 80724207, 629.00, 638.00, 622.00, 632.00]

    df = pd.DataFrame([
        ['2021-02-01', 70161939, 595.00, 612.00, 587.00, 611.00],
        ['2021-02-02', 80724207, 629.00, 638.00, 622.00, 632.00],
        ['2021-02-03', 59763227, 638.00, 642.00, 630.00, 630.00],
        ['2021-02-04', 47547873, 626.00, 632.00, 620.00, 627.00],
        ['2021-02-05', 57350831, 638.00, 641.00, 631.00, 632.00],
        ['2021-02-17', 115578402, 663.00, 668.00, 660.00, 663.00],
        ['2021-02-18', 54520341, 664.00, 665.00, 656.00, 660.00],
        ['2021-02-19', 51651844, 656.00, 657.00, 647.00, 652.00],
        ['2021-02-22', 39512078, 660.00, 662.00, 650.00, 650.00],
        ['2021-02-23', 52868029, 641.00, 643.00, 633.00, 641.00],
        ['2021-02-24', 80010637, 627.00, 636.00, 625.00, 625.00],
        ['2021-02-25', 45279276, 636.00, 636.00, 628.00, 635.00],
        ['2021-02-26', 137933162, 611.00, 618.00, 606.00, 606.00],
    ], columns=['Date', 'Volume', 'Open', 'High', 'Low', 'Close'])

    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df.set_index('Date', inplace=True)

    mpf.available_styles()

    mpf.plot(df,
             type='candle',
             title='2330',
             volume=True,
             ylabel_lower='Shares')

    mpf.plot(df, type='candlestick', style='yahoo', ylabel='$', title='2330')

    mc = mpf.make_marketcolors(up='r',
                               down='g',
                               edge='',
                               wick='inherit',
                               volume='inherit')
    s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)
    mpf.plot(df, type='candle', style=s, volume=True)

    mpf.plot(df,
             type='candle',
             style='yahoo',
             mav=(2, 3),
             title='2330',
             volume=True,
             ylabel_lower='Shares')

import datetime
import math
import sys
import zipfile
import pandas as pd
import mplfinance as mpf


class MTX_period_data:
    expiry_month = ""
    trx_date_time = ""  # 成交時間
    trx_number = -1  # 成交數量
    max_price = sys.float_info.min
    min_price = sys.float_info.max
    start_price = -1
    end_price = -1

    def toList(self):
        return [self.trx_date_time,
                int(self.trx_number),
                int(self.start_price),
                int(self.max_price),
                int(self.min_price),
                int(self.end_price)]

    def toText(self):
        s = self.expiry_month
        s += "," + self.trx_date_time
        s += "," + str(self.trx_number)
        s += ",start=" + str(self.start_price)
        s += ",end=" + str(self.end_price)
        s += ",min=" + str(self.min_price)
        s += ",max=" + str(self.max_price)
        return s


class MTX_data:
    trx_date = ""  # 成交日期
    product_id = ""  # 商品代號
    expiry_month = ""  # 到期月份(週別)
    trx_date_time = ""  # 成交時間
    deal_price = -1  # 成交價格
    trx_number = -1  # 成交數量


class MTX2:
    # _list_ma_data = []
    _cur_data = MTX_period_data()

    def __init__(self, product_id, expiry_month):
        self.product_id = product_id
        self.expiry_month = expiry_month
        self.df = pd.DataFrame(columns=['Date', 'Volume', 'Open', 'High', 'Low', 'Close'])

    @staticmethod
    def read_zip(fn):
        with zipfile.ZipFile(fn, "r") as zip_ref:
            fn_csv = zip_ref.namelist()[0]
            with zip_ref.open(fn_csv) as f:
                return f.read()

    def parse_data(self, line):
        cols = line.split(',')
        if len(cols) != 9:
            return None

        if cols[1].strip() != self.product_id:
            return None

        if len(self.expiry_month) > 0 and cols[2].strip() != self.expiry_month:
            return None

        data = MTX_data()
        data.trx_date = cols[0].strip()
        data.product_id = cols[1].strip()
        data.expiry_month = cols[2].strip()
        data.trx_date_time = cols[3].strip()
        data.deal_price = cols[4].strip()
        data.trx_number = cols[5].strip()

        if float(data.deal_price) < 0:
            return None

        return data

    def load_from_zip(self, filename):
        b = MTX2.read_zip(filename)
        s = b.decode('Big5')
        ss = s.splitlines()

        print("product_id=" + self.product_id)
        print("expiry_month=" + self.expiry_month)

        count = 0
        for line in ss:
            mtx = self.parse_data(line)
            if mtx is None:
                continue

            count = count + 1
            if count >= 5000:
                pass

            self.add_data(mtx)

    def plot_data(self):
        if self._cur_data is not None and self._cur_data.trx_number != -1:
            # self._list_ma_data.append(self._cur_data)
            self.df.loc[len(self.df.index)] = self._cur_data.toList()
            self._cur_data = None

        # s = "_list_ma_data.count=" + str(len(self._list_ma_data))
        # print(s)

        # for ma in self._list_ma_data:
        #    print(ma.toText())
        print("df_count="+str(len(self.df)))

        # self.df['Date'] = pd.to_datetime(self.df['Date'], format='%Y-%m-%d')
        self.df['Date'] = pd.to_datetime(self.df['Date'], format='%Y-%m-%d %H:%M:%S')
        self.df.set_index('Date', inplace=True)

        mc = mpf.make_marketcolors(up='r',
                                   down='g',
                                   edge='',
                                   wick='inherit',
                                   volume='inherit')
        s = mpf.make_mpf_style(base_mpf_style='yahoo', marketcolors=mc)
        mpf.plot(self.df, type='candle', style=s, volume=True)

    def add_data(self, mtx):
        tmp = mtx.trx_date + "_" + mtx.trx_date_time
        dt = datetime.datetime.strptime(tmp, '%Y%m%d_%H%M%S')

        period = math.floor(dt.timestamp() / 600) * 600
        dt2 = datetime.datetime.fromtimestamp(period)

        # s = str(dt) + "=>" + str(dt2)
        # print(s)

        tdt = str(dt2)

        if tdt == self._cur_data.trx_date_time and self._cur_data.expiry_month == mtx.expiry_month:

            if mtx.deal_price > self._cur_data.max_price:
                self._cur_data.max_price = mtx.deal_price
            elif mtx.deal_price < self._cur_data.min_price:
                self._cur_data.min_price = mtx.deal_price

            self._cur_data.trx_number += int(mtx.trx_number)
            self._cur_data.end_price = mtx.deal_price

        else:
            if self._cur_data.trx_number != -1:
                # self._list_ma_data.append(self._cur_data)
                self.df.loc[len(self.df.index)] = self._cur_data.toList()

            self._cur_data = MTX_period_data()
            self._cur_data.expiry_month = mtx.expiry_month
            self._cur_data.trx_date_time = tdt
            self._cur_data.trx_number = int(mtx.trx_number)
            self._cur_data.max_price = mtx.deal_price
            self._cur_data.min_price = mtx.deal_price
            self._cur_data.start_price = mtx.deal_price
            self._cur_data.end_price = mtx.deal_price

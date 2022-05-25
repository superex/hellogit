class MTX2:

    def add_data(self, mtx):
        print(mtx.trx_date)
        print(mtx.product_id)
        print(mtx.expiry_month)
        print(mtx.trx_date_time)
        print(mtx.deal_price)
        print(mtx.trx_number)


class MTX_data:
    trx_date = "" #成交日期
    product_id = "" #商品代號
    expiry_month = "" #到期月份(週別)
    trx_date_time = "" #成交時間
    deal_price = -1 #成交價格
    trx_number = -1 #成交數量


def parse_data(cols):
    if len(cols) != 9:
       return None

    data = MTX_data()
    data.trx_date = cols[0].strip()
    data.product_id = cols[1].strip()
    data.expiry_month = cols[2].strip()
    data.trx_date_time = cols[3].strip()
    data.deal_price = cols[4].strip()
    data.trx_number = cols[5].strip()

    return  data;
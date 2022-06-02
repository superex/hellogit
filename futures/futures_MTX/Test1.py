import datetime
import zipfile

from MTX import MTX2


def test_read_futures_data():
    b = read_zip()
    s = b.decode('Big5')
    ss = s.splitlines()

    day_month = ""
    m2 = MTX2("MTX", "")
    for line in ss:
        mtx = m2.parse_data(line)
        if mtx is None:
            continue

        dm = mtx.expiry_month + "_" + mtx.trx_date
        if dm != day_month:
            print(dm)
            day_month = dm


def read_zip():
    fn = "D:\\test\\20220524_option_data\\Daily_2022_05_18.zip"
    with zipfile.ZipFile(fn, "r") as zip_ref:
        fn_csv = zip_ref.namelist()[0]
        with zip_ref.open(fn_csv) as f:
            return f.read()


def test_date_time():
    s1 = '20220513_150022'
    s2 = '20220513_150122'
    print(type(s1))
    d1 = datetime.datetime.strptime(s1, '%Y%m%d_%H%M%S')
    d2 = datetime.datetime.strptime(s2, '%Y%m%d_%H%M%S')

    print(int(d1.timestamp()))
    print(int(d2.timestamp()))
    print(d2.timestamp())

    now = datetime.datetime.now()
    print(now)
    print(now.timestamp())

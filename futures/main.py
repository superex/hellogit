import zipfile

from MTX import parse_data, MTX2


def read_zip():
    fn = "D:\\test\\20220524_option_data\\Daily_2022_05_16.zip"
    with zipfile.ZipFile(fn, "r") as zip_ref:
        fn_csv = zip_ref.namelist()[0]
        with zip_ref.open(fn_csv) as f:
            return f.read()


if __name__ == '__main__':
    b = read_zip()
    print(type(b))
    s = b.decode('Big5')
    print(type(s))
    ss = s.splitlines()
    print(type(ss))
    print(ss[0])

    count = 0
    mtx2 = MTX2()
    for line in ss:
        cols = line.split(',')
        if len(cols) != 9:
            continue
        if cols[1].strip() != 'MTX':
            continue

        count = count + 1
        if count >= 3:
            break

        print(line)

        mtx = parse_data(cols)
        if mtx is None:
            print("none")
            continue

        mtx2.add_data(mtx)

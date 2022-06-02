import TestPlot
from MTX import MTX2

if __name__ == '__main__':
    TestPlot.test1()


if __name__ == '__main__2':
    mtx2 = MTX2("MTX", "202205")
    fn = "D:\\test\\20220524_option_data\\Daily_2022_05_16.zip"
    mtx2.load_from_zip(fn)
    mtx2.plot_data()

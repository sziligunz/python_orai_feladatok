import datetime as d


def eltelt_ido(ora1, perc1, ora2, perc2):
    time1 = d.datetime(2023, 3, 1, ora1, perc1)
    time2 = d.datetime(2023, 3, 1, ora2, perc2)
    timedelta = time2 - time1
    return (d.datetime.now().min + timedelta).time()



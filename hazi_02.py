import datetime as d
import csv as c


def eltelt_ido(ora1, perc1, ora2, perc2):
    time1 = d.datetime(2023, 3, 1, ora1, perc1)
    time2 = d.datetime(2023, 3, 1, ora2, perc2)
    # checking for negative timedelta
    timedelta = time2 - time1 if time2 > time1 else time1 - time2
    return (d.datetime.now().min + timedelta).time()


def kesesek(path):
    res = None
    try:
        with open(path, 'r', encoding="utf8") as file:
            res = {}
            reader = c.reader(file, delimiter=',')
            for row in reader:
                if row[0].strip() == "nev":
                    continue
                if row[0].strip() not in res.keys():
                    res[row[0].strip()] = d.timedelta(0, 0, 0, 0, 0, 0, 0)
                start = d.datetime.strptime(row[1].strip(), "%Y-%m-%d %H:%M:%S")
                end = d.datetime.strptime(row[2].strip(), "%Y-%m-%d %H:%M:%S")
                if end > start:
                    res[row[0].strip()] += end - start
            most = d.timedelta(0, 0, 0, 0, 0, 0, 0)
            most_name = None
            for key, value in res.items():
                if value > most:
                    most = value
                    most_name = key
            return most_name
    except FileNotFoundError as e:
        return res

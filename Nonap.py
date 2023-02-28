import datetime as d


def nonap_statisztika():
    days = {
        0 : "Hétfő",
        1 : "Kedd",
        2 : "Szerda",
        3 : "Csütörtök",
        4 : "Péntek",
        5 : "Szombat",
        6 : "Vasárnap"
    }
    dic = {
        "Hétfő" : 0,
        "Kedd" : 0,
        "Szerda" : 0,
        "Csütörtök" : 0,
        "Péntek" : 0,
        "Szombat" : 0,
        "Vasárnap" : 0,
    }
    for i in range(1993, 2024):
        day = days[d.datetime(i, 3, 8).weekday()]
        dic[day] += 1
    return dic


print(nonap_statisztika())

import datetime
import datetime as d
import argparse as a
import requests
from requests.exceptions import HTTPError

HP_API = "https://hp-api.onrender.com/api/characters"
args = {}
response = [{}]


def setup_arguments():
    global args
    parser = a.ArgumentParser()
    parser.add_argument('-y', action="store_true")
    parser.add_argument('-o', action="store_true")
    parser.add_argument('-avg', action="store_true")
    parser.add_argument('-house', choices=("Gryffindor", "Ravenclaw", "Slytherin", "all"), default="all")
    args = vars(parser.parse_args())


def get_api_response():
    global response
    try:
        _ = requests.get(HP_API)
    except HTTPError as e:
        print("Something went wrong during api request: " + str(e.response))
        return
    except Exception as e:
        print("Something went wrong during api request: " + str(e))
        return
    response = _.json()
    # with open("apioutput.txt", "w") as f:
    #     f.write(f"name;dateOfBirth;yearOfBirth;wizard;house;alive\n")
    #     for item in response:
    #         f.write(f"{item['name']};{item['dateOfBirth']};{item['yearOfBirth']};{item['wizard']};{item['house']};{item['alive']}\n")


def print_youngest(_=True):
    res = []
    if args['house'] != "all":
        for item in response:
            if item['house'] == args['house']:
                res.append(item)
    else:
        for item in response:
            if item['house'] != "":
                res.append(item)
    res2 = []
    for item in res:
        if (item['yearOfBirth'] is not None and item['yearOfBirth'] != 0) and item["wizard"] is True and item["alive"] is True:
            if not isinstance(item['dateOfBirth'], datetime.date):
                if item['dateOfBirth'] is None or item['dateOfBirth'] == 0:
                    item['dateOfBirth'] = d.date(int(item['yearOfBirth']), 1, 1)
                else:
                    splited = str(item['dateOfBirth']).split('-')
                    item['dateOfBirth'] = d.date(int(splited[2]), int(splited[1]), int(splited[0]))
            res2.append(item)
    print(sorted(res2, key=lambda x: x['yearOfBirth'], reverse=_)[0]['name'])


def print_average():
    res = []
    if args['house'] != "all":
        for item in response:
            if item['house'] == args['house']:
                res.append(item)
    else:
        for item in response:
            if item['house'] != "":
                res.append(item)
    res2 = []
    ossz_eletkor = 0
    for item in res:
        if (item['yearOfBirth'] is not None and item['yearOfBirth'] != 0) and item["wizard"] is True and item['alive'] is True:
            item['yearOfBirth'] = int(item['yearOfBirth'])
            ossz_eletkor += d.datetime.now().year - item['yearOfBirth']
            res2.append(item)
    print(ossz_eletkor // len(res2))


if __name__ == '__main__':
    setup_arguments()
    get_api_response()
    if args['o']:
        print_youngest(False)
    if args['y']:
        print_youngest()
    if args['avg']:
        print_average()

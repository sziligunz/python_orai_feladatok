import os


def stats(path):
    res = {}
    files = os.listdir(path)
    for file in files:
        kiterjesztes = file.split(".")[1].strip()
        if kiterjesztes not in res.keys():
            res[kiterjesztes] = {
                "atlagos_fajlmeret": 0,
                "min_fajlmeret": 0,
                "max_fajlmeret": 0,
                "fajlok_szama": 0
            }
        # TODO
        print(os.stat(path + "/" + file))


stats("./")

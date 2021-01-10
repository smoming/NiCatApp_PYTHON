def dictToList(dict_data, *args):
    l = list()
    for k in args:
        if k in dict_data.keys():
            l.append(dict_data[k])
        else:
            l.append(None)
    return l


def dictToJson(dict_data, *args):
    d = dict()
    for k in args:
        if k in dict_data.keys():
            d.popitem(k, dict_data[args.index(k)])
        else:
            d.popitem(k, None)
    return d

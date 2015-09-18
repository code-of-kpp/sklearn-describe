import pkg_resources


def describe(obj):

    kw = dict()

    for ep in pkg_resources.iter_entry_points('sklearn.describe'):
        func = ep.load()

        kw = func(obj)

    return kw

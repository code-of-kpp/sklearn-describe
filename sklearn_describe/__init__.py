import pkg_resources


def describe(obj):

    kw = dict()

    for ep in pkg_resources.iter_entry_points('sklearn.describe'):
        check = ep.load()

        if check.applicable(obj):
            kw = check.describe(obj, **kw)

    return kw

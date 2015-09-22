import pkg_resources



def describe(obj, allowed=None):

    kw = dict()

    sentinel = object()
    checks = []

    checked = set()

    for ep in pkg_resources.iter_entry_points('sklearn.describe'):

        if allowed is not None:
            if ep.name not in allowed:
                continue
        checks.insert(0, ep)

    checks.insert(0, sentinel)

    while len(checks):
        ep = checks.pop()

        if ep is sentinel:
            if len(checks):
                raise RuntimeError('Broken dependencies while describing')
            else:
                break

        check = ep.load()

        if not all(req in checked for req in check.needs):
           checks.insert(0, ep)

        if check.applicable(obj):
            kw = check.describe(obj, **kw)

    return kw

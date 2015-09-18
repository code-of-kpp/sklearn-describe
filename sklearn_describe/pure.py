class PureChecker(object):
    @staticmethod
    def applicable(obj, **kwargs):
        return True

    @staticmethod
    def describe(obj, **kwargs):
        if isinstance(obj, type):
            kwargs['instance'] = False
        else:
            kwargs['instance'] = True
        return kwargs

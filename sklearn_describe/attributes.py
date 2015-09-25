ATTRIBUTES = (
    'fit',
    'predict',
    'predict_proba',
    'predict_log_proba',
    'fit_predict',
    'partial_fit',
    'transform',
    'inverse_transform',
    'decision_function',
    'score',
)


class AttributesChecker(object):

    @staticmethod
    def applicable(obj, **kwargs):
        return True

    @staticmethod
    def describe(obj, **kwargs):
        for key in ATTRIBUTES:
            kwargs[key] = hasattr(obj, key)
        return kwargs

    needs = ()

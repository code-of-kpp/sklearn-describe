import six


class MixinsChecker(object):
    @staticmethod
    def applicable(obj, **kwargs):
        if kwargs.get('instance', False):
            cls = obj.__class__
        else:
            cls = obj

        for p_cls in cls.__bases__:
            if p_cls.__module__ == 'sklearn.base':
                return True
        return False

    @staticmethod
    def describe(obj, **kwargs):
        from sklearn import base

        MIXINS = {
            'classifier': base.ClassifierMixin,
            'cluster': base.ClusterMixin,
            'bicluster': base.BiclusterMixin,
            'metaestimator': base.MetaEstimatorMixin,
            'regressor': base.RegressorMixin,
            'transformer': base.TransformerMixin,
        }

        kwargs.setdefault('mixins', set())

        if kwargs.get('instance', False):
            for key, mixin in six.iteritems(MIXINS):
                if isinstance(obj, mixin):
                    kwargs['mixins'].add(key)
        else:
            for key, mixin in six.iteritems(MIXINS):
                if issubclass(obj, mixin):
                    kwargs['mixins'].add(key)

        return kwargs

    needs = ('pure', )

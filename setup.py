from setuptools import setup, find_packages


setup(
    name='sklearn-describe',
    version='0.1dev0',
    packages=find_packages(),
    extras_require={
        'sklearn': ['scikit-learn'],
    },
    entry_points='''
    [sklearn.describe]
    pure = sklearn_describe.pure:PureChecker
    attrs = sklearn_describe.attributes:AttributesChecker
    mixins = sklearn_describe.mixins:MixinsChecker
    ''',
)

from setuptools import setup, find_packages


setup(
    name='sklearn-describe',
    version='0.1dev0',
    packages=find_packages(),
    entry_points='''
    [sklearn.describe]
    pure = sklearn_describe.pure:PureChecker
    attrs = sklearn_describe.attributes:AttributesCheck
    ''',
)

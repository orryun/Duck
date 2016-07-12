from setuptools import setup, find_packages

REQUIRES = ['flask', 'ujson']

setup(
    name="duck_u04",
    version='1.0',
    packages=find_packages(),
    install_requires=REQUIRES
)

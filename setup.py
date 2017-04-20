from setuptools import find_packages
from setuptools import setup
import os

# The version of the wrapped library is the starting point for the
# version number of the python package.
# In bugfix releases of the python package, add a '-' suffix and an
# incrementing integer.
# For example, a packaging bugfix release version 1.4.4 of the
# js.jquery package would be version 1.4.4-1 .

version = '0.0.2-3'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'bootstrap_wysihtml5', 'test_bootstrap_wysihtml5.rst')
    + '\n' +
    read('CHANGES.rst'))

setup(
    name='js.bootstrap_wysihtml5',
    version=version,
    description="Fanstatic packaging of bootstrap_wysihtml5",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Fanstatic Developers',
    author_email='fanstatic@googlegroups.com',
    url='https://github.com/teixas/js.bootstrap_wysihtml5',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'js.bootstrap',
        'js.wysihtml5',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'bootstrap_wysihtml5 = js.bootstrap_wysihtml5:library',
            ],
        },
    )

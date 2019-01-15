#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine


import io
import os
import sys
import glob
from shutil import rmtree
from setuptools import find_packages, setup, Command


here = os.path.abspath(os.path.dirname(__file__))


# Load the package's _meta.py module as a dictionary
meta_file = glob.glob(os.path.join(here, '*', '_meta.py'))[0]
meta = {}
with open(meta_file) as f:
    exec(f.read(), meta)


# What packages are required for this module to be executed?
# which are not in requirements.txt yet
REQUIRED = [
    # 'requests', 'maya', 'records',
]
with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIRED.extend(item.strip() for item in f.readlines())


# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# Import the README and use it as the long-description
readme_file = os.path.join(here, 'README.rst')
try:
    with io.open(readme_file, encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    print('Could not find file: {}'.format(readme_file))
    long_description = meta['_description']


class UploadCommand(Command):
    """Support setup.py upload."""
    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds...')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution...')
        os.system('{0} setup.py sdist bdist_wheel --universal'
                  .format(sys.executable))

        self.status('Uploading the package to PyPI via Twine...')
        os.system('twine upload -r pypi dist/*')

        self.status('Pushing git tags...')
        os.system('git tag v{0}'.format(meta['__version__']))
        os.system('git push --tags')
        
        sys.exit()


# Where the magic happens:
setup(
    name=meta['_package_name'],
    version=meta['__version__'],
    description=meta['_description'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=meta['__author__'],
    author_email=meta['__contact__'],
    python_requires=meta['_python'],
    url=meta['_url'],
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license=meta['_license'],
    classifiers=meta['_classifiers'],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
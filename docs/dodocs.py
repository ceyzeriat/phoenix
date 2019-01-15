#!/usr/bin/env python
# -*- coding: utf-8 -*-

# written by Guillaume Schworer, 2019


import glob
import os
import time


now = time.strftime('%Y_%m_%dx%H_%M_%S')


# Load the package's _meta.py module as a dictionary
base = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
basedoc = os.path.join(base, 'docs')
basemod = os.path.join(base, meta['_package_name'])
meta_file = glob.glob(os.path.join(base, '*', '_meta.py'))[0]
meta = {}
with open(meta_file) as f:
    exec(f.read(), meta)


# remove all old rst
for item in glob.glob(base, 'docs', '*.rst'):
    if item != 'index.rst':
        os.remove(item)
print('Removed old rst files')


# creating rst file
os.system('sphinx-apidoc -o {basedoc} {basemod}{sep} '\
          '{basemod}{sep}tests{sep} {basemod}{sep}example*'\
          .format(basedoc=basedoc, basemod=basemod, sep=os.sep))
print('Created new .rst files')


# compiling
os.system('make html')
os.system('make latexpdf')
print('Compiled into pdf and html')


# zip the html output
os.system('zip -r -0 {basedoc}{sep}_build{sep}html{sep}html.zip *'\
          .format(basedoc=basedoc, sep=os.sep))
cd ../..
print('Created html zip')


# create old docs folder if needed
os.system('mkdir -p {basedoc}{sep}old_docs'
          .format(basedoc=basedoc, sep=os.sep))
os.system('mv {basedoc}{sep}JoystickHTML*.zip {basedoc}{sep}old_docs{sep}'
          .format(basedoc=basedoc, sep=os.sep)

os.system('mv {basedoc}{sep}Joystick*.pdf {basedoc}{sep}old_docs{sep}'
          .format(basedoc=basedoc, sep=os.sep)

print('Moved old documentation to ./old_docs/')


# move the new doc files
os.system('mv {basedoc}{sep}_build{sep}html{sep}html.zip '
          '{basedoc}{sep}JoystickHTML_{now}.zip'
          .format(basedoc=basedoc, sep=os.sep, now=now)))
os.system('mv {basedoc}{sep}_build{sep}latex{sep}joystick.pdf '
          '{basedoc}{sep}Joystick_{now}.pdf'
          .format(basedoc=basedoc, sep=os.sep, now=now)))
print('Copied latest documentation to root\nAll done')

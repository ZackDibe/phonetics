
from setuptools import setup, find_packages
from codecs import open
from os import path

VERSION = '1.0.5'

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='phonetics',

    version=VERSION,

    description='Compute phonetic key of strings for indexing or fuzzy matching',
    long_description=LONG_DESCRIPTION,

    url='https://github.com/Zack--/phonetics',

    author='Zack Dibe',
    author_email='contact@zackdibe.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='phonetics metaphone soundex indexing search fuzzy',

    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
)

try:
    from setuptools import setup
except ImportError:
    from distutils import setup

import scrapylogentries


packages = [
    'scrapylogentries',
]

requires = [
    'scrapy',
    'logentries',
]

setup(
    name='scrapylogentries',
    version=scrapylogentries.__version__,
    description='Scrapy extension to enable logging to Logentries.',
    long_description=open('README.md').read(),
    author='Jean Maynier',
    author_email='jmaynier@kpler.com',
    url='http://github.com/kpler/scrapy-logentries-extension',
    packages=packages,
    install_requires=requires,
    license=open('LICENSE').read(),
    classifiers=(
        'Development Status :: 4 - Beta'
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ),
)

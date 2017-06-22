import sys, os
import setuptools

version = '0.6.8'

setuptools.setup(
    name='ph4-python-whois',
    version=version,
    description="Whois querying and parsing of domain registration information.",
    long_description='',
    install_requires=[
        'future',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
    keywords='whois, python',
    author='Richard Penman',
    author_email='richard@webscraping.com',
    maintainer='Dusan Klinec (ph4r05)',
    maintainer_email='dusan.klinec@gmail.com',
    url='https://github.com/ph4r05/python-whois',
    license='MIT',
    packages=['ph4whois'],
    package_dir={'ph4whois':'ph4whois'},
    extras_require={
        'better date conversion': ["python-dateutil"]
    },
    test_suite='nose.collector',
    tests_require=['nose', 'simplejson'],
    include_package_data=True,
    zip_safe=False
)

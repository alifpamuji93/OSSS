# coding=utf-8

from oss import __version__
from setuptools import setup, find_packages

setup(
    name='oss',
    version=__version__,
    description='One Shock Security System and Linux system information web dashboard',
    long_description='One shock Security System  is a system information for  web dashboard for linux using data mainly served by flask and psutil',
    classifiers=[
        'Topic :: System :: Monitoring',
        'Topic :: System :: Logging',
        'Topic :: System :: Networking :: Monitoring',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators'
    ],
    keywords='Raspberry Pi, smart home, security, Monitoring, linux, web, dashboard',
    author='Nur Wachid, Alif Pamuji',
    author_email='wachid@outlook.com',
    url='https://github.com/alifpamji93/OSSS',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask==0.10.1',
        'psutil==2.1.3',
        'glob2==0.4.1',
        'gevent==1.0.2',
        'zerorpc==0.4.4',
        'netifaces==0.10.4',
        'argparse'
    ],
    test_suite='tests',
    tests_require=['unittest2'],
    entry_points={
        'console_scripts': [
            'oss = oss.run:main'
        ]
    }
)

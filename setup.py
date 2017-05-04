import os
import sys
from setuptools import setup, find_packages

"One shock security system."

if sys.version_info[0] == 2:
    if not sys.version_info >= (2, 7):
        raise ValueError('This package requires Python 2.7 or above')
else:
    raise ValueError('Unrecognized major version of Python')

HERE = os.path.abspath(os.path.dirname(__file__))

# Workaround <http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html>
try:
    import multiprocessing
except ImportError:
    pass

__project__      = 'oss'
__version__      = '1.0.0'
__author__       = 'Nur Wachid'
__author_email__ = 'wachid@outlook.com'
__url__          = 'https://github.com/RPi-Distro/python-gpiozero'
__platforms__    = 'ALL'

__classifiers__ = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Intended Audience :: Developers",
    "Topic :: Education",
    "Topic :: System :: Hardware",
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: PyPy",
]

__keywords__ = [
    'raspberrypi',
    'gpio',
]

__requires__ = [
]

__extra_requires__ = {
    'doc':   ['sphinx'],
    'test':  ['pytest', 'coverage', 'mock'],
}

if sys.version_info[:2] == (3, 2):
    # Particular versions are required for Python 3.2 compatibility
    __extra_requires__['doc'].extend([
        'Jinja2<2.7',
        'MarkupSafe<0.16',
        ])
    __extra_requires__['test'][1] = 'coverage<4.0dev'

__entry_points__ = {
    'gpiozero_pin_factories': [
        'PiGPIOPin  = gpiozero.pins.pigpiod:PiGPIOPin',
        'RPiGPIOPin = gpiozero.pins.rpigpio:RPiGPIOPin',
        'RPIOPin    = gpiozero.pins.rpio:RPIOPin',
        'NativePin  = gpiozero.pins.native:NativePin',
        'MockPin    = gpiozero.pins.mock:MockPin',
        'MockPWMPin = gpiozero.pins.mock:MockPWMPin',
    ],
}


def main():
    import io
    with io.open(os.path.join(HERE, 'README.rst'), 'r') as readme:
        setup(
            name                 = __project__,
            version              = __version__,
            description          = __doc__,
            long_description     = readme.read(),
            classifiers          = __classifiers__,
            author               = __author__,
            author_email         = __author_email__,
            url                  = __url__,
            license              = [
                c.rsplit('::', 1)[1].strip()
                for c in __classifiers__
                if c.startswith('License ::')
            ][0],
            keywords             = __keywords__,
            packages             = find_packages(),
            include_package_data = True,
            platforms            = __platforms__,
            install_requires     = __requires__,
            extras_require       = __extra_requires__,
            entry_points         = __entry_points__,
        )


if __name__ == '__main__':
    main()

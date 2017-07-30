import sys
from distutils.core import setup

if sys.version_info < (3, 2):
    raise NotImplementedError(
        "Sorry, you need at least Python 3.2+ or Python 3.2+ to use jeroboam.")

import jeroboam  # NOQA

setup(name='Jeroboam',
      version=jeroboam.__version__,
      author=jeroboam.__author__,
      author_email=jeroboam.__author_email__,
      license=jeroboam.__license__,
      packages=['jeroboam'],
      long_description=open('README.rst', 'r').read(),
      install_requires=[
          'click>=4.0',
          'Werkzeug>=0.9'
      ],
      entry_points={
          'console_scripts': [
              'jb = jeroboam.cli.management:main'
          ]
      }
      )

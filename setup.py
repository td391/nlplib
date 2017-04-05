from setuptools import setup
setup(name='nlplib',
      install_requires=['langid'],
      extras_require={
        'test': ['pytest'],
      },
      packages=['nlplib'])


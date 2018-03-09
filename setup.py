from setuptools import setup
from pypandoc import convert

setup(name='charpy',
      version='0.0.2',
      description='Render chart from data',
      long_description=convert('README.md', 'rst'),
      url='http://github.com/sylhare/chartapp',
      author='sylhare',
      author_email='sylhare@outlook.com',
      license='MIT',
      packages=['charpy'],
      install_requires=['flask>=0.12'],
      zip_safe=False)

from setuptools import setup, find_packages
from charpy.data_import.io_import import get_readme_rst

setup(name='charpy',
      version='0.4.3',
      description='Render chart from data',
      long_description=get_readme_rst(),
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='flask chart.js web app chart charpy',
      url='http://github.com/sylhare/chartapp',
      author='sylhare',
      author_email='sylhare@outlook.com',
      license='MIT',
      packages=find_packages(exclude=['docs']),
      include_package_data=True,
      install_requires=['flask>=0.12'],
      extras_require={
          'dev': ['pypandoc', 'setuptools'],
          'test': ['coverage==4.1', 'pytest==2.9.2']
      },
      zip_safe=False
      )

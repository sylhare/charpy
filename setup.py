from setuptools import setup, find_packages

setup(name='charpy',
      version='0.0.2',
      description='Render chart from data',
      long_description='README.rst',
      url='http://github.com/sylhare/chartapp',
      author='sylhare',
      author_email='sylhare@outlook.com',
      license='MIT',
      packages=find_packages("charpy", exclude=["test, docs"]),
      install_requires=['flask>=0.12'],
      zip_safe=False)

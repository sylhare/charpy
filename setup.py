from setuptools import setup, find_packages

setup(name                  ='charpy',
      version               ='0.1.2',
      description           ='Render chart from data',
      long_description      ='README.rst',
      classifiers           =[
                              'Development Status :: 3 - Alpha',
                              'License :: OSI Approved :: MIT License',
                              'Programming Language :: Python :: 3.6',
                          ],
      keywords              ='flask chart.js web app chart charpy',
      url                   ='http://github.com/sylhare/chartapp',
      author                ='sylhare',
      author_email          ='sylhare@outlook.com',
      license               ='MIT',
      packages              =find_packages(),
      include_package_data  =True,
      install_requires      =['flask>=0.12'],
      zip_safe              =False)

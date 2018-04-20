Chart App
=========

|PyPI version| |Build Status| |codecov| |Codacy Badge|

This is a web app designed to crunch data into charts.

Demo
----

You can have a demo available at
`localhost:5001 <http://127.0.0.1:5001/>`__

.. code:: bash

    python charpy/app.py

Dependencies
------------

Used for this project:

Python
~~~~~~

-  Flask - base of the microservice (Jinja2 for templating)
-  SQLAlchemy - for database manipulation
-  Pandas - for the dataframe object and data manipulation
-  dateutils - for the date and time parser

Javascript
~~~~~~~~~~

-  Chart.js - for displaying the charts

.. |PyPI version| image:: https://badge.fury.io/py/charpy.svg
   :target: https://badge.fury.io/py/charpy
.. |Build Status| image:: https://travis-ci.org/Sylhare/charpy.svg?branch=master
   :target: https://travis-ci.org/Sylhare/charpy
.. |codecov| image:: https://codecov.io/gh/Sylhare/charpy/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/Sylhare/charpy
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/7ecd2366da08459aa8c7af9c489dc65c
   :target: https://www.codacy.com/app/Sylhare/charpy?utm_source=github.com&utm_medium=referral&utm_content=Sylhare/charpy&utm_campaign=Badge_Grade

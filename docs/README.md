# Chart App

[![PyPI version](https://badge.fury.io/py/charpy.svg)](https://badge.fury.io/py/charpy)
[![Build Status](https://travis-ci.org/Sylhare/charpy.svg?branch=master)](https://travis-ci.org/Sylhare/charpy)
[![codecov](https://codecov.io/gh/Sylhare/charpy/branch/master/graph/badge.svg)](https://codecov.io/gh/Sylhare/charpy)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7ecd2366da08459aa8c7af9c489dc65c)](https://www.codacy.com/app/Sylhare/charpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Sylhare/charpy&amp;utm_campaign=Badge_Grade)

This is a web app designed to crunch data into charts.

## Demo

You can have a demo available at [localhost:5001](http://127.0.0.1:5001/)

```bash
python charpy/factory.py
```

## Dependencies

Used for this project:
 
### Python
 
- Flask - base of the microservice (Jinja2 for templating)
- SQLAlchemy - for SQL database manipulation
- Pandas - for the dataframe object and data manipulation
- dateutils - for the date and time parser

### Javascript

- Chart.js - for displaying the charts
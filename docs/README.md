# Chart App

[![PyPI version](https://badge.fury.io/py/charpy.svg)](https://badge.fury.io/py/charpy)
[![Build Status](https://travis-ci.org/Sylhare/charpy.svg?branch=master)](https://travis-ci.org/Sylhare/charpy)
[![codecov](https://codecov.io/gh/Sylhare/charpy/branch/master/graph/badge.svg)](https://codecov.io/gh/Sylhare/charpy)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7ecd2366da08459aa8c7af9c489dc65c)](https://www.codacy.com/app/Sylhare/charpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Sylhare/charpy&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/ad17a7f76d6421c83b61/maintainability)](https://codeclimate.com/github/Sylhare/charpy/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ad17a7f76d6421c83b61/test_coverage)](https://codeclimate.com/github/Sylhare/charpy/test_coverage)

This is a web app designed to crunch data into charts.
The interesting part is where the data is crunched. 

## Demo

You can have a demo available at [localhost:5001](http://127.0.0.1:5001/)

```bash
python charpy/app.py
```

## Dependencies

Used for this project:
 
### Python
 
- Flask - base of the microservice
- Pandas - for the dataframe object and data manipulation
- dateutils - for the date and time parser

### Javascript

- Chart.js - for displaying the charts
# Charpy

[![PyPI version](https://badge.fury.io/py/charpy.svg)](https://badge.fury.io/py/charpy)
[![Build Status](https://travis-ci.org/Sylhare/charpy.svg?branch=master)](https://travis-ci.org/Sylhare/charpy)
[![codecov](https://codecov.io/gh/Sylhare/charpy/branch/master/graph/badge.svg)](https://codecov.io/gh/Sylhare/charpy)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7ecd2366da08459aa8c7af9c489dc65c)](https://www.codacy.com/app/Sylhare/charpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Sylhare/charpy&amp;utm_campaign=Badge_Grade)

This is a web app designed to crunch data into charts, maybe like a dashboard.

## Release

### Version 1

For this version the goals were:

- Create an API in python that can be customized easily (finding an implenting a framework)
- Provide a flexible api that can render csv files into charts (only basic ones will work)
    - Have the possibility to render more than one chart per page
    - Have the possibility to color the charts automatically
- Provide an endpoint so that you can use http request to get the csv data into json
- Provide an html view of the csv data
- Have a start with SQL compatibilities
- Have all functionality developed using TDD (test driven development) as much as possible

## Demo

You can have a demo available at [localhost:5001](http://127.0.0.1:5001/)

```bash
python charpy/factory.py
```

## Dependencies

Used for this project:
 
### Python
 
- Flask - base of the microservice (Jinja2 for templating)
- SQLAlchemy - for SQL database manipulation (not really implemented at the moment)
- Pandas - for the dataframe object and data manipulation
- dateutils - for the date and time parser

### Javascript

- Chart.js - for displaying the charts

## Other Alternatives

I want to display other alternatives because well, this is a bit missing in feature as of now, 
and you might want to know what is being developed and maintained.

- [plotly - Dash](https://github.com/plotly/dash): flask framework using react and plotpy to display charts in a nice dashboard.
- [anaconda - Bokeh](https://github.com/bokeh/bokeh/) depends on Jinja2 for templating, bokeh server and js library for chart
- [jwkvam - bowtie](https://github.com/jwkvam/bowtie): sockets.io, flask and react to create dashboard
# zeppelin-handy-helpers

Console helper to check, monitor, stop zeppelin paragraph and receive notifications to Slack

[![Build Status](https://travis-ci.org/sbilello/zeppelin-handy-helpers.svg?branch=master)](https://travis-ci.org/sbilello/zeppelin-handy-helpers)
[![CircleCI](https://circleci.com/gh/sbilello/zeppelin-handy-helpers.svg?style=svg)](https://circleci.com/gh/sbilello/zeppelin-handy-helpers)
[![PyPI version](https://badge.fury.io/py/zeppelin-handy-helpers.svg)](https://badge.fury.io/py/zeppelin-handy-helpers)

### Disclaimer

This tool is just a small helper and it is not ready for production yet. It works pretty well for my use cases. Feel free to expand or improve.

### Installation

```
pip install zeppelin-handy-helpers
```

### Usage

```
usage: zhh [-h] [--end_point [END_POINT]]
           [--slack_end_point [SLACK_END_POINT]] [--read] [--check] [--stop]
           [--monitor]

optional arguments:
  -h, --help            show this help message and exit
  --end_point [END_POINT]
                        Specify Zeppelin API end_point
  --slack_end_point [SLACK_END_POINT]
                        Specify Slack Incoming Webhook
  --read                Show all notebook names and ids
  --check               Show all running paragraphs
  --stop                Stop all runnning paragraphs
  --monitor             Monitor all running paragraphs
```


### Examples

```
(demo) ➜  zeppelin-handy-helpers git:(master) ✗ zhh --end_point http://localhost/api/notebook --slack_end_point https://hooks.slack.com/services/XXXXX/XXXX/XXXXX --read
[
    {
        "id": "2CFH4E3TG",
        "name": "OWL"
    },
    {
        "id": "2CF34ERK6",
        "name": "SparkPi"
    },
    {
        "id": "2D62499YH",
        "name": "DemoNotebook"
    }
]

Execution completed
```
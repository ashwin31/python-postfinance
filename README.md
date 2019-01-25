# PostFinance Python Library

[![TravisCI](https://travis-ci.org/niespodd/python-postfinance.svg?branch=master)](https://travis-ci.org/niespodd/python-postfinance.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/niespodd/python-postfinance/badge.svg?branch=master)](https://coveralls.io/github/niespodd/python-postfinance?branch=master)


The PostFinance Python library provides an API for creating payment forms and payment validation according to PostFinance PSP integration guide.

`pip install postfinance`

## Features
* Facilitates creating payment forms by generating form dictionary and field validation (handle `ITEM*xx*` sorting, allowed fields)
* Generates `SHASIGN` according to integration guide (supports `sha1`, `sha256`, `sha512`)

## How to use it?

The example below uses test environment to create a payment form data.

```python
>>> from postfinance import PostFinance, Environment
>>> client = PostFinance(psp_id="clientDEMO", env=Environment.TEST, sha_password="SuperSecret123?!")
>>> client.payments.create("", "12.99", "CHF")
{'LANGUAGE': 'en_US', 'ORDERID': '', 'PSP_ID': 'clientDEMO', 'AMOUNT': 1299, 'CURRENCY': 'CHF', 'SHASIGN': '199acacbaef8417424eeea998e84366cf81c475e'}
```

# Using with Django
tbd


## TODO
* Validate form against [postfinance/constants/sha_in.py](postfinance/constants/sha_in.py) allowed fields
* Create Django form helper
* Add `PostFinance.validator` for sha-out validation

# PostFinance Python Library

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![V](https://img.shields.io/pypi/v/postfinance.svg)]()
[![TravisCI](https://travis-ci.org/niespodd/python-postfinance.svg?branch=master)](https://travis-ci.org/niespodd/python-postfinance.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/niespodd/python-postfinance/badge.svg?branch=master)](https://coveralls.io/github/niespodd/python-postfinance?branch=master)
[![License MIT](https://img.shields.io/github/license/ResidentMario/missingno.svg)](https://github.com/niespodd/python-postfinance/blob/master/LICENSE)

The PostFinance Python library provides an API for creating payment forms and payment validation according to PostFinance PSP integration guide.

*NOTE: This project is not a officially supported by PostFinance or any affiliated organisation*


**Installation:**

`pip install postfinance`

## Integration
This library can be used with popular frameworks like Flask or Django. For more information please refer to
[integration guide](INTEGRATION.md).

## Features
* Natual currency formatting, i.e. `12.00CHF`, `5CHF`, `12.99CHF` - no decimal conversion headache
* Payment form signing including order preservation for `ITEM*XX*` fields and filtering against [SHA-IN allowed parameters list](postfinance/constants/sha_in.py)
* Support for incoming transaction data validation `SHA-OUT`

## Example use
```python
>>> from postfinance import PostFinance
>>> from postfinance.constants Environment
>>> client = PostFinance(psp_id="clientDEMO", env=Environment.PROD, sha_password="SuperSecret123?!")
>>> payment = client.payments.create("", "12.99", "CHF")
>>> payment.url
'https://e-payment.postfinance.ch/ncol/prod/orderstandard_utf8.asp'
>>> payment.form_data
{'LANGUAGE': 'en_US',
 'ORDERID': 'order-1',
 'PSPID': 'clientDEMO',
 'AMOUNT': 1299,
 'CURRENCY': 'CHF',
 'SHASIGN': '29ad8a6946bbca5fcb82197f4dff1145d413ec72'}
```

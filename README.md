# PostFinance Python Library

[![TravisCI](https://travis-ci.org/niespodd/python-postfinance.svg?branch=master)](https://travis-ci.org/niespodd/python-postfinance.svg?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/niespodd/python-postfinance/badge.svg?branch=master)](https://coveralls.io/github/niespodd/python-postfinance?branch=master)


The PostFinance Python library provides an API for creating payment forms and payment validation according to PostFinance PSP integration guide.

## How to use it?

The example below uses test environment to create a payment form data.

```python
from postfinance import (
    PostFinance, ENV_TEST
)

client = PostFinance(psp_id="clientDEMO", env=ENV_TEST, sha_password="SuperSecret123?!")
payment_form = client.payments.create(
    order_id="", amount="12.99", currency="CHF"
)

print(payment_form)


```

## TODO
* Validate form against [postfinance/constants/sha_in.py](postfinance/constants/sha_in.py) allowed fields
* Create Django form helper
* Add `PostFinance.validator` for sha-out validation

# Integration guide

A typical scenario assumes you are running an e-commerce system where people can purchase items or services. 

There is a data model representing orders that holds customer information along with order value and payment currency.

```python
from django.db import models 

class Order(models.Model):
    id = models.UUIDField()
    # (...) customer information
    total_value = models.DecimalField()
```

Once an order is created the user have to be forwarded to the PostFinance gateway to make the payment.

First, the application has to create a PostFinance instance.
```python
pf = PostFinance(psp_id='XX-YY', sha_password='SecretSig123?!')
```

Secondly, it has to provide a view where the payment form will be generated. 

(tbd)
import logging
from decimal import Decimal

from iso4217 import Currency

from .constants import (
    SHA_IN_ALLOWED_FIELDS_RE,
)
from .utils import dict_to_ordered_qs
from .config import PostFinanceConfig
from .exceptions import (
    PaymentAmountInvalidException,
)


class PostFinancePayments(object):
    def __init__(self, config: PostFinanceConfig):
        self._config = config

    def create(self, order_id: str, amount: str, currency: str, extra_config: dict = None) -> dict:
        currency = currency.upper()
        extra_config = {k.upper(): v for k, v in extra_config.items()} if extra_config else {}
        form_fields = {
            "LANGUAGE": self._config.language,
            **self._config.extra_config,
            **extra_config,
            "ORDERID": order_id,
            "PSPID": self._config.psp_id,
            "AMOUNT": self._amount_to_int(amount, currency),
            "CURRENCY": currency,
        }
        sha_sign = self._sign_fields(form_fields)
        form_fields.update({"SHASIGN": sha_sign})
        return form_fields

    def _sign_fields(self, fields_dict: dict) -> str:
        fields_dict = {k: v for k, v in fields_dict.items() if SHA_IN_ALLOWED_FIELDS_RE.match(k)}
        fields_str = dict_to_ordered_qs(fields_dict, self._config.sha_password).encode('utf-8')
        return self._config.sha_method(fields_str).hexdigest()

    @staticmethod
    def _amount_to_int(amount: str, currency: str) -> int:
        try:
            iso_currency = Currency(currency.upper())
            amount_flt = Decimal(amount.replace(",", "."))
            amount_flt = amount_flt * pow(10, iso_currency.exponent)
            if amount_flt % 1 > 0:
                raise PaymentAmountInvalidException("The provided amount has too many decimal places.")
            return int(amount_flt)
        except ValueError:
            logging.warning("`{}` currency has not been recognized. Make sure the provided value is correct.".format(currency))
            return int(amount)

from unittest import TestCase
from mock import patch

from hashlib import (
    sha1, sha256, sha512
)

from postfinance.config import (
    PostFinanceConfig,
)
from postfinance.exceptions import PaymentAmountInvalidException
from postfinance.payments import PostFinancePayments


class PaymentsTestCase(TestCase):
    def setUp(self):
        self._config = PostFinanceConfig(psp_id="AAA", sha_password="BBB")
        self._builder = PostFinancePayments(self._config)

    def test_values_correctly_formatted(self):
        payment = self._builder.create("test_order", "12.5", "pln")

        assert payment.get("CURRENCY") == "PLN"
        assert payment.get("AMOUNT") == 1250

    def test_amount_converts_to_nonfloating_int(self):
        payment = self._builder.create("test_order", "1234.56", "EUR")

        self.assertEqual(payment.get("AMOUNT"), 123456)

    def test_amount_various_formats(self):
        for _format in ["1234.56", "1234,56"]:
            payment = self._builder.create("test_order", _format, "EUR")
            assert payment.get("AMOUNT") == int(123456)

    @patch('logging.warning')
    def test_warn_about_invalid_currency(self, mock):
        self._builder.create("test_order", "5", "INEXISTS")

        self.assertTrue(mock.called)

    def test_throws_when_amount_decimals_mismatch(self):
        with self.assertRaises(PaymentAmountInvalidException):
            self._builder.create("test_order", "5.1234567890", "USD")

    def test_supply_extra_config_to_payment(self):
        payment = self._builder.create("test_order", "15", "EUR", {
            "title": "That was a payment!"
        })

        self.assertEqual(payment.get("TITLE"), "That was a payment!")


class PaymentsSigningTestCase(TestCase):
    def test_payment_has_signature(self):
        payment = self._get_builder(sha1).create("test_order", "15", "PLN")

        self.assertIn("SHASIGN", payment)

    def test_payment_signature_alternative_alg(self):
        test_algos = (
            (sha1, "9cace149459a28c56b578a96eea7dd5e227d3c81"),
            (sha256, "4b85896aa526906d51a13e59435782ff24beaaef0dd403ac8a4b0573889e882a"),
            (sha512, "380737af181bda5cbd63529b837d7acb06443a2d07cc987c8f57293257617098"
                     "518be5adc707337b430940917c37307d218ea5dadcb155dd91ab7c1450742a2a"),
        )

        for sig_method, sig_exp_out in test_algos:
            builder = self._get_builder(sig_method)
            payment = builder.create("test_order", "15", "PLN")

            self.assertEqual(payment.get("SHASIGN"), sig_exp_out)

    @staticmethod
    def _get_builder(sig_method):
        _config = PostFinanceConfig(psp_id="AAA", sha_password="BBB", sha_method=sig_method)
        return PostFinancePayments(_config)


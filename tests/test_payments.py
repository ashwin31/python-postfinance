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

        assert payment.form_data.get("CURRENCY") == "PLN"
        assert payment.form_data.get("AMOUNT") == 1250

    def test_amount_converts_to_nonfloating_int(self):
        payment = self._builder.create("test_order", "1234.56", "EUR")

        self.assertEqual(payment.form_data.get("AMOUNT"), 123456)

    def test_amount_various_formats(self):
        for _format in ["1234.56", "1234,56"]:
            payment = self._builder.create("test_order", _format, "EUR")
            assert payment.form_data.get("AMOUNT") == int(123456)

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

        self.assertEqual(payment.form_data.get("TITLE"), "That was a payment!")


class PaymentsSigningTestCase(TestCase):
    def test_payment_has_signature(self):
        payment = self._get_builder(sha1).create("test_order", "15", "PLN")

        self.assertIn("SHASIGN", payment.form_data)

    def test_payment_signature_alternative_alg(self):
        test_algos = (
            (sha1, "6ad88229a6d229b1a69a1200ebaa3aaf66a5fb9b"),
            (sha256, "e31c867a1835c1a3658532f15ca10511a70686c66ae56ad40883bea01ce0a2a4"),
            (sha512, "14d017e0f78f944793d206c4a30f7703c011cd610242648b0acc3a6c0dfd5804"
                     "a45a93b24d67d73f444b6f10fa06b1715bfa8445c1f048f624e27653cd94bb4d"),
        )

        for sig_method, sig_exp_out in test_algos:
            builder = self._get_builder(sig_method)
            payment = builder.create("test_order", "15", "PLN")

            self.assertEqual(payment.form_data.get("SHASIGN"), sig_exp_out)

    def test_payment_signature_doesnt_include_unallowed_fields(self):
        builder = self._get_builder(sha1)
        p_1 = builder.create("order1", "15", "CHF")
        p_2 = builder.create("order1", "15", "CHF", extra_config={"RANDOM": "FIELD"})

        self.assertEqual(p_1.form_data.get("SHASIGN"), p_2.form_data.get("SHASIGN"))
        self.assertEqual(p_2.form_data.get("RANDOM"), "FIELD")

    @staticmethod
    def _get_builder(sig_method):
        _config = PostFinanceConfig(psp_id="AAA", sha_password="_", sha_method=sig_method)
        return PostFinancePayments(_config)


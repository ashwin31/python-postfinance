from unittest import TestCase

from postfinance import PostFinance
from postfinance.constants import Environment
from postfinance.payments import PostFinancePayments


class PostFinanceTestCase(TestCase):
    def test_submodules_are_accessible(self):
        client = PostFinance(psp_id="A", sha_password="B")

        self.assertTrue(hasattr(client, "payments"))
        self.assertIsInstance(client.payments, PostFinancePayments)

    def test_update_extra_config_with_a_title(self):
        client = PostFinance(psp_id="A", sha_password="B")
        client.configure({"TITLE": "A Shop Payments"})

        payment = client.payments.create("test_order", "15", "CHF")

        self.assertEqual(payment.get("TITLE"), "A Shop Payments")

    def test_url_updates_for_non_test_env(self):
        client = PostFinance(psp_id="A", sha_password="B", env=Environment.PROD)

        self.assertEqual(client._base_config.url, Environment.get_env_url(Environment.PROD))

from unittest import TestCase

from postfinance.constants import SHA_IN_ALLOWED_FIELDS_RE, Environment


class ConstantsShaInTestCase(TestCase):
    def test_sha_in_regex_compiles(self):
        self.assertTrue(SHA_IN_ALLOWED_FIELDS_RE.match("PSPID"))


class ConstantsEnvironmentTestCase(TestCase):
    def test_gets_url_according_to_env(self):
        self.assertIn("/prod/", Environment.get_env_url(Environment.PROD))
        self.assertIn("/test/", Environment.get_env_url(Environment.TEST))

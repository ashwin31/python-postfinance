from enum import Enum


class Environment(Enum):
    TEST = "test"
    PROD = "prod"

    @staticmethod
    def get_env_url(env: 'Environment') -> str:
        return ENV_URLS.get(env)


ENV_URLS = {
    Environment.TEST: "https://e-payment.postfinance.ch/ncol/test/orderstandard_utf8.asp",
    Environment.PROD: "https://e-payment.postfinance.ch/ncol/prod/orderstandard_utf8.asp"
}



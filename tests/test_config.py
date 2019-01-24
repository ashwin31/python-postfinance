from postfinance.config import PostFinanceConfig
from postfinance.constants import (
    Environment,
)


def test_default_config_values():
    test_config = PostFinanceConfig(psp_id="a", sha_password="b")
    assert test_config.env == Environment.TEST
    assert test_config.url == Environment.get_env_url(
        Environment.TEST
    )

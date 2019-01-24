from .config import PostFinanceConfig
from .payments import PostFinancePayments

from .constants import Environment


class PostFinance(object):
    def __init__(self, psp_id: str, sha_password: str, env: Environment = None, default_lang: str = None, **kwargs):
        _kwargs = kwargs.copy()
        _kwargs.update({"psp_id": psp_id, "sha_password": sha_password, "language": default_lang or "en_US"})
        if env:
            env_url = Environment.get_env_url(env)
            kwargs.update({"env": "env", "url": env_url})

        self._base_config = PostFinanceConfig(**_kwargs)
        self.payments = PostFinancePayments(self._base_config)

    def configure(self, extra_config: dict) -> None:
        self._base_config.extra_config.update(
            extra_config
        )

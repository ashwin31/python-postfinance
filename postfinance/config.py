from typing import NamedTuple, Optional

from hashlib import (
    sha1,
)
from .constants import Environment


class PostFinanceConfig(NamedTuple):
    psp_id: str
    sha_password: str

    language: str = "en_US"
    env: Environment = Environment.TEST
    url: str = Environment.get_env_url(
        Environment.TEST
    )
    sha_method: callable = sha1
    extra_config: dict = dict()

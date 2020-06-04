"""PurplShip UPS connection settings."""

import attr
from purplship.carriers.ups.utils import Settings as BaseSettings


@attr.s(auto_attribs=True)
class Settings(BaseSettings):
    """UPS connection settings."""

    username: str
    password: str
    access_license_number: str
    account_number: str = None
    id: str = None
    test: bool = False
    carrier_name: str = "UPS"
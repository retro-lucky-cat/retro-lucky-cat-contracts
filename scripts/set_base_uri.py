from brownie import (
    RetroCats,
)

from scripts.helpful_scripts import get_account


def set_interval():
    account = get_account()
    retro_cats = RetroCats[-1]
    tx = retro_cats._setBaseURI(
        "https://us-central1-retro-cats.cloudfunctions.net/retro-cats-function-rinkeby?token_id=",
        {"from": account},
    )
    tx.wait(1)


def main():
    set_interval()

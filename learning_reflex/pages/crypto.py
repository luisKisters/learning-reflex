import reflex as rx
from typing import Literal


class CryptoState(rx.State):
    cryptoName: str = ""
    currency: Literal["USD", "EUR"] = "USD"
    timeFrameStr: Literal["1D", "3D", "1W", "2W", "1M", "6M", "1Y"]


@rx.page(route="/crypto")
def crypto() -> rx.Component:
    return rx.container(
        rx.heading("See the course of all your favourite crypto coins"),
    )

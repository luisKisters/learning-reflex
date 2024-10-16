"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
import requests as r
from .pages import joke, crypto


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.heading("Hello World!")


app = rx.App()
app.add_page(index)
app.add_page(crypto.crypto)
app.add_page(joke.joke)

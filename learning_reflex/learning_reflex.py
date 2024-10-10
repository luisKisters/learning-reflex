"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
import requests as r
import time


class State(rx.State):
    """The app state."""

    ...


class JokeState(rx.State):
    joke: str = ""
    loading: bool = False

    @rx.background
    async def get_joke(self):
        async with self:
            self.loading = True
            print("self.loading", self.loading)
            res = r.get("https://v2.jokeapi.dev/joke/Pun?format=txt&type=single")
            print("res", res.content)
            self.joke = res.content.decode("utf-8")
            time.sleep(10)  # Consider using asyncio.sleep instead
            print("self.joke", self.joke)
            self.loading = False
            print("self.loading", self.loading)

    async def log_loading(self):
        print(self.loading)


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Hello World!", size="9"),
            rx.box(
                rx.heading("Jokes", size="9"),
                rx.flex(
                    rx.button(
                        "Get Joke",
                        loading=JokeState.loading,
                        on_click=JokeState.get_joke(),
                    ),
                    rx.text(JokeState.loading),
                    rx.button("Check loading state", on_click=JokeState.log_loading()),
                ),
            ),
        ),
        rx.text(JokeState.joke, font_size="2em"),
        # rx.text(JokeState.joke, hidden=JokeState.joke == ""),
    )


app = rx.App()
app.add_page(index)

import asyncio
import reflex as rx
import requests as r

import time


class JokeState(rx.State):
    joke: str = ""
    loading: bool = False
    error: str = ""

    async def get_joke(self):
        self.loading = True
        yield
        try:
            res = r.get(
                "https://v2.jokeapi.dev/joke/Pun?format=txt&type=single"
            ).content.decode("utf-8")
            self.joke = res
        except Exception as e:
            print(e)
            self.error = str(e)
        finally:
            self.loading = False
            yield


@rx.page(route="/login")
def joke() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.box(
                rx.heading("Jokes", size="9"),
                rx.button(
                    "Get Joke",
                    loading=JokeState.loading,
                    on_click=JokeState.get_joke(),
                ),
            ),
        ),
        rx.text(JokeState.joke, font_size="2em"),
        rx.text(JokeState.error, font_size="2em"),
    )

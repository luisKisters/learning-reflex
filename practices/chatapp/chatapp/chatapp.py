"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )


def chat() -> rx.Component:
    qa_pairs = [
        ("What is reflex?", "A way to build web apps in pure python!"),
        (
            "What can I make with it?",
            "Anything simple from a simple website to a complex web app!",
        ),
        (
            "How do you advertise a thing you build?",
            "By constantly advertising it in the docs!",
        ),
    ]

    return rx.box(*[qa(question, answer) for question, answer in qa_pairs])


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.container(chat())


app = rx.App()
app.add_page(index)

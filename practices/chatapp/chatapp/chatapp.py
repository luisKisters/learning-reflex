"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from chatapp import style


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, style=style.question_style, text_align="right"),
        rx.box(answer, style=style.answer_style, text_align="left"),
        margin_y="1em",
        width="100%",
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


def action_bar():
    return rx.hstack(
        rx.input(placeholder="What is your question?", style=style.input_style),
        rx.button("Ask", style=style.button_style),
    )


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.center(rx.vstack(chat(), action_bar(), align="center"))


app = rx.App()
app.add_page(index)

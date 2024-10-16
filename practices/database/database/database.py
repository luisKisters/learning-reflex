"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    name: str
    description: str
    price: float

    def add_product(self):
        with rx.session() as session:
            session.add(
                Product(
                    name=self.name,
                    description=self.description,
                    price=self.price,
                )
            )
            session.commit()
            print("Product added, name: ", self.name)


class Product(rx.Model, table=True):
    name: str
    description: str
    price: float


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        rx.heading("add product"),
        rx.input(value=State.name, on_change=State.set_name),
        rx.input(value=State.description, on_change=State.set_description),
        rx.input(value=State.price, on_change=State.set_price),
        rx.button("add product", on_click=State.add_product()),
    )


app = rx.App()
app.add_page(index)

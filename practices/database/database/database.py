"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class Product(rx.Model, table=True):
    name: str
    description: str
    price: float


class State(rx.State):
    name: str
    description: str
    price: float
    products: list[Product] = []

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

    def get_products(self):
        with rx.session() as session:
            self.products = session.exec(Product.select()).all()


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        rx.heading("add product"),
        rx.input(value=State.name, on_change=State.set_name),
        rx.input(value=State.description, on_change=State.set_description),
        rx.input(value=State.price, on_change=State.set_price),
        rx.button("add product", on_click=State.add_product()),
        rx.heading("products"),
        rx.foreach(
            State.products,
            lambda product: rx.text(
                f"{product.name} {product.description} {product.price}"
            ),
        ),
        rx.button("get products", on_click=State.get_products()),
    )


app = rx.App()
app.add_page(index)

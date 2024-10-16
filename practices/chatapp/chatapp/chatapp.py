"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

import time
from pages import chatapp_doc_example


class State(rx.State):
    msg_content: str
    username: str
    # chat_history: list[
    #     dict["msg":str, "user":str, "date":str]
    # ]  # TODO: CONVERT THIS TO A FKN DICT RIGHT?
    chat_history: list[dict[str, str, str]]

    def send_msg(self, msg, usr):
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        # self.chat_history.append("msg": msg, "user": usr, "date": date)
        if msg == "" or usr == "":
            yield rx.toast("Message or Sender is  empty")
        else:
            self.chat_history.append({"msg": msg, "user": usr, "date": date})
            print("message send")
            # print("msg:", self.msg_content, self.username)
            print({"msg": msg, "user": usr, "date": date})
            print("current chat history")
            self.msg_content = ""
            print(self.msg_content)
            yield
        # self.username = ""


def chat() -> rx.Component:
    return rx.box(
        # rx.text(State.chat_history),
        rx.foreach(State.chat_history, lambda msg: chat_msg(msg)),
        input(),
    )
    # result: [["test msg","test sender","2024-10-14 19:39:15"],["","test sender","2024-10-14 19:39:17"],["","test sender","2024-10-14 19:39:17"],["","test sender","2024-10-14 19:39:17"],["","test sender","2024-10-14 19:39:17"],["","test sender","2024-10-14 19:39:18"],["","test sender","2024-10-14 19:39:18"],["","test sender","2024-10-14 19:40:03"],["test msgasdasdsad","test sender","2024-10-14 19:40:08"]]


def chat_msg(msg: dict[str, str, str]) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text(
                    msg["msg"],
                    background_color=rx.cond(
                        msg["user"] == State.username,
                        "blue",
                        "green",
                    ),
                    padding="12px",
                    border_radius="10px",
                ),
                rx.flex(rx.text(msg["user"]), rx.text(msg["date"]), spacing="3"),
            ),
        )
    )


def input() -> rx.Component:
    return rx.hstack(
        rx.input(
            "Write a message",
            on_change=State.set_msg_content,
            value=State.msg_content,
        ),
        rx.input("Input username", on_change=State.set_username, value=State.username),
        rx.button(
            "Submit Message",
            on_click=lambda: State.send_msg(State.msg_content, State.username),
        ),
        width="100%",
    )


def index() -> rx.Component:
    return rx.hstack(chat())


app = rx.App()
app.add_page(chatapp_doc_example.chatapp)
app.add_page(index)

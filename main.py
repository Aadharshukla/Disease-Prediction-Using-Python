import flet as ft
import threading
from chatbot import get_response

def main(page: ft.Page):
    page.title = "Disease Prediction System"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 1000
    page.window.height = 700
    page.padding = 20

    title = ft.Text("Disease Prediction System", size=30, weight=ft.FontWeight.BOLD)
    subtitle = ft.Text("AI Powered Medical Assistant", size=18, color=ft.Colors.BLUE_300)

    chat_area = ft.ListView(expand=True, spacing=10, auto_scroll=True)

    user_input = ft.TextField(
        hint_text="Describe your symptoms...",
        expand=True,
        border_radius=15
    )

    send_button = ft.Button("Send", icon=ft.Icons.SEND)

    def get_ai_reply(user_text, thinking_msg):
        bot_reply = get_response(user_text)
        thinking_msg.value = f"🤖 AI: {bot_reply}"
        send_button.disabled = False
        page.update()

    def send_message(e):
        if user_input.value.strip() == "":
            return

        user_text = user_input.value
        chat_area.controls.append(ft.Text(f"🧑 You: {user_text}"))

        thinking_msg = ft.Text("🤖 AI: Thinking...")
        chat_area.controls.append(thinking_msg)

        user_input.value = ""
        send_button.disabled = True
        page.update()

        threading.Thread(target=get_ai_reply, args=(user_text, thinking_msg), daemon=True).start()

    send_button.on_click = send_message

    page.add(
        title,
        subtitle,
        ft.Divider(),
        chat_area,
        ft.Row([user_input, send_button])
    )

ft.run(main)
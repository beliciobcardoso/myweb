import flet as ft

import os
import dotenv
import time

dotenv.load_dotenv(dotenv.find_dotenv())

def main(page: ft.Page):
    user_login = os.getenv("USER_LOGIN")
    password_login = os.getenv("PASSWORD_LOGIN")
    
    page.scroll = "adaptive"
    page.title = "AppBar Example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    icon = ft.Image(src="icon.png", width=100, height=100)
    logo = ft.Image(src="logo.png", width=150, height=150)

    def close_dlg(e):
        page_login.open = False
        page.update()

    button_close_modal = ft.ElevatedButton("Cancelar", on_click=close_dlg)

    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    def update_page():
        page.update()
        time.sleep(5)
        page.snack_bar.open = False

    def login(e):
        user = input_user.value
        password = input_password.value

        if user == user_login and password == password_login:
            page.remove(container)
            page_login.open = False
            input_user.value = ""
            input_password.value = ""
            page.snack_bar = ft.SnackBar(ft.Text("Login efetuado com sucesso", size=30, color="white"), bgcolor="green")
            page.snack_bar.open = True
            page.add(container2)
            page.add(container)
            update_page()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha inválidos", size=30, color="white"), bgcolor="red")
            page.snack_bar.open = True
            input_user.value = ""
            input_password.value = ""
            update_page()
            

    input_user = ft.TextField(label="Usuário")
    input_password = ft.TextField(label="Senha", password=True)
    button_login = ft.ElevatedButton("Login", on_click=login)

    input_column = ft.Column([input_user, input_password])

    container_input = ft.Container(
        content=input_column, 
        alignment=ft.alignment.center, 
        width=300, 
        height=150
    )    

    page_login = ft.AlertDialog(
        modal=True,
        title=ft.Text("Login"), 
        content=container_input,
        actions=[button_login, button_close_modal], 
        actions_alignment=ft.MainAxisAlignment.END
    )

    def page_login_open(e):
        page.dialog = page_login
        page_login.open = True
        page.update()


    page.appbar = ft.AppBar(
        leading=logo,
        leading_width=100,
        title=ft.Text("AppBar Example"),
        center_title=False,
        toolbar_height=70,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.WHITE54,
        actions=[
            ft.Text(" "), 
            ft.ElevatedButton("Login", on_click=page_login_open),
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
        
    titulo = ft.Text("AppBar Example")
    titulo2 = ft.Text("Container 2")

    texto = ft.Text("This is an example of an AppBar with a title, leading icon, actions and a popup menu button.")

    column = ft.Column(
        [titulo, texto, logo],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    container = ft.Container(
        padding=20,
        content=column,
    )
    
    container2 = ft.Container(
        padding=20,
        content=titulo2,
    )

    page.add(container)

ft.app(main, view=ft.WEB_BROWSER, web_renderer=ft.WebRenderer.HTML)

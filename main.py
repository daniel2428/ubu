import flet as ft

def main(page: ft.Page):
    page.title = 'My first app'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text('Hello, world!')


    greeting_history = []
    history_text = ft.Text("История приветствий:", style='bodyMedium')


    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f'Hello, {name}!'
            greet_button.text = 'Click me again!'
            name_input.value = ''

            greeting_history.append(name)
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

            
        else:
            greeting_text.value = 'Please enter your name!'

        page.update()
    name_input = ft.TextField(label='Enter your name', autofocus=True, on_submit=on_button_click)    

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Theme change", on_click=toggle_theme)

        
        # greeting_text.value = f'Hello, {name_input.value}!'
        # page.update()

    greet_button = ft.ElevatedButton('Click me!', on_click=on_button_click)

    page.add(ft.Row([theme_button]),
              greeting_text, 
              name_input, 
              greet_button,
              history_text,)

ft.app(target=main)

# ft.app(target=main, view=ft.WEB_BROWSER)
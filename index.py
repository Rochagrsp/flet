import flet as ft

def main(page: ft.Page):
    def clicar(e):
         texto.value= "App flet"
         page.update()

    texto = ft.Text("Usando o Flet")
    botao =ft.ElevatedButton("Clique Aqui",on_click=clicar)
       

    page.add(texto, botao)

ft.app(target=main)

import flet as ft

def main(page: ft.Page):

    page.title="Calculadora"
    numero1=ft.TextField(label="Primeiro Numero")
    numero2=ft.TextField(label="Segundo Numero")

    

    resultado=ft.Text("Resultado:")

    def calcular():
       n1= float(numero1.value)
       n2= float(numero2.value)

       


    page.add(numero1,numero2,resultado)


ft.app(target=main)
import flet as ft

def main(page: ft.Page):

    page.title="Calculadora"
    numero1=ft.TextField(label="Primeiro Numero")
    numero2=ft.TextField(label="Segundo Numero")

    

    resultado=ft.Text("Resultado:")

    def calcular(e):
       n1= float(numero1.value)
       n2= float(numero2.value)
    

       operacao = operacoes.value

       if operacao == '+':
           conta= n1+n2
       elif operacao=="-":
           conta=n1-n2
       elif operacao=="*":
           conta=n1*n2
       elif operacao=="/":
           conta=n1/n2  

       resultado.value=f"Resultado:{conta}" 
       page.update()

           

    operacoes = ft.Dropdown(
            label='Escolha a operação',
            options=[
                ft.dropdown.Option("+"),
                ft.dropdown.Option("-"),
                ft.dropdown.Option("*"),
                ft.dropdown.Option("/"),
           ]
       )
    botao=ft.ElevatedButton(
        "Calcular",
        on_click=calcular
    )

    page.add(numero1,
             numero2,
             resultado,
             operacoes,
             botao)


ft.app(target=main)
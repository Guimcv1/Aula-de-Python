import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE

    product_images = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(
                    src='https://a-static.mlcdn.com.br/1500x1500/controle-para-xbox-one-xbox-series-xs-e-pc-sem-fio-microsoft-preto/magazineluiza/231216200/f9b38ae15b9ca0eb0a3a7b96866317f6.jpg'
                )
            ]
        )
    )

    product_details = ft.Container()

    layout = ft.Container(
        width=800,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.Colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[

            ]
        )
)

if __name__ == '__main__':
    ft.app(target=main)
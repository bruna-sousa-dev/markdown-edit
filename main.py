import flet as ft

class App:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.padding = 0
        self.page.title = 'Markdown Editor'
        self.main()

    def main(self):

        def update_view(e):
            view.value = editor.value
            view.update()
        
        editor = ft.TextField(
            multiline = True,
            min_lines = 15,
            max_lines = 15,
            color = ft.colors.WHITE60,
            content_padding = ft.padding.all(30),
            border = ft.InputBorder.NONE,
            bgcolor = ft.colors.BLUE_GREY,
            on_change = update_view,
            cursor_color = ft.colors.BLACK54,
            hint_text = 'Digite aqui...',
        )

        how_to = ft.Container(
            expand = True,
            padding = ft.padding.all(30), 
            content = ft.Column(
                scroll = ft.ScrollMode.ALWAYS,
                controls = [
                    ft.Text(value = 'Para criar títulos em diferentes tamanhos', weight = ft.FontWeight.BOLD, color = ft.colors.BLACK),
                    ft.Text(value = '# H1', color = ft.colors.GREY_700),
                    ft.Text(value = '## H2', color = ft.colors.GREY_700),
                    ft.Text(value = '### H3', color = ft.colors.GREY_700),
                    ft.Divider(color = ft.colors.GREY, height = 40),

                    ft.Text(value = 'Para formatar o estilo do texto', weight = ft.FontWeight.BOLD, color = ft.colors.BLACK),
                    ft.Text(value = '**Texto em negrito**', color = ft.colors.GREY_700),
                    ft.Text(value = '*Texto em itálico*', color = ft.colors.GREY_700),
                    ft.Text(value = '~~Texto tachado~~', color = ft.colors.GREY_700),
                    ft.Divider(color = ft.colors.GREY, height = 40),

                    ft.Text(value = 'Para criar listas', weight = ft.FontWeight.BOLD, color = ft.colors.BLACK),
                    ft.Text(value = '1. Ordenada', color = ft.colors.GREY_700),
                    ft.Text(value = '- Desordenada', color = ft.colors.GREY_700),
                    ft.Divider(color = ft.colors.GREY, height = 40),

                    ft.Text(value = 'Inserir links e imagens', weight = ft.FontWeight.BOLD, color = ft.colors.BLACK),
                    ft.Text(value = '[Texto do link](https://programadoraventureiro.com)', color = ft.colors.GREY_700),
                    ft.Text(value = '![Label da imagem](image.jpg)', color = ft.colors.GREY_700),
                    ft.Divider(color = ft.colors.GREY, height = 40),

                    ft.Text(value = 'Para inserir código', weight = ft.FontWeight.BOLD, color = ft.colors.BLACK),
                    ft.Text(value = '`print("Código em uma linha")`', color = ft.colors.GREY_700),
                    ft.Text(value = '```\nprint("Código em mútiplas linhas") \n```', color = ft.colors.GREY_700),
                ],
            ),
        )

        view = ft.Markdown(
            value = editor.value,
            selectable = True,
            extension_set = ft.MarkdownExtensionSet.GITHUB_WEB,
            code_theme = 'monokai-sublime',
            on_tap_link = lambda e: self.page.launch_url(e.data),
        )

        layout = ft.Row(
            expand = True,
            spacing = 0,
            vertical_alignment = ft.CrossAxisAlignment.STRETCH,
            controls = [
                ft.Container(
                    expand = True,
                    bgcolor = ft.colors.WHITE,
                    content = ft.Column(
                        controls = [
                            editor,
                            how_to,
                        ],
                    ),
                ),
                ft.Container(
                    expand = True,
                    bgcolor = ft.colors.BLACK,
                    padding = ft.padding.all(30),
                    content = view,
                ),
            ]
        )

        self.page.add(layout)

ft.app(target = App, assets_dir = 'assets')

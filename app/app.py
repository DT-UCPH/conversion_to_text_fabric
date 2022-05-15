from tf.advanced.app import App


class TfApp(App):
    def __init__(app, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def fmt_layoutRich(app, n, **kwargs):
        api = app.api
        F = api.F
        material = F.text.v(n) or ""
        layout = f'<span class="gap">{material}</span>' if material
        return f"{layout} "
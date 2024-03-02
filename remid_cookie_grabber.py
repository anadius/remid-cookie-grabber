from functools import partialmethod

import webview


SUCCESS = (
    '<div>Your <code>remid</code> cookie:<br><input value="{}" size="40">'
    "<br>Press <code>Ctrl+A</code> to select the whole text,<br>"
    "then press <code>Ctrl+C</code> to copy it.</div>"
)
FAILURE = (
    "<div>Could not find the <code>remid</code> cookie. "
    "Make sure to log in with email and password.</div>"
)
COOKIES_URL = "https://accounts.ea.com/connect"
MAIN_URL = "https://www.ea.com"
SIGNIN_URL = "https://signin.ea.com/p/juno/login"


class Manager():
    def __init__(self):
        self.window = webview.create_window(
            "remid cookie grabber",
            f"{MAIN_URL}/login",
            width=550,
            height=700,
        )
        self.window.events.loaded += self.on_load

        webview.start()

    def on_load(self):
        url = self.window.get_current_url()
        if url is None:
            return
        elif url.startswith(MAIN_URL):
            self.window.hide()
            self.window.load_url(COOKIES_URL)
        elif url.startswith(COOKIES_URL):
            remid = None
            for cookie in self.window.get_cookies():
                for x in cookie.values():
                    if x.key == "remid":
                        remid = x.value

            if remid is None:
                html = FAILURE
            else:
                html = SUCCESS.format(remid)

            self.window.load_html(html)
            self.window.resize(550, 180)
            self.window.show()
        elif url.startswith(SIGNIN_URL):
            if self.window.dom.get_element("head") is None:
                self.window.hide()
                return
            if self.window.dom.get_element("body") is None:
                self.window.hide()
                return


_ = Manager()

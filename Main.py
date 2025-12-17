from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import socket

class IPApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=40, spacing=20)
        self.label = Label(text="Butona bas")
        btn = Button(text="IP GÖSTER")
        btn.bind(on_press=self.show_ip)
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def show_ip(self, *args):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
        except:
            ip = "Bulunamadı"
        self.label.text = f"IP: {ip}"

IPApp().run()

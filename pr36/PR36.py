from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500,700)

# Designate Our .kv design file
Builder.load_file('calc.kv')

class MyLayout(Widget):
    calc_input = ObjectProperty(None)  # Добавляем ObjectProperty для текстового поля

    def clear(self):
        self.calc_input.text = '0'

    def on_button_press(self, button):
        if button.text == '=':
            self.calc_input.text = str(eval(self.calc_input.text))
        elif button.text == 'C':
            self.calc_input.text = self.calc_input.text[:-1]
        else:
            if self.calc_input.text == '0':
                self.calc_input.text = ''
            self.calc_input.text += button.text

class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()

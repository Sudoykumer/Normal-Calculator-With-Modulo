from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/', '%', '**', '//']
        
        # BoxLayout to hold the result and the buttons
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Result TextInput for displaying the calculation result
        self.result = TextInput(font_size=48, readonly=True, halign='right', multiline=False,
                                size_hint_y=None, height="150dp", background_color=(1, 1, 1, 1),
                                foreground_color=(0, 0, 0, 1))
        
        # Add the result TextInput to the layout
        layout.add_widget(self.result)

        # Create the buttons for the calculator
        button_grid = GridLayout(cols=4, padding=10, spacing=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            '**', '(', ')', '%',
            '//', '.', 'Del', 'Exit'
        ]
        
        for button in buttons:
            button_widget = Button(text=button, size_hint=(None, None), size=("100dp", "100dp"),
                                   background_normal='', background_color=(0, 0, 0, 1),  # Black background
                                   color=(1, 1, 1, 1), font_size=80)  # White text and font size 80
            button_widget.bind(on_press=self.on_button_press)
            button_grid.add_widget(button_widget)

        # Add the button grid to the layout
        layout.add_widget(button_grid)

        return layout
    
    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ""
        elif button_text == 'Del':
            self.result.text = current[:-1]
        elif button_text == 'Exit':
            App.get_running_app().stop()
        elif button_text == '=':
            try:
                self.result.text = str(eval(current))
            except Exception as e:
                self.result.text = 'Error'
        else:
            self.result.text = current + button_text

if __name__ == '__main__':
    CalculatorApp().run()

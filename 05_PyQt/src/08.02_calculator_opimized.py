import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class CalculatorApp(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("08.02_calculator.ui", self)
        self.setWindowTitle('Calculator')
        self.current_input = ""
        self.connect_buttons()

    def connect_buttons(self):
        buttons = {
            "btn_0": self.input_digit, "btn_1": self.input_digit, "btn_2": self.input_digit,
            "btn_3": self.input_digit, "btn_4": self.input_digit, "btn_5": self.input_digit,
            "btn_6": self.input_digit, "btn_7": self.input_digit, "btn_8": self.input_digit,
            "btn_9": self.input_digit, "btn_plus": self.input_operation, "btn_minus": self.input_operation,
            "btn_multiply": self.input_operation, "btn_divide": self.input_operation,
            "btn_AC": self.clear_display, "btn_CE": self.clear_last_entry, "btn_dot": self.input_dot,
            "btn_sign": self.change_sign, "btn_equal": self.calculate_result
        }
        for btn_name, btn_action in buttons.items():
            getattr(self, btn_name).clicked.connect(btn_action)

    def input_digit(self):
        button = self.sender()
        self.current_input += button.text()
        self.textBrowser.setText(self.current_input)

    def input_operation(self):
        button = self.sender()
        if self.current_input and self.current_input[-1].isdigit():
            self.current_input += f" {button.text()} "
            self.textBrowser.setText(self.current_input)

    def change_sign(self):
        if self.current_input and (self.current_input[-1].isdigit() or self.current_input[-1] == '.'):
            self.current_input = self.current_input[1:] if self.current_input.startswith('-') else '-' + self.current_input
            self.textBrowser.setText(self.current_input)

    def clear_display(self):
        self.current_input = ""
        self.textBrowser.clear()

    def clear_last_entry(self):
        self.current_input = self.current_input[:-1]
        self.textBrowser.setText(self.current_input)

    def input_dot(self):
        if not self.current_input or (self.current_input and self.current_input[-1] not in "+-*/"):
            self.current_input += "."
            self.textBrowser.setText(self.current_input)

    def calculate_result(self):
        try:
            result = eval(self.current_input)
            self.textBrowser.setText(str(result))
            self.current_input = str(result)
        except Exception as e:
            self.textBrowser.setText('Error')
            self.current_input = ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())

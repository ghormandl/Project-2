from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QComboBox, QHBoxLayout
from PyQt6.QtCore import Qt
from logic import CalculatorLogic

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 600)
        self.layout = QVBoxLayout()
        self.result_label = QLineEdit(self)
        self.result_label.setPlaceholderText("")
        self.result_label.setReadOnly(True)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.result_label)
        self.mode_layout = QHBoxLayout()
        self.mode_button = QPushButton("Mode", self)
        self.mode_button.clicked.connect(self.toggle_mode)
        self.mode_layout.addWidget(self.mode_button)
        self.geometry_controls = QComboBox(self)
        self.geometry_controls.addItems(['Square Area', 'Rectangle Area', 'Circumference'])
        self.geometry_controls.setVisible(False)
        self.mode_layout.addWidget(self.geometry_controls)
        self.layout.addLayout(self.mode_layout)
        self.grid_layout = QGridLayout()
        self.buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
            ('C', 4, 0)
        ]
        for text, row, col in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_clicked)
            self.grid_layout.addWidget(button, row, col)

        self.layout.addLayout(self.grid_layout)
        self.calculator_logic = CalculatorLogic()
        self.is_geometry_mode = False
        self.setLayout(self.layout)

    def toggle_mode(self):
        """Toggle between basic calculator and geometry mode."""
        self.is_geometry_mode = not self.is_geometry_mode

        if self.is_geometry_mode:
            self.result_label.setPlaceholderText("Enter dimension(s)")
            self.geometry_controls.setVisible(True)
            self.clear_input()
        else:
            self.result_label.setPlaceholderText("")
            self.geometry_controls.setVisible(False)
            self.clear_input()

    def button_clicked(self):
        """Handles the button click events."""
        button_text = self.sender().text()

        if button_text == 'C':
            self.clear_input()
        elif button_text == '=':
            if self.is_geometry_mode:
                self.calculate_geometry()
            else:
                self.result_label.setText(self.calculator_logic.evaluate_expression())
        else:
            if self.is_geometry_mode:
                self.result_label.setText(self.result_label.text() + button_text)
            else:
                self.result_label.setText(self.calculator_logic.update_input(button_text))

    def clear_input(self):
        """Clear the result label and reset the internal state."""
        self.result_label.setText("")
        self.calculator_logic.clear_input()

    def calculate_geometry(self):
        """Calculate area or circumference based on current mode (Square Area, Rectangle Area, Circumference)."""
        shape = self.geometry_controls.currentText()
        dimension_input = self.result_label.text()

        try:
            dimensions = list(map(float, dimension_input.split(',')))
        except ValueError:
            self.result_label.setText("Invalid input")
            return

        if shape == "Square Area":
            if len(dimensions) == 1:
                self.result_label.setText(str(self.calculator_logic.square_area(dimensions[0])))
            else:
                self.result_label.setText("Invalid input for Square. Enter side length.")
        elif shape == "Rectangle Area":
            if len(dimensions) == 2:
                self.result_label.setText(str(self.calculator_logic.rectangle_area(dimensions[0], dimensions[1])))
            else:
                self.result_label.setText("Invalid input for Rectangle. Enter length,width.")
        elif shape == "Circumference":
            if len(dimensions) == 1:
                self.result_label.setText(str(self.calculator_logic.circumference(dimensions[0])))
            else:
                self.result_label.setText("Invalid input for Circumference. Enter radius.")
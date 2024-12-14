import sys
from PyQt6.QtWidgets import QApplication
from gui import Calculator

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
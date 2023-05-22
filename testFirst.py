
import sys

from PySide6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
widget = QWidget()
widget.setWindowTitle("Hello, PySide6")
widget.resize(300, 300)
widget.show()
sys.exit(app.exec())
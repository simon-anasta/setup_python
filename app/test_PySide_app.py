# PySide app - simple window and close button
#
# not available for Python 3.14
#

from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

class TestApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test App")
        self.setGeometry(100, 100, 300, 200)

        # Create a close button
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.close_app)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(close_button)
        self.setLayout(layout)

    def close_app(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    test_app = TestApp()
    test_app.show()
    sys.exit(app.exec_())

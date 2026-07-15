import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl


class TeaMachineApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tea Machine Monitoring")
        self.resize(1400, 850)

        browser = QWebEngineView()
        browser.setUrl(QUrl("http://127.0.0.1:8000"))

        self.setCentralWidget(browser)


app = QApplication(sys.argv)

window = TeaMachineApp()
window.show()

sys.exit(app.exec())
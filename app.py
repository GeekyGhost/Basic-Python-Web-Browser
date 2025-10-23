import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl  # <-- ADD THIS LINE

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Web Browser")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com")) 

        # Navigation bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.go_button = QPushButton("Go")
        self.go_button.clicked.connect(self.navigate_to_url)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.go_button)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url)) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())
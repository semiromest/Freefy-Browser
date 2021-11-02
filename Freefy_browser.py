from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QToolBar, QAction, QLineEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #navbar
        navbar  = QToolBar()
        self.addToolBar(navbar)

        #back button
        bck_btn = QAction('Back',self)
        bck_btn.triggered.connect(self.browser.back)
        navbar.addAction(bck_btn)

        #forward button
        forward_button = QAction('Forward',self)
        forward_button.triggered.connect(self.browser.forward)
        navbar.addAction(forward_button)

        #reload button
        reload_button = QAction('Reload',self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        #home page button
        home_button=QAction('Home',self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        # my github page button
        github_button=QAction('Github',self)
        github_button.triggered.connect(self.navigate_github)
        navbar.addAction(github_button)

        #urlbar
        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com.tr'))
    def navigate_github(self):
        self.browser.setUrl(QUrl("https://github.com/semiromest"))
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self,q):
        self.url_bar.setText(q.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName("Freefy Browser")
    window = MainWindow()
    sys.exit(app.exec())



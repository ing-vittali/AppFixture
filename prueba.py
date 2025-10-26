from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton,
    QAction, QMessageBox
)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo PySide6 - QMainWindow")

        # Widget central
        central = QWidget()
        layout = QVBoxLayout(central)
        btn_close = QPushButton("Cerrar")
        btn_close.clicked.connect(self.close)
        layout.addWidget(btn_close)
        self.setCentralWidget(central)

        # Menús
        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(self.close)
        about_action = QAction("Acerca de", self)
        about_action.triggered.connect(self.show_about)

        file_menu = self.menuBar().addMenu("Archivo")
        file_menu.addAction(exit_action)
        help_menu = self.menuBar().addMenu("Ayuda")
        help_menu.addAction(about_action)

        # Barra de estado
        self.statusBar().showMessage("Listo")

    def show_about(self):
        QMessageBox.information(self, "Acerca de", "Ejemplo PySide6\nEjecutando en devcontainer")

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
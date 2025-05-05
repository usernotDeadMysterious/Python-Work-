from PySide6.QtWidgets import QApplication, QLabel

# Create the application instance
app = QApplication([])

# Create a simple label
label = QLabel("Hello, PySide6!")
label.show()

# Run the application event loop
app.exec()
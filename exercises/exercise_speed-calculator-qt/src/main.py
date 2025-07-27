import sys
from PyQt6.QtWidgets import (QComboBox, QGridLayout, QPushButton, QWidget, QApplication, 
                             QLineEdit, QLabel)


class AverageSpeed(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours): ")
        self.time_line_edit = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(["Metric (km)", "Imperial (miles)"])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_avg)
        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0)
        
        self.setLayout(grid)

    def calculate_avg(self):

        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())

        speed = distance/time
        
        if self.unit_combo.currentText() == "Metric (km)":
            speed = round(speed, 2)
            self.output_label.setText(f"Average speed is {speed}km/h")
        else:
            speed = round(speed * 0.621371, 2)
            self.output_label.setText(f"Average speed is {speed}miles/h")
        

app = QApplication(sys.argv)
avg_speed = AverageSpeed()
avg_speed.show()
sys.exit(app.exec())


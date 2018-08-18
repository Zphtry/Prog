from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox, QHBoxLayout, QRadioButton, QVBoxLayout, \
    QComboBox, QSpinBox, QLabel
import sys


def list_to_strings(strs):
    return list(map(lambda x: str(x), strs))


def titled_widget(title, widget):
    vbox = QVBoxLayout()
    vbox.addWidget(QLabel(title))
    vbox.addWidget(widget)
    return vbox


class Layout(QWidget):

    def config(self):
        self.config_checkbox = QCheckBox('Config')
        self.layout.addWidget(self.config_checkbox)

    def mode_radio(self):
        self.fu1 = QRadioButton("FU1")
        self.controls.addWidget(self.fu1)

        self.fu2 = QRadioButton("FU2")
        self.controls.addWidget(self.fu2)

        self.fu3 = QRadioButton("FU3")
        self.controls.addWidget(self.fu3)

        self.fu4 = QRadioButton("FU4")
        self.controls.addWidget(self.fu4)

    def baudrate_select(self):
        self.baud_rate_combobox = QComboBox()
        self.baud_rate_combobox.addItems(list_to_strings([1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]))
        self.controls.addLayout(titled_widget('Baud rate', self.baud_rate_combobox))

    def channel(self):
        self.channel_spinbox = QSpinBox()
        self.channel_spinbox.setMaximum(127)
        self.controls.addLayout(titled_widget('Channel', self.channel_spinbox))

    def address(self):
        self.address_spinbox = QSpinBox()
        self.address_spinbox.setMaximum(255)
        self.layout.addLayout(titled_widget('Address', self.address_spinbox))

    def power(self):
        self.power_combobox = QComboBox()
        self.power_combobox.addItems(list_to_strings(range(1, 9)))
        self.controls.addLayout(titled_widget('Power', self.power_combobox))

    def switch_controls(self, state: bool):
        self.fu1.setEnabled(state)
        self.fu2.setEnabled(state)
        self.fu3.setEnabled(state)
        self.fu4.setEnabled(state)

        self.baud_rate_combobox.setEnabled(state)
        self.channel_spinbox.setEnabled(state)
        self.address_spinbox.setEnabled(state)
        self.power_combobox.setEnabled(state)

    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.controls = QHBoxLayout()

        self.config()
        self.layout.addLayout(self.controls)

        self.mode_radio()
        self.baudrate_select()
        self.channel()
        self.address()
        self.power()

        self.config_checkbox.stateChanged.connect(lambda x: self.switch_controls(x > 0))

        self.get_params_button = QPushButton('Get params')
        self.layout.addWidget(self.get_params_button)

        self.read_all = QPushButton('Read all')
        self.layout.addWidget(self.read_all)

        self.setLayout(self.layout)
        self.show()

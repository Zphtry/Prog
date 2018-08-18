import sys

from PyQt5.QtWidgets import QApplication

import layout
from serial import Serial


ser = Serial('/dev/ttyACM0', 9600)


def read_all():
    print(ser.read_all().decode('utf-8'))

# ser.close()
read_all()
# ser.write(b'config.enable')
# ser.close()


def enable_config():
    ser.write(b'config.enable')
    read_all()


def disable_config():
    ser.write(b'config.disable')
    read_all()


def config_handler(i):
    if i > 0: enable_config()
    elif i == 0: disable_config()



app = QApplication(sys.argv)
gui = layout.Layout()

gui.config_checkbox.stateChanged.connect(config_handler)


def get_params():
    ser.write(b'AT+RX')
    read_all()



gui.get_params_button.clicked.connect(get_params)
gui.read_all.clicked.connect(read_all)

sys.exit(app.exec_())

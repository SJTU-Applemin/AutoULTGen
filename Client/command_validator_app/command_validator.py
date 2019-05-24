import sys
from PySide2.QtUiTools import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ui_mainwindow import Ui_MainWindow
from ui_form import Ui_Form
from lxml import etree
import webgenxml


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonGen.clicked.connect(self.generate_xml)
        self.ui.pushButtonBspec.clicked.connect(self.generate_from_bspec)
        self.ui.pushButtonRef.clicked.connect(self.show_command_info)

        self.command_info = []
        self.command_xml = 'test.xml'
        self.test_class_name = ''
        self.read_command_info_from_xml()

        self.form = Form()
        self.form.setObjectName(self.test_class_name)

        # self.show_command_info()

    @Slot()
    def generate_from_bspec(self):
        url = self.ui.lineEditURL.text()
        webgenxml.webgen(url)
        self.ui.logBrowser.append('Get infomation from ' + url + '\n')



    def load_vesc_ring_info(self):
        vesc_ring_info = {}

    @Slot()
    def show_command_info(self):
        # self.form.ui = Form()
        # self.form.ui.setupUi(self.form)
        i_row = 0
        table = self.form.ui.cmdTable
        print(self.command_info)
        for command in self.command_info:
            fields_n = len(command['fields'])
            table.setSpan(i_row, 0, fields_n, 1)
            table.setItem(i_row, 0, QTableWidgetItem(command['name']))

            for key, value in command['fields'].items():
                print(i_row)
                if i_row >= self.form.ui.cmdTable.rowCount():
                    self.form.ui.cmdTable.insertRow(i_row)
                table.setItem(i_row, 1, QTableWidgetItem(key))
                checkBox = QCheckBox()

                checkBox.setCheckState(Qt.CheckState.Checked)
                checkBox.stateChanged.connect(self.check_box_change)
                table.setCellWidget(i_row, 3, checkBox)
                table.setItem(i_row, 2, QTableWidgetItem(value['defalt_value']))
                table.setItem(i_row, 4, QTableWidgetItem(value['Address']))
                table.setItem(i_row, 5, QTableWidgetItem(value['min_value']))
                table.setItem(i_row, 6, QTableWidgetItem(value['max_value']))
                i_row += 1
        table.resizeColumnsToContents()
        table.resizeRowsToContents()
        self.form.show()


    @Slot(int)
    def check_box_change(self, row_id):
        print(row_id)

    def read_command_info_from_xml(self):
        tree = etree.parse(self.command_xml)
        root = tree.getroot()[0]
        self.test_class_name = root.get('name')
        for command in root:
            info = {'name': command.get('name'), 'fields': {}}
            for dword in command:
                for field in dword:
                    info['fields'][field.tag] = {}
                    for key, value in field.items():
                        info['fields'][field.tag][key] = value
            self.command_info.append(info)
        self.ui.logBrowser.append('Read infomation from ' + self.command_xml + '\n')


    @Slot()
    def generate_xml(self):
        if not self.command_info:
            pass
        lines = ['<?xml version="1.0"?>']
        lines.append('<class name="' + self.test_class_name + '">\n')
        for cmd in self.command_info:
            lines.append('    <cmd name="' + cmd['name'] + '">\n')
            for field_name, values in cmd['fields'].items():
                s = '        <' + field_name
                for key, value in values.items():
                    s = s + ' ' + key + '="' + str(value) + '"'
                s = s + '/>\n'
                lines.append(s)
            lines.append('    </cmd>\n')
            lines.append('</class>\n')
        file_name = self.ui.lineEditOut.text()
        with open(file_name, 'w') as fout:
            fout.writelines(lines)
        self.ui.logBrowser.append('Generating modified command xml\n')


class Form(QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.info = []
        self.ui.pushButtonSave.clicked.connect(self.save)

    @Slot()
    def save(self):
        info = []
        table = self.ui.cmdTable
        cmds = set()
        for i in range(table.rowCount()):
            cmd_name = str(table.item(i, 0))
            if cmd_name not in cmds:
                cmds.add(cmd_name)
                info.append({'name': cmd_name, 'fields': {}})
            if table.cellWidget(i, 3).checkState():
                field_name = str(table.item(i, 1))
                info[-1]['fields'][field_name] = {}
                info[-1]['fields']['defalt_value'] = str(table.item(i, 2))
                info[-1]['fields']['Address'] = str(table.item(i, 4))
                info[-1]['fields']['min_value'] = str(table.item(i, 5))
                info[-1]['fields']['max_value'] = str(table.item(i, 6))
        self.info = info


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

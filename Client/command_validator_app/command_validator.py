import sys
import os
import re
import shutil
from PySide2.QtUiTools import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ui_mainwindow import Ui_mainWindow
# from ui_form import Ui_Form
from ui_command_info import Ui_FormCommandInfo
from ui_inputwindow import Ui_InputWindow
from lxml import etree
from htoxml.cmdfinder import CmdFinder
import webgenxml
import copy
from functools import partial
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonGAll.clicked.connect(self.GAll)
        #self.ui.pushButtonGAll.clicked.connect(self.read_command_info_from_xml)

        self.media_path = ''
        self.command_info = []
        self.command_tags = ('DW0_dwlen', 'class', 'def_dwSize', 'index', 'input_dwsize', 'name')
        self.dword_tags = ('NO', 'value', 'class', 'cmdarraysize', 'otherCMD')
        self.command_filter = {'MI_NOOP_CMD', 'MI_NOOP'}
        self.ringinfo_path = ''
        self.output_path = ''
        self.command_xml = ''
        self.test_name = ''
        self.platform = ''
        self.frame_num = 0
        self.row_num = 0

        self.form = FormCommandInfo(self)
        
        #
        self.ui.SelectMediaPath.clicked.connect(partial(self.selectpath,'Media'))
        self.ui.SelectRinginfoPath.clicked.connect(partial(self.selectpath,'Ringinfo'))
        self.ui.SelectDDIInputPath.clicked.connect(partial(self.selectpath,'DDIInput'))

        self.ui.lineEditMediaPath.setText(r'C:\Users\jiny\gfx\gfx-driver\Source\media')
        self.ui.lineEditDDIInputPath.setText(r'C:\projects\github\AutoULTGen\command_validator_app2\command_validator_app\vcstringinfo\HEVC-VDENC-Grits001-2125\DDI_Input')
        self.ui.lineEditRinginfoPath.setText(r'C:\projects\github\AutoULTGen\command_validator_app2\command_validator_app\vcstringinfo\HEVC-VDENC-Grits001-2125\VcsRingInfo')
        self.typeinputpara = InputWindow(self)

    
    @Slot()
    def generate_from_bspec(self):
        url = self.ui.lineEditURL.text()
        webgenxml.webgen(url)
        self.ui.logBrowser.append('Get infomation from ' + url + '\n')

    def load_vesc_ring_info(self):
        vesc_ring_info = {}
        pass

    @Slot()
    def show_command_table(self, item, column = 0):
        self.form.current_item = item
        if item.data(2, 1):
            idx = item.data(2, 1)
            if idx['cmd_idx'] == 'all':
                self.form.current_frame = self.command_info[idx['frame_idx']]
                self.form.current_command = 'all'
                command_list = self.command_info[idx['frame_idx']]
            else:
                self.form.current_frame = self.command_info[idx['frame_idx']]
                self.form.current_command = self.command_info[idx['frame_idx']][idx['cmd_idx']]
                command_list = [self.command_info[idx['frame_idx']][idx['cmd_idx']]]

            table = self.form.ui.tableWidgetCmd
            table.clearContents()
            self.form.row_command_map = []
            table.setRowCount(0)
            i_row = 0

            for command_idx, command in enumerate(command_list):
                print('command ' + str(command_idx) + '\n')
                QCoreApplication.processEvents()
                # fields_num = 0
                # for dword in command['dwords']:
                #     for key in dword:
                #         if key != 'value' and key != 'unmappedstr':
                #             fields_num += 1

                # print(command)
                # print(fields_num)
                # print(i_row)

                if i_row >= table.rowCount():
                    table.insertRow(i_row)
                table.setItem(i_row, 0, QTableWidgetItem(command['name']))
                for dword_idx, dword in enumerate(command['dwords']):
                    print('dword ' + str(dword_idx) + '\n')
                    QCoreApplication.processEvents()
                    if 'unmappedstr' in dword and dword['unmappedstr']:
                        continue
                    if i_row >= table.rowCount():
                        table.insertRow(i_row)
                    table.setItem(i_row, 1, QTableWidgetItem('dword' + dword['NO']))
                    if not dword['fields']:
                        if dword['value']:
                            table.setItem(i_row, 3, QTableWidgetItem(dword['value']))
                        self.form.row_command_map.append(
                            {'frame_idx': idx['frame_idx'], 'command_idx': command['index'], 'dword_idx': dword_idx})
                        i_row += 1

                    for field in dword['fields']:
                        QCoreApplication.processEvents()
                        if field['field_name'].startswith('Obj'):
                            if i_row >= table.rowCount():
                                table.insertRow(i_row)
                            table.setItem(i_row, 1, QTableWidgetItem('dword' + dword['NO'] + '_' + field['field_name']))
                            for obj_field in field['obj_fields']:
                                if obj_field['obj_field_name'].startswith('Reserved') and self.form.ui.checkBoxReserved.isChecked():
                                    continue
                                if i_row >= table.rowCount():
                                    table.insertRow(i_row)
                                table.setItem(i_row, 2, QTableWidgetItem(obj_field['obj_field_name']))
                                checkBox = QCheckBox()
                                if not obj_field['obj_field_name'].startswith('Reserved') and item.checkState(0) == Qt.CheckState.Checked:
                                    checkBox.setCheckState(Qt.CheckState.Checked)
                                checkBox.stateChanged.connect(self.check_box_change)
                                table.setCellWidget(i_row, 5, checkBox)
                                if self.form.mode == 'bin':
                                    table.setItem(i_row, 3, QTableWidgetItem(bin(int(obj_field['default_value'], 16))))
                                    table.setItem(i_row, 4, QTableWidgetItem(bin(int(obj_field['default_value'], 16))))
                                    table.setItem(i_row, 7, QTableWidgetItem(bin(int(obj_field['min_value'], 16))))
                                    table.setItem(i_row, 8, QTableWidgetItem(bin(int(obj_field['max_value'], 16))))
                                elif self.form.mode == 'dec':
                                    table.setItem(i_row, 3, QTableWidgetItem(str(int(obj_field['default_value'], 16))))
                                    table.setItem(i_row, 4, QTableWidgetItem(str(int(obj_field['default_value'], 16))))
                                    table.setItem(i_row, 7, QTableWidgetItem(str(int(obj_field['min_value'], 16))))
                                    table.setItem(i_row, 8, QTableWidgetItem(str(int(obj_field['max_value'], 16))))
                                else:
                                    table.setItem(i_row, 3, QTableWidgetItem(obj_field['default_value']))
                                    table.setItem(i_row, 4, QTableWidgetItem(obj_field['default_value']))
                                    table.setItem(i_row, 7, QTableWidgetItem(obj_field['min_value']))
                                    table.setItem(i_row, 8, QTableWidgetItem(obj_field['max_value']))
                                if 'Address' in field:
                                    table.setItem(i_row, 6, QTableWidgetItem(obj_field['Address']))
                                else:
                                    table.setItem(i_row, 6, QTableWidgetItem('N'))
                                table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                                table.setItem(i_row, 9, QTableWidgetItem(obj_field['bitfield_l']))
                                table.setItem(i_row, 10, QTableWidgetItem(obj_field['bitfield_h']))
                                table.item(i_row, 9).setFlags(Qt.NoItemFlags)
                                table.item(i_row, 10).setFlags(Qt.NoItemFlags)
                                self.form.row_command_map.append(
                                    {'frame_idx': idx['frame_idx'], 'command_idx': command['index'],
                                     'dword_idx': dword_idx})
                                i_row += 1
                            continue

                        if field['field_name'].startswith('Reserved') and self.form.ui.checkBoxReserved.isChecked():
                            continue

                        if i_row >= table.rowCount():
                            table.insertRow(i_row)
                        table.setItem(i_row, 2, QTableWidgetItem(field['field_name']))
                        checkBox = QCheckBox()
                        if not field['field_name'].startswith('Reserved') and item.checkState(0) == Qt.CheckState.Checked:
                            checkBox.setCheckState(Qt.CheckState.Checked)
                        checkBox.stateChanged.connect(self.check_box_change)
                        table.setCellWidget(i_row, 5, checkBox)
                        if self.form.mode == 'bin':
                            table.setItem(i_row, 3, QTableWidgetItem(bin(int(field['default_value'], 16))))
                            table.setItem(i_row, 4, QTableWidgetItem(bin(int(field['default_value'], 16))))
                            table.setItem(i_row, 7, QTableWidgetItem(bin(int(field['min_value'], 16))))
                            table.setItem(i_row, 8, QTableWidgetItem(bin(int(field['max_value'], 16))))
                        elif self.form.mode == 'dec':
                            table.setItem(i_row, 3, QTableWidgetItem(str(int(field['default_value'], 16))))
                            table.setItem(i_row, 4, QTableWidgetItem(str(int(field['default_value'], 16))))
                            table.setItem(i_row, 7, QTableWidgetItem(str(int(field['min_value'], 16))))
                            table.setItem(i_row, 8, QTableWidgetItem(str(int(field['max_value'], 16))))
                        else:
                            table.setItem(i_row, 3, QTableWidgetItem(field['default_value']))
                            table.setItem(i_row, 4, QTableWidgetItem(field['default_value']))
                            table.setItem(i_row, 7, QTableWidgetItem(field['min_value']))
                            table.setItem(i_row, 8, QTableWidgetItem(field['max_value']))
                        table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                        if 'Address' in field:
                            table.setItem(i_row, 6, QTableWidgetItem(field['Address']))
                        else:
                            table.setItem(i_row, 6, QTableWidgetItem('N'))
                        table.setItem(i_row, 9, QTableWidgetItem(field['bitfield_l']))
                        table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                        table.setItem(i_row, 10, QTableWidgetItem(field['bitfield_h']))
                        table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                        self.form.row_command_map.append({'frame_idx': idx['frame_idx'],'command_idx': command['index'], 'dword_idx': dword_idx})
                        i_row += 1
                    # for key, value in dword.items():
                    #     if key.startswith('Obj'):
                    #         print(key)
                    #         if i_row >= table.rowCount():
                    #             table.insertRow(i_row)
                    #         table.setItem(i_row, 1, QTableWidgetItem('dword' + dword['NO'] + '_' + key))
                    #         for obj_key, obj_value in value.items():
                    #             if obj_key.startswith('Reserved') and self.form.ui.checkBoxReserved.isChecked():
                    #                 continue
                    #             if i_row >= table.rowCount():
                    #                 table.insertRow(i_row)
                    #             table.setItem(i_row, 2, QTableWidgetItem(obj_key))
                    #             checkBox = QCheckBox()
                    #             if not obj_key.startswith('Reserved'):
                    #                 checkBox.setCheckState(Qt.CheckState.Checked)
                    #             checkBox.stateChanged.connect(self.check_box_change)
                    #             table.setCellWidget(i_row, 5, checkBox)
                    #             table.setItem(i_row, 3, QTableWidgetItem(obj_value['default_value']))
                    #             table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                    #             table.setItem(i_row, 4, QTableWidgetItem(obj_value['default_value']))
                    #             table.setItem(i_row, 6, QTableWidgetItem(obj_value['Address']))
                    #             table.setItem(i_row, 7, QTableWidgetItem(obj_value['min_value']))
                    #             table.setItem(i_row, 8, QTableWidgetItem(obj_value['max_value']))
                    #             table.setItem(i_row, 9, QTableWidgetItem(obj_value['bitfield_l']))
                    #             table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                    #             table.setItem(i_row, 10, QTableWidgetItem(obj_value['bitfield_h']))
                    #             table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                    #             i_row += 1
                    #         continue
                    #
                    #     if key == 'value' or key == 'unmappedstr' or key == 'NO':
                    #         continue
                    #     if key.startswith('Reserved') and self.form.ui.checkBoxReserved.isChecked():
                    #         continue
                    #     # print(i_row)
                    #     if i_row >= table.rowCount():
                    #         table.insertRow(i_row)
                    #     table.setItem(i_row, 2, QTableWidgetItem(key))
                    #     checkBox = QCheckBox()
                    #     if not key.startswith('Reserved'):
                    #         checkBox.setCheckState(Qt.CheckState.Checked)
                    #     checkBox.stateChanged.connect(self.check_box_change)
                    #     table.setCellWidget(i_row, 5, checkBox)
                    #     table.setItem(i_row, 3, QTableWidgetItem(value['default_value']))
                    #     table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                    #     table.setItem(i_row, 4, QTableWidgetItem(value['default_value']))
                    #     table.setItem(i_row, 6, QTableWidgetItem(value['Address']))
                    #     table.setItem(i_row, 7, QTableWidgetItem(value['min_value']))
                    #     table.setItem(i_row, 8, QTableWidgetItem(value['max_value']))
                    #     table.setItem(i_row, 9, QTableWidgetItem(value['bitfield_l']))
                    #     table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                    #     table.setItem(i_row, 10, QTableWidgetItem(value['bitfield_h']))
                    #     table.item(i_row, 3).setFlags(Qt.NoItemFlags)
                    #     self.form.row_command_map.append({'frame_idx': idx['frame_idx'],'command_idx': command['index'], 'dword_idx': dword_idx})
                    #     i_row += 1
            table.resizeColumnsToContents()
            table.resizeRowsToContents()

    @Slot()
    def show_command_info(self):
        # self.form.ui = Form()
        # self.form.ui.setupUi(self.form)
        self.dw_length_check()
        self.form.setWindowTitle(self.test_name)
        tree = self.form.ui.treeWidgetCmd
        tree.itemDoubleClicked.connect(self.form.save)
        tree.itemDoubleClicked.connect(self.show_command_table)
        tree.itemClicked.connect(self.form.save)
        tree.itemClicked.connect(self.show_command_table)
        tree.itemChanged.connect(self.form.update_tree_checkstate)
        test = QTreeWidgetItem(tree)
        test.setText(0, self.test_name)
        for frame_idx in range(len(self.command_info)):
            frame = QTreeWidgetItem(test)
            frame.setText(0, 'frame' + str(frame_idx))
            frame.setData(2, 1, {'frame_idx': frame_idx, 'cmd_idx': 'all'})
            for command_idx, command in enumerate(self.command_info[frame_idx]):
                # print(command_idx)
                cmd = QTreeWidgetItem(frame)
                cmd.setText(0, command['name'])
                if command['name'] in self.command_filter:
                    cmd.setCheckState(0, Qt.CheckState.Unchecked)
                else:
                    cmd.setCheckState(0, Qt.CheckState.Checked)
                cmd.setData(2, 1, {'frame_idx': frame_idx, 'cmd_idx': command_idx})
                for dword_idx in range(len(command['dwords'])):
                    dword = QTreeWidgetItem(cmd)
                    dword.setText(0, 'dword' + command['dwords'][dword_idx]['NO'])
                    dword.setCheckState(0, Qt.CheckState.Checked)
                    for field_obj in command['dwords'][dword_idx]['fields']:
                        field = QTreeWidgetItem(dword)
                        if 'field_name' in field_obj:
                            field.setText(0, field_obj['field_name'])


        # for command in self.command_info:
        #     fields_num = 0
        #     for dword in command['dwords']:
        #         for key in dword:
        #             if key != 'value' and key != 'unmappedstr':
        #                 fields_num += 1
        #     # print(command)
        #     # print(fields_num)
        #     # print(i_row)
        #     if i_row >= self.form.ui.cmdTable.rowCount():
        #         self.form.ui.cmdTable.insertRow(i_row)
        #
        #     table.setItem(i_row, 0, QTableWidgetItem(command['name']))
        #     for dword in command['dwords']:
        #         for key, value in dword.items():
        #             if key == 'value' or key == 'unmappedstr':
        #                 continue
        #             # print(i_row)
        #             if i_row >= self.form.ui.cmdTable.rowCount():
        #                 self.form.ui.cmdTable.insertRow(i_row)
        #             table.setItem(i_row, 1, QTableWidgetItem(key))
        #             checkBox = QCheckBox()
        #
        #             checkBox.setCheckState(Qt.CheckState.Checked)
        #             checkBox.stateChanged.connect(self.check_box_change)
        #             table.setCellWidget(i_row, 3, checkBox)
        #             table.setItem(i_row, 2, QTableWidgetItem(value['default_value']))
        #             table.setItem(i_row, 4, QTableWidgetItem(value['Address']))
        #             table.setItem(i_row, 5, QTableWidgetItem(value['min_value']))
        #             table.setItem(i_row, 6, QTableWidgetItem(value['max_value']))
        #             i_row += 1
        # table.resizeColumnsToContents()
        # table.resizeRowsToContents()
        self.form.show()


    @Slot(int)
    def check_box_change(self, row_id):
        print(row_id)

    def parse_command_file(self):


        print('begin parse command file')
        self.ui.logBrowser.append('Begin parse vcs ring info\n')
        self.ui.logBrowser.append('It may take about 30 seconds to finish parsing.\n')
        QCoreApplication.processEvents()
        self.ringinfo_path = self.ringinfo_path.strip()
        if self.ringinfo_path[-1] != '\\':
            self.ringinfo_path = self.ringinfo_path + '\\'
        self.command_xml = os.path.join(self.ringinfo_path, 'mapringinfo.xml')
        #main(self.ringinfo_path, self.command_xml, self.media_path)
        #init
        start = time.clock()
        obj = CmdFinder(self.media_path, 12, self.ringinfo_path)
        Buf = obj.h2xml()
        obj.extractfull()
        obj.writexml()
        elapsed = (time.clock() - start)
        print("Total Time used:",elapsed)
        #
        print('end parse command file')
        self.ui.logBrowser.append('End parse vcs ring info\n')



        # self.command_xml = 'mapVcsRingInfo.xml'

    def read_info_from_ui(self):
        self.media_path = self.ui.lineEditMediaPath.text()
        self.ringinfo_path = self.ui.lineEditRinginfoPath.text()
        self.test_name = self.ui.lineEditTestName.text()
        if self.ui.lineEditComponent.text():
            self.component = self.ui.lineEditComponent.text()
        else:
            self.component = self.ui.comboBoxComponent.currentText()
        if self.ui.lineEditPlatform.text():
            self.platform = self.ui.lineEditPlatform.text()
        else:
            self.platform = self.ui.comboBoxPlatform.currentText()
        if self.component in ('vp', 'VP'):
            self.output_path = self.ui.lineEditMediaPath.text().replace('/', '\\') + '\\media_embargo\\media_driver_next\\ult\\windows\\vp\\test\\test_data'
        else:
            self.output_path = self.ui.lineEditMediaPath.text().replace('/', '\\') + '\\media_embargo\\media_driver_next\\ult\\windows\\codec\\test\\test_data'
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)


    def read_command_info_from_xml(self):
        self.read_info_from_ui()
        self.parse_command_file()
        # if self.ui.lineEditFrame.text():
        #     self.frame_num = int(self.ui.lineEditFrame.text())
        # else:
        #     self.ui.logBrowser.append('Please input frame count\n')
        #     return
        tree = etree.parse(self.command_xml)
        root = tree.getroot()[0]
        frames = []
        for frame in root:
            print(frame.tag)
            commands = []
            # self.test_class_name = root.get('name')
            for command in frame:
                info = {'dwords': []}
                for command_tag in self.command_tags:
                    info[command_tag] = command.get(command_tag)
                if info['name'] in self.command_filter:
                    info['check'] = 'N'
                else:
                    info['check'] = 'Y'
                # f_other_cmd = False

                for dword in command:
                    # dword_t = {}
                    # dword_t['value'] = dword.get('value')
                    # dword_t['NO'] = dword.get('NO')
                    # if dword.get('otherCMD'):
                    #     f_other_cmd = True
                    #     other_cmd = {'name': dword.get('otherCMD'), 'class': command.get('class'), 'dwords': []}
                    #     dword_t['NO'] = '0'
                    #     for field in dword:
                    #         dword_t[field.tag] = {}
                    #         if field.tag.startswith('Obj'):
                    #             for obj_field in field:
                    #                 dword_t[field.tag][obj_field.tag] = {}
                    #                 for key, value in obj_field.items():
                    #                     dword_t[field.tag][obj_field.tag][key] = value
                    #         else:
                    #             for key, value in field.items():
                    #                 dword_t[field.tag][key] = value
                    #     other_cmd['dwords'].append(dword_t)
                    #     commands.append(other_cmd)
                    # if not dword_t['value']:
                    #     dword_t['unmappedstr'] = dword.get('unmappedstr')
                    dword_info = {'fields': []}
                    for dword_tag in self.dword_tags:
                        dword_info[dword_tag] = dword.get(dword_tag)

                    # if dword_info['otherCMD']:
                    #     f_other_cmd = True

                    for field in dword:
                        field_info = {'field_name': field.tag}
                        if field.tag.startswith('Obj'):
                            field_info = {'value': field.get('value'), 'obj_fields': [], 'field_name': field.tag}
                            for obj_field in field:
                                obj_field_info = {'obj_field_name': obj_field.tag}
                                for key, value in obj_field.items():
                                    obj_field_info[key] = value
                                field_info['obj_fields'].append(obj_field_info)
                        else:
                            for key, value in field.items():
                                field_info[key] = value
                            if 'default_value' in field_info:
                                field_info['value'] = field_info['default_value']
                        dword_info['fields'].append(field_info)
                    info['dwords'].append(dword_info)
                # if not f_other_cmd:
                commands.append(info)
            # for command_idx, command in enumerate(commands):
            #     command['index'] = command_idx
            frames.append(commands)
        self.command_info = frames
        print(len(frames))
        #
        self.ui.lineEditFrame.setText(str(len(frames)))
        #
        self.ui.logBrowser.append('Read infomation from ' + self.command_xml + '\n')
        self.form.info = self.command_info
        self.show_command_info()
        # self.update_cmd_list()


    def dw_length_check(self):
        s = ''
        for frame_idx, frame in enumerate(self.command_info):
            for command_idx, command in enumerate(frame):
                # DW0_dwlen = item_text_to_dec(command['input_dwsize'])
                input_dwsize = 0
                if 'input_dwsize' in command and command['input_dwsize']:
                    input_dwsize = item_text_to_dec(command['input_dwsize'])
                if 'def_dwsize' in command and command['def_dwSize']:
                    def_dwsize = item_text_to_dec(command['def_dwSize'])
                if command['dwords']:
                    last_dword_no = command['dwords'][-1]['NO']
                    if last_dword_no.find('_') != -1:
                        idx = last_dword_no.rfind('_')
                        last_dword_no = last_dword_no[idx + 1:]
                    last_dword_no = int(last_dword_no)
                    # print(last_dword_no)
                    # print(input_dwsize)
                    print(command['input_dwsize'])
                    if last_dword_no and input_dwsize and last_dword_no > input_dwsize:
                        s = 'frame ' + str(frame_idx) + ' command ' + str(command_idx) + ' ' + command['name'] + 'wrong dword length. \n'
                        s = s + 'Suggest ' + str(hex(last_dword_no)) + ' intstead\n\n'
        if s:
            self.show_message(s, 'Error')


    def show_message(self, inf, title):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        msgBox.setInformativeText(inf)
        msgBox.exec_()

    def split_dword(self):
        for frame_idx, frame in enumerate(self.command_info):
            for cmd_idx, cmd in enumerate(frame):
                for dword_idx, dword in enumerate(cmd['dwords']):
                    if dword['NO'].find('_') != -1:
                        print(dword_idx)
                        print(dword['NO'])
                        idx = dword['NO'].find('_')
                        l = dword['NO'][:idx]
                        r = dword['NO'][idx+1:]
                        cmd['dwords'][dword_idx]['NO'] = l
                        next_dword = copy.deepcopy(dword)
                        next_dword['NO'] = r
                        next_dword['value'] = '0x' + dword['value'][10:]
                        if next_dword['value'] == '0x':
                            next_dword['value'] = '0x0'
                        dword['value'] = dword['value'][:10]
                        split_field_idx = -1
                        for field_idx, field in enumerate(dword['fields']):
                            if int(field['bitfield_h'])> 31 and int(field['bitfield_l']) <= 31:
                                split_field_idx = field_idx
                                break
                        if split_field_idx >= 0:
                            dword['fields'][split_field_idx]['bitfield_h'] = '31'
                            dword['fields'] = dword['fields'][:split_field_idx + 1]
                            dword['fields'][split_field_idx]['have_following'] = 'Y'
                            next_dword['fields'][split_field_idx]['bitfield_l'] = '32'
                            next_dword['fields'] = next_dword['fields'][split_field_idx:]
                            next_dword['fields'][0]['have_precursor'] = 'Y'
                            for field in next_dword['fields']:
                                field['bitfield_l'] = str(int(field['bitfield_l']) - 32)
                                field['bitfield_h'] = str(int(field['bitfield_h']) - 32)
                            len1 = int(dword['fields'][split_field_idx]['bitfield_h']) - int(dword['fields'][split_field_idx]['bitfield_l'])
                            len1 = len1//4
                            if dword['fields'][split_field_idx]['default_value'] != 0:
                                dword['fields'][split_field_idx]['default_value'] = dword['fields'][split_field_idx]['default_value'][:2+len1]
                                dword['fields'][split_field_idx]['value'] = dword['fields'][split_field_idx]['default_value']
                                dword['fields'][split_field_idx]['min_value'] = dword['fields'][split_field_idx]['default_value']
                                dword['fields'][split_field_idx]['max_value'] = dword['fields'][split_field_idx]['default_value']
                                next_dword['fields'][0]['default_value'] = '0x' + next_dword['fields'][0]['default_value'][2+len1:]
                                next_dword['fields'][0]['value'] = next_dword['fields'][0]['default_value']
                                next_dword['fields'][0]['min_value'] = next_dword['fields'][0]['default_value']
                                next_dword['fields'][0]['max_value'] = next_dword['fields'][0]['default_value']
                        cmd['dwords'].insert(dword_idx+1, next_dword)


    @Slot()
    def generate_xml(self):
        if not self.command_info:
            pass
        self.test_name = self.ui.lineEditTestName.text()
        self.platform = self.ui.comboBoxPlatform.currentText()
        self.split_dword()
        lines = ['<?xml version="1.0"?>\n']
        lines.append('<' + self.test_name + '>\n')
        lines.append('  <Platform name="' + self.platform + '">\n')
        for frame_idx, frame in enumerate(self.command_info):
            # print('frame' + str(frame_idx))
            lines.append('    <Frame NO="' + str(frame_idx + 1) + '">\n')
            for cmd_idx, cmd in enumerate(frame):
                # print('cmd' + str(cmd_idx))
                s_cmd = '      <CMD'
                for key, value in cmd.items():
                    if key != 'dwords' and value:
                        s_cmd = s_cmd + ' ' + key + '="' + str(value) + '"'
                s_cmd  = s_cmd + '>\n'
                lines.append(s_cmd)
                # lines.append('      <CMD index="' + str(cmd_idx) + '" name="' + cmd['name'] + '" class="' + cmd['class'] + '">\n ')
                for dword_idx, dword in enumerate(cmd['dwords']):
                    s_dword = '        <dword'
                    for key, value in dword.items():
                        if key != 'fields' and value:
                            s_dword = s_dword + ' ' + key + '="' + str(value) + '"'
                    s_dword = s_dword + '>\n'
                    lines.append(s_dword)
                    # if 'unmappedstr' in dword:
                    #     continue
                    # if dword['value']:
                    #     lines.append('        <dword index="' + dword['NO'] + '" value="' + dword['value'] + '">\n')
                    # elif dword['unmappedstr']:
                    #     lines.append('        <dword index="' + dword['NO'] + '" unmappedstr="' + dword['unmappedstr'] + '">\n')
                    for field in dword['fields']:
#                        if 'CHECK' in field and field['CHECK'] == 'Y':
                         if not field['field_name'].startswith('Reserve'):
                            s_field = '          <' + field['field_name']
                            for key, value in field.items():
                                if key == 'have_precursor':
                                     print('have_precursor')
                                if key != 'field_name':
                                    s_field = s_field + ' ' + key + '="' + str(value) + '"'
                            s_field = s_field + '/>\n'
                            lines.append(s_field)
                    lines.append('        </dword>\n')
                lines.append('      </CMD>\n')
            lines.append('    </Frame>\n')
        lines.append('  </Platform>\n')
        lines.append('</' + self.test_name + '>\n')
        file_name = self.test_name + '.xml'
        with open(self.output_path + '\\' + file_name, 'w') as fout:
            fout.writelines(lines)
        self.ui.logBrowser.append('Generating modified command xml' + self.output_path + '\\' + file_name + '\n')
        self.show_message('Generating modified command xml' + self.output_path + '\\' + file_name + '\n', '')

    #
    @Slot()
    def selectpath(self, name):
        #open file dialog and display directory in the text edit area
        dir = QFileDialog.getExistingDirectory(self, "Open Directory",
                                       "/home",
                                       QFileDialog.ShowDirsOnly
                                       | QFileDialog.DontResolveSymlinks)
        if name == 'Media':
            self.ui.lineEditMediaPath.setText(dir)
        if name == 'DDIInput':
            self.ui.lineEditDDIInputPath.setText(dir)
            self.ddiinputpath = self.ui.lineEditDDIInputPath.text()
        if name == 'Ringinfo':
            self.ui.lineEditRinginfoPath.setText(dir)

    @Slot()
    def GAll(self):
        #self.read_command_info_from_xml()
        QCoreApplication.processEvents()
        self.typeinputpara.show()
        # how to wait to execute next evernt after closing 1 event ?
        #app.exec_()
        


class FormCommandInfo(QWidget):
    def __init__(self, main_window):
        super(FormCommandInfo, self).__init__()
        self.ui = Ui_FormCommandInfo()
        self.ui.setupUi(self)
        self.info = []
        self.main_window = main_window
        self.ui.pushButtonSave.clicked.connect(self.save)
        self.ui.pushButtonGen.clicked.connect(self.main_window.generate_xml)
        self.current_frame = 0
        self.current_command = ''
        self.mode = 'hex'
        self.first = True
        self.row_command_map = []
        self.ui.checkBoxHex.stateChanged.connect(self.update_data_mode_hex)
        self.ui.checkBoxDec.stateChanged.connect(self.update_data_mode_dec)
        self.ui.checkBoxBinary.stateChanged.connect(self.update_data_mode_bin)
        self.current_item = None
        #
        self.ui.stackedWidget.setCurrentIndex(0)   #set the all infomation page as default page
        self.ui.pushButtonSCL.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))  #show cmd name list
        self.ui.pushButtonGB.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(0))  #show cmd name list
        

    def show_message(self, inf, title):
        msgBox = QMessageBox()
        msgBox.setWindowTitle(title)
        if title == 'Save':
            msgBox.addButton(QMessageBox.Ok)
            msgBox.addButton(QMessageBox.No)
        msgBox.setInformativeText(inf)
        msgBox.exec_()

    def check(self):
        s = ''
        table = self.ui.tableWidgetCmd
        for i in range(table.rowCount()):
            if not table.item(i, 2):
                continue
            if table.cellWidget(i, 5).isChecked():
                command = self.info[int(self.row_command_map[i]['frame_idx'])][int(self.row_command_map[i]['command_idx'])]
                dword = 'dword' + command['dwords'][int(self.row_command_map[i]['dword_idx'])]['NO']
                field = str(table.item(i, 2).text())
                value = str(table.item(i, 4).text())

                min_value = str(table.item(i, 7).text())
                max_value = str(table.item(i, 8).text())
                # value = item_text_to_dec(value)
                # min_value = item_text_to_dec(min_value)
                # max_value = item_text_to_dec(max_value)
                if max_value < min_value:
                    s = s + 'Command ' + command['name'] + ' ' + dword + ' max value smaller than min value\n\n'
                    # s = s + 'Row' + str(i) + ' max value smaller than min value\n\n'
                if value < min_value:
                    s = s + 'Command ' + command['name'] + ' ' + dword + ' value smaller than min value\n\n'
                if value > max_value:
                    s = s + 'Command ' + command['name'] + ' ' + dword + ' value larger than max value\n\n'

        if s:
            self.show_message(s, 'Error')
            return -1
        else:
            return 0


    @Slot()
    def save(self):
        table = self.ui.tableWidgetCmd
        tree = self.ui.treeWidgetCmd
        if not self.first:
            self.show_message('Save information', 'Save')
        else:
            self.first = False
            # for i in range(table.rowCount()):
            #     cmd_name = str(table.item(i, 0))
            #     if cmd_name not in cmds:
            #         cmds.add(cmd_name)
            #         info.append({'name': cmd_name, 'fields': {}})
            #     if table.cellWidget(i, 3).checkState():
            #         field_name = str(table.item(i, 1))
            #         info[-1]['fields'][field_name] = {}
            #         info[-1]['fields']['defalt_value'] = str(table.item(i, 2))
            #         info[-1]['fields']['Address'] = str(table.item(i, 4))
            #         info[-1]['fields']['min_value'] = str(table.item(i, 5))
            #         info[-1]['fields']['max_value'] = str(table.item(i, 6))
        if self.check() != 0:
            return
        for i in range(table.rowCount()):
            dword = self.info[int(self.row_command_map[i]['frame_idx'])][int(self.row_command_map[i]['command_idx'])]['dwords'][int(self.row_command_map[i]['dword_idx'])]
            if dword:
                if not table.item(i, 2):
                    continue
                field_name = str(table.item(i, 2).text())
                for field in dword['fields']:
                    if field['field_name'] == field_name:
                        field['value'] = str(table.item(i, 4).text())
                        if table.cellWidget(i, 5).isChecked():
                            field['CHECK'] = 'Y'
                        else:
                            field['CHECK'] = 'N'
                        if self.mode == 'bin':
                            field['value'] = hex(int(str(table.item(i, 4).text()), 2))
                            field['min_value'] = hex(int(str(table.item(i, 7).text()), 2))
                            field['max_value'] = hex(int(str(table.item(i, 8).text()), 2))
                        elif self.mode == 'dec':
                            field['value'] = hex(int(str(table.item(i, 4).text())))
                            field['min_value'] = hex(int(str(table.item(i, 7).text())))
                            field['max_value'] = hex(int(str(table.item(i, 8).text())))
                        else:
                            field['value'] = str(table.item(i, 4).text())
                            field['min_value'] = str(table.item(i, 7).text())
                            field['max_value'] = str(table.item(i, 8).text())

    @Slot(QTreeWidgetItem, int)
    def update_tree_checkstate(self, item, column):
        for i in range(item.childCount()):
            dword = item.child(i)
            if item.checkState(0) == Qt.CheckState.Checked:
                dword.setCheckState(0, Qt.CheckState.Checked)
            else:
                dword.setCheckState(0, Qt.CheckState.Unchecked)


    @Slot()
    def update_data_mode_hex(self):
        if self.ui.checkBoxHex.isChecked():
            self.mode = 'hex'
            self.ui.checkBoxDec.setCheckState(Qt.CheckState.Unchecked)
            self.ui.checkBoxBinary.setCheckState(Qt.CheckState.Unchecked)
            if self.current_item:
              self.main_window.show_command_table(self.current_item)

    @Slot()
    def update_data_mode_dec(self):
        if self.ui.checkBoxDec.isChecked():
            self.mode = 'dec'
            self.ui.checkBoxHex.setCheckState(Qt.CheckState.Unchecked)
            self.ui.checkBoxBinary.setCheckState(Qt.CheckState.Unchecked)
            if self.current_item:
              self.main_window.show_command_table(self.current_item)

    @Slot()
    def update_data_mode_bin(self):
        if self.ui.checkBoxBinary.isChecked():
            self.mode = 'bin'
            self.ui.checkBoxDec.setCheckState(Qt.CheckState.Unchecked)
            self.ui.checkBoxHex.setCheckState(Qt.CheckState.Unchecked)
            if self.current_item:
              self.main_window.show_command_table(self.current_item)

class InputWindow(QMainWindow):
    def __init__(self, main_window):
        super(InputWindow, self).__init__()
        self.ui = Ui_InputWindow()
        self.ui.setupUi(self)
        self.main_window = main_window
        self.ui.buttonBox.accepted.connect(self.addHeader)
        self.ui.buttonBox.rejected.connect(self.reject)
        #self.ui.SelectPath.clicked.connect(self.selectpath)
        self.ui.InputPathText.setText(self.main_window.ui.lineEditDDIInputPath.text())
        self.ui.Component_input.setText(self.main_window.ui.lineEditComponent.text())
        self.ui.GUID_input.setText('DXVA2_Intel_LowpowerEncode_HEVC_Main')
        self.ui.Width_input.setText('256')
        self.ui.Height_input.setText('192')
        self.ui.RawTileType_input.setText('1')
        self.ui.RawFormat_input.setText('25')
        self.ui.ResTileType_input.setText('4')
        self.ui.ResFormat_input.setText('62')
        self.ui.EncFunc_input.setText('4')
        self.ui.FrameNum_input.setReadOnly(True)
        #self.ui.FrameNum_input.setText('1')
        self.FrameNumdiff = 0


    @Slot()
    def addHeader(self):
        # click OK, generate xml header
        self.Component = self.ui.Component_input.text()
        self.GUID = self.ui.GUID_input.text()
        self.Width = self.ui.Width_input.text()
        self.Height = self.ui.Height_input.text()
        self.inputpath = self.ui.InputPathText.text()
        self.RawTileType = self.ui.RawTileType_input.text()
        self.RawFormat = self.ui.RawFormat_input.text()
        self.ResTileType = self.ui.ResTileType_input.text()
        self.ResFormat = self.ui.ResFormat_input.text()
        self.EncFunc = self.ui.EncFunc_input.text()
        self.FrameNum = self.ui.FrameNum_input.text()
        # get real Frame Number according to input files
        os.chdir(self.inputpath)
        Frameset = set()
        for f in os.listdir(self.inputpath):
            pattern = re.search('^(\d)-0.*DDIEnc_(.*)Params_._Frame', f)
            if pattern:
                Frameset.add(int(pattern.group(1)))
        self.FrameNumdiff = min(Frameset) - 0
        self.FrameNum = str(len(Frameset))
        self.ui.FrameNum_input.setText(self.FrameNum)
        # combine input files and parameters
        self.combine()
        self.main_window.ui.logBrowser.append("The input file has been generated.\n")
        #pop out message box
        msgBox = QMessageBox()
        msgBox.setText("The input file has been generated.")
        msgBox.exec_()
        
        self.main_window.read_command_info_from_xml()
    
    @Slot()
    def reject(self):
        # click cancel, exit
        sys.exit(app.exec_())
        

    def combine(self):
        #combine ddi_input text files and add header infomation
        
        with open('encodeHevcCQPInput.dat','w') as wfd:
            #wfd.write('<Header Component=%s  GUID=%s Width=%s Height=%s OutputFormat=%s>\n' % (self.Component, self.GUID, self.Width, self.Height, self.OutputFormat))
            wfd.write(f'''<Header>
Component = {self.Component}
GUID = DXVA2_Intel_LowpowerEncode_HEVC_Main
Width = {self.Width}
Height = {self.Height}
#MOS_TILE_Y
RawTileType = {self.RawTileType}
#Format_NV12
RawFormat = {self.RawFormat}
#MOS_TILE_LINEAR
ResTileType = {self.ResTileType}
#Format_Buffer
ResFormat = {self.ResFormat}
#ENCODE_ENC_PAK, 4
EncFunc = {self.EncFunc}
FrameNum = {self.FrameNum}
''')
            #wfd.write('</Header>')
             
            for f in os.listdir(self.inputpath):
                pattern = re.search('^(\d)-0.*DDIEnc_(.*)Params_._Frame', f)
                if pattern:
                    FrameNo = str(int(pattern.group(1))-self.FrameNumdiff)
                    ParaGroup = pattern.group(2)
                    wfd.write('<Frame No=%s  Param=%s >\n' % (FrameNo, ParaGroup))
                    with open(f, 'r') as file:
                        content = file.readlines()
                        new_content = []
                        for line in content:
                            clean_line = line.replace('\00', '')
                            new_content.append(clean_line)
                    wfd.writelines(new_content)
                    #wfd.write('</Frame>\n')
        

def item_text_to_dec(s):
    if s.startswith('0x'):
        return int(s, 16)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

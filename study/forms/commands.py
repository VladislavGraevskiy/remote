# coding: utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

from django import forms
from study.constants import (
    CMD_MINIMAL, CMD_NOMINAL, CMD_OPERATING, CMD_ENABLE_BROADCASTING, CMD_DISABLE_BROADCASTING,
    CMD_SET_REAL_TIME, CMD_ENABLE_DEVICE, CMD_DISABLE_DEVICE, CMD_TRANSCEIVER_SELECT, CMD_DEVICE_COMMAND,
    CMD_RESERVE_MAIN_POWER_OFF, CMD_RESERVE_MAIN_POWER_ON, CMD_SOFT_SHUTDOWN
)
CMD = (
    (CMD_MINIMAL, 'Перейти в режим работы с минимальным энергопотреблением'),
    (CMD_NOMINAL, 'Перейти в штатный режим работы'),
    (CMD_OPERATING, 'Перейти в режим работы с научной аппаратурой')
)


class Modes(forms.Form):
    inform = forms.CharField(widget=forms.TextInput(attrs={'class': 'special', 'size': '40', 'wight': '6'}), max_length=1000)
    modes_command = forms.ChoiceField(choices=CMD, label='Комманда')
    # datetime = forms.DateTimeField(widget=forms.DateTimeInput, input_formats='%Y-%m-%d %H:%M:%S')


   # MainWindow.setWindowTitle(_translate("MainWindow", "Satellite simulator control program", None))
   #      self.execution_date_time_checkBox.setText(_translate("MainWindow", "Выполнить команду сразу при получении", None))
   #      self.execution_date_time_label.setText(_translate("MainWindow", "Установить время и дату выполнения посылаемой команды или выполнить команду сразу при получении:", None))
   #      self.undecoded_data_from_packages_label.setText(_translate("MainWindow", "Панель отображения содержимого ответных пакетов:", None))
   #      self.panel_for_manual_sending_of_commands_label.setText(_translate("MainWindow", "Панель посыла команд в ручном режиме:", None))
   #      self.enable_operating_mode_label.setText(_translate("MainWindow", "Перейти в режим работы с научной аппаратурой ", None))
   #      self.enable_nominal_mode_pushButton.setText(_translate("MainWindow", "Отправить", None))
   #      self.enable_operating_mode_pushButton.setText(_translate("MainWindow", "Отправить", None))
   #      self.enable_nominal_mode_label.setText(_translate("MainWindow", "Перейти в штатный режим работы", None))
   #      self.enable_minimal_mode_label.setText(_translate("MainWindow", "Перейти в режим работы с минимальным энергопотреблением ", None))
   #      self.enable_minimal_mode_pushButton.setText(_translate("MainWindow", "Отправить", None))
   #      self.enable_equipment_mode_label.setText(_translate("MainWindow", "Перейти в режим работы с отрабатываемым оборудованием", None))
   #      self.enable_equipment_mode_pushButton.setText(_translate("MainWindow", "Отправить", None))
   #      self.modes_of_operation_tabWidget.setTabText(self.modes_of_operation_tabWidget.indexOf(self.modes_of_operation_tab), _translate("MainWindow", "Режимы работы", None))
   #      self.device_power_disable_pushButton.setText(_translate("MainWindow", " Выключить", None))
   #      self.label.setText(_translate("MainWindow", " Идентификатор оборудования:", None))
   #      self.device_power_enable_pushButton.setText(_translate("MainWindow", " Включить", None))
   #      self.label_2.setText(_translate("MainWindow", "Управление питанием:", None))
   #      self.label_3.setText(_translate("MainWindow", "Отправка команд:", None))
   #      self.label_5.setText(_translate("MainWindow", "Имя команды:", None))
   #      self.device_id_comboBox.setItemText(0, _translate("MainWindow", "power", None))
   #      self.device_id_comboBox.setItemText(1, _translate("MainWindow", "gpsa", None))
   #      self.device_id_comboBox.setItemText(2, _translate("MainWindow", "gpsb", None))
   #      self.device_id_comboBox.setItemText(3, _translate("MainWindow", "os", None))
   #      self.device_id_comboBox.setItemText(4, _translate("MainWindow", "cpu_temp", None))
   #      self.device_id_comboBox.setItemText(5, _translate("MainWindow", "light", None))
   #      self.device_id_comboBox.setItemText(6, _translate("MainWindow", "hmc5883l", None))
   #      self.device_id_comboBox.setItemText(7, _translate("MainWindow", "mpu6050", None))
   #      self.device_id_comboBox.setItemText(8, _translate("MainWindow", "ms5611", None))
   #      self.device_id_comboBox.setItemText(9, _translate("MainWindow", "ds1621", None))
   #      self.device_id_comboBox.setItemText(10, _translate("MainWindow", "ds1621-2", None))
   #      self.device_id_comboBox.setItemText(11, _translate("MainWindow", "ds1621-3", None))
   #      self.label_6.setText(_translate("MainWindow", "Аргумент команды:", None))
   #      self.device_command_pushButton.setText(_translate("MainWindow", "Выполнить", None))
   #      self.modes_of_operation_tabWidget.setTabText(self.modes_of_operation_tabWidget.indexOf(self.toggle_power_tab), _translate("MainWindow", "Исполнительные устройства", None))
   #      self.label_4.setText(_translate("MainWindow", "Выбор основного передатчика:", None))
   #      self.enable_broadcasting_pushButton.setText(_translate("MainWindow", "Включить", None))
   #      self.disable_broadcasting_pushButton.setText(_translate("MainWindow", "Выключить", None))
   #      self.toggle_transmission_label.setText(_translate("MainWindow", "Вещание в эфир", None))
   #      self.transceiver_select_comboBox.setItemText(0, _translate("MainWindow", "TNCA", None))
   #      self.transceiver_select_comboBox.setItemText(1, _translate("MainWindow", "TNCB", None))
   #      self.transceiver_select_pushButton.setText(_translate("MainWindow", "Назначить основным", None))
   #      self.modes_of_operation_tabWidget.setTabText(self.modes_of_operation_tabWidget.indexOf(self.other_commands_tab), _translate("MainWindow", "Радиомодуль", None))
   #      self.set_real_time_pushButton.setText(_translate("MainWindow", "Отправить", None))
   #      self.other_commands_real_time_clock_settings_label.setText(_translate("MainWindow", " Установка даты и времени на имитаторе СМКА:", None))
   #      self.modes_of_operation_tabWidget.setTabText(self.modes_of_operation_tabWidget.indexOf(self.tab), _translate("MainWindow", "Другие команды", None))
   #      self.hard_power_off_pushButton.setText(_translate("MainWindow", "Отправить", None))
   #      self.hard_power_off_label.setText(_translate("MainWindow", "Выключить питание ПК", None))
   #      self.soft_power_off_label.setText(_translate("MainWindow", "Выключить ПК", None))
   #      self.soft_power_off_pushButton.setText(_translate("MainWindow", "Отправить", None))
   #      self.hard_power_on_label.setText(_translate("MainWindow", "Включить питание ПК", None))
   #      self.hard_power_on_pushButton.setText(_translate("MainWindow", "Отправить", None))
   #      self.modes_of_operation_tabWidget.setTabText(self.modes_of_operation_tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Управление бортовым ПК", None))
   #      self.actionOpen.setText(_translate("MainWindow", "Open", None))
   #      self.actionSave.setText(_translate("MainWindow", "Save", None))
   #      self.actionClose.setText(_translate("MainWindow", "Close", None))

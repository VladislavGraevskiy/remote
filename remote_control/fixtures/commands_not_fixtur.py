# coding: utf-8
from __future__ import absolute_import, unicode_literals, division, print_function

js = {
  "version": "0.2",
  "name": "Программа управления имитатором МКА",
  "categories": [
    {
      "name": "Управление бортовым ПК",
      "commands": [
        {
          "name": "Включить питание ПК",
          "arguments": [
            {
              "name": "reserve_system",
              "type": "literal",
              "value": true
            }
          ],
          "command": "CMD_RESERVE_MAIN_POWER_ON"
        },
        {
          "name": "Выключить ПК",
          "arguments": [],
          "command": "CMD_SOFT_SHUTDOWN"
        },
        {
          "name": "Выключить питание ПК",
          "arguments": [
            {
              "name": "reserve_system",
              "type": "literal",
              "value": true
            }
          ],
          "command": "CMD_RESERVE_MAIN_POWER_OFF"
        }
      ]
    },
    {
      "name": "Режимы работы",
      "commands": [
        {
          "name": "Режим работы с минимальным энергопотреблением",
          "arguments": [],
          "command": "CMD_MINIMAL"
        },
        {
          "name": "Штатный режим работы",
          "arguments": [],
          "command": "CMD_NOMINAL"
        },
        {
          "name": "Режим работы с отрабатываемым оборудованием",
          "arguments": [],
          "command": "CMD_NOMINAL"
        },
        {
          "name": "Режим работы с научной аппаратурой",
          "arguments": [],
          "command": "CMD_OPERATING"
        }
      ]
    },
    {
      "name": "Исполнительные устройства",
      "commands": [
        {
          "name": "Отправить команду",
          "arguments": [
            {
              "id": "device_list",
              "name": "device",
              "type": "list",
              "list": [
                "power",
                "gpsa",
                "gpsb",
                "os",
                "cpu_temp",
                "light",
                "hmc5883l",
                "mpu6050",
                "ms5611",
                "ds1621",
                "ds1621-1",
                "ds1621-2"
              ]
            },
            {
              "name": "arg",
              "type": "string_input"
            }
          ],
          "command": "CMD_DEVICE_COMMAND"
        },
        {
          "name": "Включить устройство",
          "arguments": [
            {
              "name": "device",
              "type": "reference",
              "reference": "device_list"
            }
          ],
          "command": "CMD_ENABLE_DEVICE"
        },
        {
          "name": "Выключить устройство",
          "arguments": [
            {
              "name": "device",
              "type": "reference",
              "reference": "device_list"
            }
          ],
          "command": "CMD_DISABLE_COMMAND"
        }
      ]
    },
    {
      "name": "Радиомодуль",
      "commands": [
        {
          "name": "Включить вещание в эфир",
          "arguments": [],
          "command": "CMD_ENABLE_TRANSMISSION"
        },
        {
          "name": "Выключить вещание в эфир",
          "arguments": [],
          "command": "CMD_DISABLE_TRANSMISSION"
        },
        {
          "name": "Назначить основным",
          "arguments": [
            {
              "name": "arg",
              "type": "list",
              "list": [
                "TNCA",
                "TNCB",
                "TNCC",
                "TNCD"
              ]
            }
          ],
          "command": "CMD_TRANSCEIVER_SELECT"
        }
      ]
    },
    {
      "name": "Другие команды",
      "commands": [
        {
          "name": "Установить дату и время",
          "arguments": [
            {
              "name": "arg",
              "type": "time",
              "default": 1451606400
            }
          ],
          "command": "CMD_SET_REAL_TIME"
        }
      ]
    }
  ]
}

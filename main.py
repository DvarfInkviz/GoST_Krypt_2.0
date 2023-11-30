#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################
#                                       #
# Lyashko A.A. 21 Nov 2023              #
# Script GoST Compilation.py v.1.0      #
#                                       #
#########################################################################
import glob
import os
import sys
from datetime import datetime

# max_qpf: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_NEW.dpf
# max_dir: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\
# max_qsf: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_NEW.qsf
# max_pof: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_NEW.pof
# max_const: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\
# max_ML: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\C_ML_TEST.tdf
# max_ST: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\C_ST_TEST.tdf
# max_XL0: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X0L.v
# max_XS0: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X0S.v
# max_XL1: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X1L.v
# max_XS1: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X1S.v
# max_XL2: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X2L.v
# max_XS2: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X2S.v
# max_XL3: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X3L.v
# max_XS3: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X3S.v
# max_XL4: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X4L.v
# max_XS4: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X4S.v
# max_XL5: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X5L.v
# max_XS5: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X5S.v
# max_XL6: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X6L.v
# max_XS6: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X6S.v
# max_XL7: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X7L.v
# max_XS7: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X7S.v
# cyc_qpf: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW.qpf
# cyc_dir: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\
# cyc_qsf: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW.qsf
# cyc_pof: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW.pof
# cyc_const: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\
# cyc_mif: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\ROM_FLASH_CYCLON.mif
# cyc_c24: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\CON_24bit.tdf
# cyc_XL0: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X0L.v
# cyc_XS0: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X0S.v
# cyc_XL1: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X1L.v
# cyc_XS1: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X1S.v
# cyc_XL2: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X2L.v
# cyc_XS2: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X2S.v
# cyc_XL3: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X3L.v
# cyc_XS3: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X3S.v
# cyc_XL4: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X4L.v
# cyc_XS4: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X4S.v
# cyc_XL5: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X5L.v
# cyc_XS5: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X5S.v
# cyc_XL6: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X6L.v
# cyc_XS6: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X6S.v
# cyc_XL7: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X7L.v
# cyc_XS7: R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\X7S.v
# qua_map: C:\Altera\10.1\quartus\bin\quartus_map.exe
# qua_dir: C:\Altera\10.1\quartus\bin\
# fil_fol: R:\Niir\GostCrypt\


class Max:

    def __init__(self, start_folder):
        for root, dirs, files in os.walk(start_folder):
            for file in files:
                if file.endswith('.qpf'):
                    self.max_qpf = os.path.join(root, file)
                if file.endswith('.qsf'):
                    self.max_qsf = os.path.join(root, file)
                if file.endswith('.pof'):
                    self.max_pof = os.path.join(root, file)
        self.const = os.path.join(start_folder, 'GOST_MAX_LIB')
        for root, dirs, files in os.walk(self.const):
            for file in files:
                if file == 'C_ML_TEST.tdf':
                    self.max_ML = os.path.join(root, file)
                if file == 'C_ST_TEST.tdf':
                    self.max_ST = os.path.join(root, file)
        # max_const: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\
        # max_ML: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\C_ML_TEST.tdf
        # max_ST: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\C_ST_TEST.tdf
        # max_XL0: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X0L.v
        # max_XS0: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X0S.v
        # max_XL1: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X1L.v
        # max_XS1: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X1S.v
        # max_XL2: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X2L.v
        # max_XS2: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X2S.v
        # max_XL3: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X3L.v
        # max_XS3: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X3S.v
        # max_XL4: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X4L.v
        # max_XS4: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X4S.v
        # max_XL5: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X5L.v
        # max_XS5: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X5S.v
        # max_XL6: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X6L.v
        # max_XS6: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X6S.v
        # max_XL7: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X7L.v
        # max_XS7: R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2\GOST_MAX_LIB\X7S.v

    def run(self):
        pass
# // формирование имени конечного файла //
# // выбор ключей
# // замена ключей для MAX
# // ввод 32-разрядных констант
# // ввод ключей для MAX

# // замена ключей для CYCLON
# // замена номера модуля в константе CON_24bit.tdf
# замена номера модуля в R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3\GOST_NEW_LIB\ud92g.mif
# Замена адресов с 073 по 076. В адресе 073 ввести 00. В адресах 074, 75, 076 ввести соответствующие три байта модуля.
# // ввод ключей для CYCLON в tdf
# // ввод ключей для CYCLON в ROM_FLASH_CYCLON.mif

# COMPILATION


max_compilation = Max(start_folder=os.path.normpath(r"R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2"))
max_compilation.run()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################
#                                       #
# Lyashko A.A. 21 Nov 2023              #
# Script GoST Compilation.py v.1.0      #
#                                       #
#########################################################################
import os
import subprocess
from datetime import datetime
import secrets
import shutil
from tqdm import tqdm


def const_edit(name, new_value):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), 'r') as _f:
        _data = _f.read()
    return _data.replace('6666', new_value)


def mif1_edit(name, new_keys):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), 'r') as _f:
        _data = _f.read()
    for i in range(0, 8):
        _data = _data.replace(f'66{i}', new_keys[i])
    return _data


def mif2_edit(name, new_value):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), 'r') as _f:
        _data = _f.read()
    _data = _data.replace('6660', new_value[:2])
    _data = _data.replace('6661', new_value[2:4])
    _data = _data.replace('6662', new_value[4:])
    return _data


def qua_cmd(qua_type, qpf, qsf, set_files=None):
    _exe = os.path.join(r'c:\altera\13.0sp1\quartus\bin', f'quartus_{qua_type}.exe')
    try:
        if set_files is None:
            process = subprocess.run([_exe, qpf, '-c', qsf], check=True, capture_output=True)
        else:
            process = subprocess.run([_exe, f'--read_settings_files={set_files}', '--write_settings_files=off', qpf,
                                      '-c', qsf], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        tqdm.write(f"Ошибка команды {e.cmd}!")
    else:
        if 'was successful. 0 errors' in str(process.stdout):
            return True
        else:
            return False


class Fpga:

    def __init__(self, start_folder, _keys, _module, _type, _lib):
        self.keys = _keys
        self.key32 = secrets.token_hex(8)
        self.cam = _module
        self.fpga = _type
        self.lib_dir = _lib
        self.cam_file = os.path.normpath(fr"R:\Niir\GostCrypt\Modules\{self.cam}_{self.fpga}.pof")
        self.cam_file2 = os.path.normpath(fr"R:\Niir\GostCrypt\Modules\{self.cam}_cyc.pof")
        self.error_ini = False
        for root, dirs, files in os.walk(start_folder):
            for file in files:
                if file.endswith('.qpf'):
                    self.qpf = os.path.join(root, file)
                if file.endswith('.qsf'):
                    self.qsf = os.path.join(root, file)
                if file.endswith('.pof'):
                    self.pof = os.path.join(root, file)
                    self.pof_date = os.path.getctime(self.pof)
        self.const = os.path.join(start_folder, self.lib_dir)
        if self.fpga == 'max':
            if os.path.isfile(os.path.join(self.const, 'C_ML_TEST.tdf')):
                self.ML = os.path.join(self.const, 'C_ML_TEST.tdf')
            else:
                self.error_ini = True
            if os.path.isfile(os.path.join(self.const, 'C_ST_TEST.tdf')):
                self.ST = os.path.join(self.const, 'C_ST_TEST.tdf')
            else:
                self.error_ini = True
        else:
            if os.path.isfile(os.path.join(self.const, 'ROM_FLASH_CYCLON.mif')):
                self.rom_flash = os.path.join(self.const, 'ROM_FLASH_CYCLON.mif')
            else:
                self.error_ini = True
            if os.path.isfile(os.path.join(self.const, 'ud92g.mif')):
                self.ud92g = os.path.join(self.const, 'ud92g.mif')
            else:
                self.error_ini = True
            if os.path.isfile(os.path.join(self.const, 'CON_24bit.tdf')):
                self.con_24bit = os.path.join(self.const, 'CON_24bit.tdf')
            else:
                self.error_ini = True
        self.x_ls = []
        for i in range(0, 8):
            self.x_ls.append({'L': ''})
            if os.path.isfile(os.path.join(self.const, f'X{i}L.v')):
                self.x_ls[i]['L'] = os.path.join(self.const, f'X{i}L.v')
            else:
                self.error_ini = True
            self.x_ls[i]['S'] = ''
            if os.path.isfile(os.path.join(self.const, f'X{i}S.v')):
                self.x_ls[i]['S'] = os.path.join(self.const, f'X{i}S.v')
            else:
                self.error_ini = True

    def run(self):
        if not self.error_ini:
            self.edit_files()
            if self.compile():
                tqdm.write(f'{self.fpga} compilation OK')
                # if os.path.getctime(self.pof) > self.pof_date:
                shutil.copyfile(self.pof, self.cam_file)
                return True
                # else:
                #     return False
            else:
                tqdm.write(f'{self.fpga} compilation ERROR - need recompile!')
                return False
        else:
            tqdm.write(f'{self.fpga} project - ini ERROR!')
            return 2

    def edit_files(self):
        tqdm.write(f'Замена констант для {self.fpga}')
        if self.fpga == 'max':
            with open(self.ML, 'w') as _f:
                _f.write(const_edit(name=fr"{self.lib_dir}\{os.path.basename(self.ML)}",
                                    new_value=str(int(self.key32[:8], 16))))
            with open(self.ST, 'w') as _f:
                _f.write(const_edit(name=fr"{self.lib_dir}\{os.path.basename(self.ST)}",
                                    new_value=str(int(self.key32[8:], 16))))
        else:
            with open(self.con_24bit, 'w') as _f:
                _f.write(const_edit(name=fr"{self.lib_dir}\{os.path.basename(self.con_24bit)}",
                                    new_value=str(self.cam)))
            with open(self.rom_flash, 'w') as _f:
                _f.write(mif1_edit(name=fr"{self.lib_dir}\{os.path.basename(self.rom_flash)}", new_keys=self.keys))
            with open(self.ud92g, 'w') as _f:
                _f.write(mif2_edit(name=fr"{self.lib_dir}\{os.path.basename(self.ud92g)}", new_value=f'{self.cam:06X}'))
        for i in range(0, 8):
            with open(self.x_ls[i]['L'], 'w') as _f:
                _f.write(const_edit(name=fr"{self.lib_dir}\{os.path.basename(self.x_ls[i]['L'])}",
                                    new_value=str(int(self.keys[i][4:], 16))))
            with open(self.x_ls[i]['S'], 'w') as _f:
                _f.write(const_edit(name=fr"{self.lib_dir}\{os.path.basename(self.x_ls[i]['S'])}",
                                    new_value=str(int(self.keys[i][:4], 16))))

    def compile(self):
        tqdm.write('Начинается компиляция проекта')
        compile_result = qua_cmd('map', self.qpf, self.qsf, set_files='on')
        if compile_result:
            compile_result = qua_cmd('fit', self.qpf, self.qsf, set_files='off')
        else:
            return False
        if compile_result:
            if self.fpga == 'max':
                compile_result = qua_cmd('asm', self.qpf, self.qsf, set_files='on')
            else:
                compile_result = qua_cmd('asm', self.qpf, self.qsf, set_files='off')
        else:
            return False
        if compile_result:
            compile_result = qua_cmd('sta', self.qpf, self.qsf)
        else:
            return False
        if compile_result:
            return True
        else:
            return False


error_compilation = False
for number in tqdm(range(14330, 14355), ncols=80, ascii=True):
    if error_compilation == 2:
        tqdm.write('ERROR in projects - STOP!')
        break
    tqdm.write(f'-=CAM #{number}=-')
    cam_file = os.path.normpath(fr"R:\Niir\GostCrypt\Modules\{number}_max.pof")
    cam_file2 = os.path.normpath(fr"R:\Niir\GostCrypt\Modules\{number}_cyc.pof")
    if os.path.isfile(cam_file) and os.path.isfile(cam_file2):
        error_compilation = True
    else:
        if os.path.isfile(cam_file):
            os.remove(cam_file)
        if os.path.isfile(cam_file2):
            os.remove(cam_file2)
    while not error_compilation:
        keys = [secrets.token_hex(4) for i in range(0, 8)]
        max_project = Fpga(start_folder=os.path.normpath(r"R:\Niir\GostCrypt\Qua_projects\MAX_28042018_restored_2"),
                           _keys=keys, _module=number, _type='max', _lib='GOST_MAX_LIB')
        error_compilation = max_project.run()
        if error_compilation:
            cyc = Fpga(start_folder=os.path.normpath(r"R:\Niir\GostCrypt\Qua_projects\CYCL_28042018_restored3"),
                       _keys=keys, _module=number, _type='cyc', _lib='GOST_NEW_LIB')
            error_compilation = cyc.run()
    tqdm.write('==================')

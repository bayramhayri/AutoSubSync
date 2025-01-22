# -*- mode: python ; coding: utf-8 -*-

import os
import sys
import platform

# Add current directory to Python path
sys.path.insert(0, os.getcwd())
from main.version import VSVersionInfo

ffmpeg_bin = os.path.join(os.curdir, 'main', 'resources', 'ffmpeg-bin')
alass_bin = os.path.join(os.curdir, 'main', 'resources', 'alass-bin')
ffsubsync_bin = os.path.join(os.curdir, 'main', 'resources', 'ffsubsync-bin')

datas = [
    (os.path.join(os.curdir, 'main', 'resources', 'config.json'), '.'),
    (os.path.join(os.curdir, 'main', 'VERSION'), '.'),
    (os.path.join(os.curdir, 'main', 'settings.png'), '.'),
    (os.path.join(os.curdir, 'main', 'icon.ico'), '.')
]

with open('main/VERSION', 'r') as f:
    version = f.read().strip()

folder_name = f'AutoSubSync-v{version}'

a = Analysis(
    ['main/AutoSubSync.pyw'],
    pathex=[],
    binaries=[
        (ffmpeg_bin, 'resources/ffmpeg-bin'),
        (alass_bin, 'resources/alass-bin'),
        (ffsubsync_bin, 'resources/ffsubsync-bin'),
    ],
    datas=datas,
    hiddenimports=[],
    hookspath=['main/resources/hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AutoSubSync',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(os.curdir, 'main', 'icon.ico'),
    version=VSVersionInfo
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=folder_name,
)
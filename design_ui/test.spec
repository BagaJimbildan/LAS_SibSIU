# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/kildyaev_bo/PycharmProjects/LAS_SibSIU/main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/kildyaev_bo/PycharmProjects/LAS_SibSIU/static_info.py', '.'), ('C:/Users/kildyaev_bo/PycharmProjects/LAS_SibSIU/methods/start_info.py', '.'), ('C:/Users/kildyaev_bo/PycharmProjects/LAS_SibSIU/design_ui/ui_main.py', '.'), ('C:/Users/kildyaev_bo/PycharmProjects/LAS_SibSIU/design_ui/ui_main_script.py', '.')],
    hiddenimports=[],
    hookspath=[],
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
    a.binaries,
    a.datas,
    [],
    name='test',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

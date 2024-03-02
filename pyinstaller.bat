@echo off

python -m PyInstaller ^
    --noupx ^
    --noconfirm ^
    --log-level=WARN ^
    --onefile ^
    --noconsole ^
    --clean ^
    --name remid_cookie_grabber ^
    --icon=NONE ^
    remid_cookie_grabber.py

rmdir /s /q build
del remid_cookie_grabber.spec

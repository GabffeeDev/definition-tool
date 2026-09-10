@echo off
setlocal
cd /d "%~dp0"

set "ICON=..\tool.ico"

echo Instalando dependencias...
py -m pip install -r requirements.txt
if errorlevel 1 goto :error

if not exist "%ICON%" (
    echo.
    echo ERROR: No se encontro el icono:
    echo %ICON%
    goto :error
)

echo.
echo Compilando RenPy Tools...

py -m PyInstaller ^
    --noconfirm ^
    --clean ^
    --onefile ^
    --windowed ^
    --name "RenPy Tools" ^
    --icon "%ICON%" ^
    --add-data "%ICON%;." ^
    RenPy_Tools.py

if errorlevel 1 goto :error

echo.
echo ==========================================
echo Compilacion terminada correctamente.
echo El ejecutable esta en: dist\RenPy Tools.exe
echo El ejecutable y la ventana incluyen tool.ico
echo ==========================================
pause
exit /b 0

:error
echo.
echo Ocurrio un error durante la compilacion.
pause
exit /b 1

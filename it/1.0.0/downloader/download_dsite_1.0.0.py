import subprocess
import sys

print("Installer di DSite 1.0.0")

input("Premi INVIO per installare: ")

print("")

subprocess.check_call([
    sys.executable,
    "-m",
    "pip",
    "install",
    "dsite==1.0.0"
])

print("")
print("✅ Installazione OK")

input("Premi INVIO per chiudere: ")

import os
import shutil
import datetime

# Percorso della cartella dei mondi Minecraft
minecraft_saves = os.path.expanduser("~\\AppData\\Roaming\\.minecraft\\saves")

# Percorso della cartella di destinazione dei backup
backup_root = os.path.expanduser("e:\\Backup . Minecraft")

# Crea la cartella di backup se non esiste
os.makedirs(backup_root, exist_ok=True)

# Crea un nome univoco per il backup con data e ora
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_path = os.path.join(backup_root, f"backup_{timestamp}")

# Copia la cartella dei salvataggi
try:
    shutil.copytree(minecraft_saves, backup_path)
    print(f"✅ Backup completato: {backup_path}")
except Exception as e:
    print(f"❌ Errore durante il backup: {e}")

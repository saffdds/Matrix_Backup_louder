# Matrix_Backup_louder

🗂️ Automatic Backup of Minecraft Java Edition Worlds  
A simple Python script to safely save your Minecraft worlds with a single click.

🚀 What is Matrix_Backup_louder?

Matrix_Backup_louder is a Python script that automates the backup process of Minecraft Java Edition worlds.  
Each time you run it, it creates a full copy of the `saves` folder with a name based on date and time, so you never risk losing your progress.

🧠 Requirements

✅ Minecraft Java Edition  
✅ Python 3.13 (or compatible versions)  
✅ Windows operating system  
✅ Java installed (required to play Minecraft Java)

📥 Installation

1. Download Python from [python.org](https://www.python.org) or from the Microsoft Store.  
2. Clone or download this repository:  
   Click on **Code > Download ZIP** and extract the files.  
3. Open the folder and double-click on `matrix.py`.

📂 Where are backups saved?

Backups are saved in the folder:


You can change this path directly in the Python code.

🧾 How it works

The script:

- Detects the Minecraft worlds folder (`.minecraft\saves`)
- Creates a backup folder named like `backup_2025-09-29_13-30-00`
- Copies all worlds into the destination folder
- Displays a success or error message

🔒 Security

The script is open source and readable.  
It does not install anything, does not modify system files, and does not access the internet.  
It is designed to be simple and safe.

📌 Notes

- Works only with Minecraft Java Edition  
- Not compatible with Minecraft Bedrock (but can be adapted)  
- You can schedule automatic execution using Windows Task Scheduler

📧 Contact

Created by **saffdds**  
For suggestions, improvements, or bug reports, open an issue on GitHub.

🌐 Currently there is no website to download it, but one will be available in the future.

## Compatibility

The script was developed using **Python 3.13**, but it does not use features exclusive to this version.  
It should work correctly with earlier versions (e.g. Python 3.10+), but this is not guaranteed.

It is recommended to use Python 3.13 for maximum compatibility.

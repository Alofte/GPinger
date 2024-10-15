import keyboard
import subprocess
import os
import sys
import winreg as reg


def add_to_startup():
    """ Add this script to Windows startup using the registry with the key name 'GPinger'. """
    file_path = os.path.abspath(__file__)
    python_exe = sys.executable
    command = f'"{python_exe}" "{file_path}"'

    key = reg.HKEY_CURRENT_USER
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        with reg.OpenKey(key, key_path, 0, reg.KEY_ALL_ACCESS) as open_key:
            reg.SetValueEx(open_key, "GPinger", 0, reg.REG_SZ, command)
    except WindowsError:
        pass  # Silently fail if it cannot add to the registry


def is_in_startup():
    """ Check if the 'GPinger' entry exists in Windows startup. """
    key = reg.HKEY_CURRENT_USER
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        with reg.OpenKey(key, key_path, 0, reg.KEY_READ) as open_key:
            value, _ = reg.QueryValueEx(open_key, "GPinger")
            expected_command = f'"{sys.executable}" "{os.path.abspath(__file__)}"'
            return value == expected_command
    except FileNotFoundError:
        return False
    except WindowsError:
        return False


def ping_google():
    """ Open a command prompt and ping Google's DNS (8.8.8.8). """
    subprocess.Popen(["cmd", "/c", "start cmd /c ping 8.8.8.8 && pause"], shell=True)


if __name__ == "__main__":
    # Add to startup if not already in the registry
    if not is_in_startup():
        add_to_startup()

    # Register the hotkey (Ctrl + Shift + F12) to trigger the ping
    keyboard.add_hotkey('ctrl+shift+f12', ping_google)

    # Keep the script running to listen for the hotkey
    keyboard.wait()

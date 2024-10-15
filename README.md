# GPinger

**GPinger** is a simple Windows utility that allows you to ping Google's DNS (`8.8.8.8`) by pressing a hotkey combination (`Ctrl + Shift + F12`). The tool automatically runs at Windows startup, so it's always ready to respond to the hotkey.

## Features

- **Hotkey Trigger**: Press `Ctrl + Shift + F12` to quickly open a command prompt and ping Google's DNS.
- **Startup**: The executable automatically adds itself to the Windows startup, so it runs every time you log in.
- **No Console Window**: The executable runs in the background without showing any console window.

## How to Use

1. **Download the GPinger.exe** file.
2. **Run the `GPinger.exe`** file by double-clicking it.
   - The tool will register itself to run at Windows startup.
   - It will continue running in the background, waiting for the hotkey.
3. **Press `Ctrl + Shift + F12`** to open a command prompt and ping Google DNS (`8.8.8.8`).

## Installation

1. Download the `GPinger.exe` file.
2. Run the executable. It will automatically register itself to start with Windows.

### Uninstalling / Removing from Startup

To remove `GPinger` from running at startup, follow these steps:

1. **Open the Registry**:
   - Press `Win + R` and type `regedit`, then press Enter to open the Windows Registry Editor.
   
2. **Navigate to the following registry key**:
   ```
   HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
   ```

3. **Find the entry named `GPinger`** and delete it.

4. Optionally, delete the `GPinger.exe` file from wherever you downloaded it.

## FAQ

### What does GPinger do?

GPinger allows you to quickly ping Google's public DNS (`8.8.8.8`) by pressing a hotkey (`Ctrl + Shift + F12`). This is useful for quickly checking your internet connection.

### Does GPinger require installation?

No, `GPinger.exe` is a standalone file. Simply download and run it. It will automatically add itself to Windows startup.

### How do I stop GPinger from running on startup?

You can remove the startup entry by manually deleting it from the Windows Registry. See the **Uninstalling / Removing from Startup** section above.

### Will GPinger work if I don't have Python installed?

Yes, `GPinger.exe` is a standalone executable that doesn't require Python to be installed on your system.

## Contact & Contribution

I'm always open to feedback, collaboration, and contributions! If you have any questions, spot a bug, or want to discuss potential improvements, feel free to reach out or submit an issue or pull request.

### Get in Touch

- **GitHub**: [Alofte](https://github.com/Alofte)
- **LinkedIn**: [Alofte](https://www.linkedin.com/in/alofte-py-090680304/)
- **Email**: [aloft.dev@gmail.com](mailto:aloft.dev@gmail.com)

### Contributions

Whether you have a suggestion, found a bug, or want to contribute to the project, your input is highly appreciated. Here’s how you can help:

- **Submit an Issue**: If you find any bugs or have ideas for enhancements, please submit an issue on GitHub.
- **Pull Requests**: Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.
- **Collaboration**: If you're interested in collaborating on a feature or project, don't hesitate to get in touch.

Thank you for your support and interest in this project!  
Don't forget to ⭐ the project ❤️.

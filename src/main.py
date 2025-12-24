"""Minimal GUI application showing a window with background color #212328.
Run locally with Python; build an .exe via PyInstaller.
"""

import tkinter as tk

WINDOW_BG = "#212328"
WINDOW_TITLE = "Steam-Phish"
WINDOW_SIZE = "500x600"


def main() -> None:
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)
    root.configure(bg=WINDOW_BG)
    root.resizable(False, False)

    root.mainloop()


if __name__ == "__main__":
    main()

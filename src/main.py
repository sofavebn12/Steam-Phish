"""Minimal GUI application showing a window with background color #212328.
Run locally with Python; build an .exe via PyInstaller.
"""

import tkinter as tk

WINDOW_BG = "#212328"
WINDOW_TITLE = "Steam-Phish"
WINDOW_SIZE = "800x500"


def main() -> None:
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)
    root.configure(bg=WINDOW_BG)
    root.resizable(False, False)

    # Add a simple label so the window is not empty.
    label = tk.Label(
        root,
        text="Placeholder window",
        bg=WINDOW_BG,
        fg="white",
        font=("Segoe UI", 12),
    )
    label.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()

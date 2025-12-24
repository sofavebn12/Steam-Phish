"""Minimal GUI application showing a window with background color #1e1f22
and a custom top bar with a close button.

Run locally with Python; build an .exe via PyInstaller.
"""

import tkinter as tk

WINDOW_BG = "#1e1f22"
WINDOW_TITLE = "Steam-Phish"
WINDOW_SIZE = "600x350"


def main() -> None:
    root = tk.Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)
    root.configure(bg=WINDOW_BG)
    root.resizable(False, False)

    # Remove native title bar and build a custom top bar
    root.overrideredirect(True)

    title_bar = tk.Frame(root, bg=WINDOW_BG, height=36)
    title_bar.pack(side="top", fill="x")

    # No title text label per requirements

    # Close button inside a wrapper frame to draw a red square outline on hover
    close_wrap = tk.Frame(title_bar, bg=WINDOW_BG)
    close_label = tk.Label(
        close_wrap,
        text="✕",
        bg=WINDOW_BG,
        fg="#c7c9cc",
        width=2,
    )
    close_label.pack(padx=0, pady=0)
    close_wrap.pack(side="right", padx=8, pady=8)

    def on_close(_event=None) -> None:
        root.destroy()

    def on_close_enter(_event=None) -> None:
        # Fill entire square with red; keep the cross visible (gray)
        close_label.configure(bg="#e22a27", fg="#c7c9cc")

    def on_close_leave(_event=None) -> None:
        close_label.configure(bg=WINDOW_BG, fg="#c7c9cc")

    close_label.bind("<Button-1>", on_close)
    close_label.bind("<Enter>", on_close_enter)
    close_label.bind("<Leave>", on_close_leave)

    # Drag window by the custom title bar
    drag_offset = {"x": 0, "y": 0}

    def start_move(event) -> None:
        drag_offset["x"] = event.x
        drag_offset["y"] = event.y

    def on_move(event) -> None:
        x = event.x_root - drag_offset["x"]
        y = event.y_root - drag_offset["y"]
        root.geometry(f"{root.winfo_width()}x{root.winfo_height()}+{x}+{y}")

    title_bar.bind("<ButtonPress-1>", start_move)
    title_bar.bind("<B1-Motion>", on_move)

    root.mainloop()


if __name__ == "__main__":
    main()

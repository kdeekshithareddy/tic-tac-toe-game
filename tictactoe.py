import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
def _init_(self, master):
self.master = master
master.title("Tic-Tac-Toe")

# INITIALIZE GAME VARIABLES
self.current_player = "X"
self.board = ["", "", "", "", "", "", "", "", ""]

# CREATE GUI ELEMENTS
self.buttons = []
for i in range(9):
button = tk.Button(master, text="", width=3, height=1, command=lambda
i=i: self.on_click(i))
button.grid(row=i // 3, column=i % 3)
self.buttons.append(button)

# CREATE MENU
menubar = tk.Menu(master)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New Game", command=self.new_game)
filemenu.add_command(label="Quit", command=self.quit)
menubar.add_cascade(label="Tic-Tac-Toe", menu=filemenu)
master.config(menu=menubar)

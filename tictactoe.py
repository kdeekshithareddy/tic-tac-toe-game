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

self.new_game()

def new_game(self):
self.current_player = "X"
self.board = ["", "", "", "", "", "", "", "", ""]
for button in self.buttons:
button.config(text="")
messagebox.showinfo("New Game", "Let's play Tic Tac Toe!")

def quit(self):
  self.master.quit()

def on_click(self, index):
if self.board[index] == "":
self.board[index] = self.current_player
self.buttons[index].config(text=self.current_player)
if self.check_win():
messagebox.showinfo("Game Over", f"{self.current_player} wins!")
self.new_game()
elif self.check_draw():
messagebox.showinfo("Game Over", "It's a draw!")
self.new_game()
else:
self.current_player = "O" if self.current_player == "X" else "X"
def check_win(self):
return (self.board[0] == self.board[1] == self.board[2] != "") or \
(self.board[3] == self.board[4] == self.board[5] != "") or \
(self.board[6] == self.board[7] == self.board[8] != "") or \
(self.board[0] == self.board[3] == self.board[6] != "") or \
(self.board[1] == self.board[4] == self.board[7] != "") or \

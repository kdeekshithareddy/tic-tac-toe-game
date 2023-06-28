import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
def _init_(self, master):
self.master = master
master.title("Tic-Tac-Toe")

# INITIALIZE GAME VARIABLES
self.current_player = "X"
self.board = ["", "", "", "", "", "", "", "", ""]

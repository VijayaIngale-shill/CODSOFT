import tkinter as tk
import random
from tkinter import messagebox

user_score, comp_score, round_no = 0, 0, 0    # track the scores and rounds
TOTAL_ROUNDS = 5
choices = ["rock", "paper", "scissors"]
Emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
Colors = {"win": "#27ae60", "loss": "#e74c3c", "tie": "#2980b9"}


def computer_choice():       
    return random.choice(choices)

def decide_winner(user, computer):    #games logic if rock will beat scissors and scissors will beat paper and paper will beat the rock
    if user == computer:
        return "tie"
    rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "user" if rules[user] == computer else "computer"

def play(user_choice):      #make choice for user and computer and decide the winner
    global user_score, comp_score, round_no
    round_no += 1
    comp_choice = computer_choice()
    result = decide_winner(user_choice, comp_choice)

    if result == "user":           
        user_score += 1
        text, color = "✅ You Win this Round!", Colors["win"]
        lbl_user.config(bg="#27ae60")
        lbl_comp.config(bg="#045ab0")
    elif result == "computer":
        comp_score += 1
        text, color = "❌ Computer Wins this Round!", Colors["loss"]
        lbl_user.config(bg="#1164b7")
        lbl_comp.config(bg="#e74c3c")
    else:
        text, color = "🤝 It's a Tie!", Colors["tie"]
        lbl_user.config(bg="#0070bb")
        lbl_comp.config(bg="#0070bb")

    lbl_round.config(text=f"Round: {round_no}")
    lbl_user.config(text=f"You chose: {Emojis[user_choice]}")
    lbl_comp.config(text=f"Computer chose: {Emojis[comp_choice]}")
    lbl_result.config(text=text, fg=color)
    lbl_score_user.config(text=f"You: {user_score}")
    lbl_score_computer.config(text=f"Computer: {comp_score}")

    if round_no == TOTAL_ROUNDS:
        winner = "You 🎉" if user_score > comp_score else "Computer 🤖"
        if user_score == comp_score:
            winner = "It's a Tie!"
        messagebox.showinfo("Game Over", f"🏆 Final Winner: {winner}")
        reset_game()

def reset_game():           #reset all the scores and rounds
    global user_score, comp_score, round_no
    user_score = comp_score = round_no = 0
    lbl_round.config(text="Round: 0")
    lbl_user.config(text="You chose: -", bg="#1d78d3")
    lbl_comp.config(text="Computer chose: -", bg="#1d78d3")
    lbl_result.config(text="Result: Make your move!", fg="white")
    lbl_score_user.config(text="You: 0")
    lbl_score_computer.config(text="Computer: 0")


root = tk.Tk()
root.title("Rock-Paper-Scissor Game")
root.geometry("450x500")
root.configure(bg="#2c3e50")

tk.Label(root, text="Rock-Paper-Scissor", font=("Helvetica", 20, "bold"),
         bg="#2a547d", fg="white", pady=10).pack(fill="x") #Title of the game

lbl_total_rounds= tk.Label(root,text="Total Rounds: 5",
                           font=("Arial",12),bg="#2c3e50",fg="white")  #For showing Total Rounds
lbl_total_rounds.pack(pady=5)  #pady for spacing above and below

lbl_round = tk.Label(root, text="Round: 0", bg="#34495e", 
                     fg="white", font=("Arial", 12)) # Total rounds played or remaining
lbl_round.pack(pady=10)

choice_frame = tk.Frame(root, bg="#2c3e50")
choice_frame.pack(pady=10)

lbl_user = tk.Label(choice_frame, text="You chose: -", bg="#1874d0", fg="white",
                    font=("Arial", 12), width=20, pady=5)
lbl_user.grid(row=0, column=0, padx=5)

lbl_comp = tk.Label(choice_frame, text="Computer chose: -", bg="#1d6fc1", fg="white",
                    font=("Arial", 12), width=20, pady=5)
lbl_comp.grid(row=0, column=1, padx=5)

lbl_result = tk.Label(root, text="Result: Make your move!", 
                      font=("Arial", 14, "bold"),bg="#2c3e50", fg="white", pady=10)
lbl_result.pack(pady=15)

score_frame = tk.Frame(root, bg="#2c3e50")
score_frame.pack(pady=10)

lbl_score_user = tk.Label(score_frame, text="You: 0", bg="#27ae60", 
                          fg="white",font=("Arial", 12, "bold"), width=12, pady=5)
lbl_score_user.grid(row=0, column=0, padx=10)

lbl_score_computer = tk.Label(score_frame, text="Computer: 0", bg="#e74c3c", 
                          fg="white",font=("Arial", 12, "bold"), width=12, pady=5)
lbl_score_computer.grid(row=0, column=1, padx=10)

btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=20)

for i, ch in enumerate(choices):
    b = tk.Button(btn_frame, text=Emojis[ch], font=("Helvetica", 22), width=5, relief="ridge",
                  bg="#3498db", fg="white", command=lambda c=ch: play(c))
    b.grid(row=0, column=i, padx=10)

tk.Button(root, text="🔄 Reset Game", bg="#e67e22", fg="white",
          font=("Arial", 12, "bold"), command=reset_game).pack(pady=10)

root.mainloop()

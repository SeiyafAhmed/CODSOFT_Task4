from ttkbootstrap import *
import random

root = Window("Rock Paper Scissor", size=(500, 600), resizable=(False, False))
root.iconbitmap("./logo.ico")

comp_score = IntVar(value=0)
plyr_score = IntVar(value=0)
hands = []

top = Frame(root, width=500, height=100)
top.pack(pady=20)
comp_box = LabelFrame(top, text="Computer", width=100, style="danger")
comp_box.pack(side=LEFT, padx=10)

plyr_box = LabelFrame(top, text="Player", width=100, style="success")
plyr_box.pack(side=RIGHT, padx=10)

Entry(comp_box, textvariable=comp_score, width=10, justify="center", font=("dubai", 20, "bold"), state="disabled", style="light").pack()
Entry(plyr_box, textvariable=plyr_score, width=10, justify="center", font=("dubai", 20, "bold"), state="disabled", style="light").pack()


game_zone = Button(root, text="\n"*15, width=65, cursor=None, style="warning-outline", state="disabled")
game_zone.place(y=120, x=50)

plyr_hand_img = PhotoImage(file="./player/rock.png",)
comp_hand_img = PhotoImage(file="./computer/rock.png")

plyr_hand = Label(game_zone, image=plyr_hand_img)
comp_hand = Label(game_zone, image=comp_hand_img)

y = 0.5
plyr_hand.place(relx=0.75, rely=y, anchor="center")
comp_hand.place(relx=0.25, rely=y, anchor="center")
a = 0.01
n = 120


class Hand:
    def __init__(self, master, img, thumbnail):
        self.img = PhotoImage(file=img)
        self.path = img
        self.thumbnail = PhotoImage(file=thumbnail)
        self.master = master

        self.btn = Button(self.master, image=self.thumbnail, command=self.click)
        self.btn.pack(side=LEFT)

    def click(self):
        self.disable()
        plyr_hand.config(image=plyr_hand_img)
        comp_hand.config(image=comp_hand_img)
        moves = ["./computer/rock.png", "./computer/paper.png", "./computer/scissor.png"]
        self.comp_path = random.choice(moves)
        self.comp_img = PhotoImage(file=self.comp_path)
        self.move(self.img, self.comp_img)
        self.comp = self.comp_path.split("/")[2].split(".")[0]
        self.plyr = self.path.split("/")[2].split(".")[0]


    def disable(self):
        for hand in hands:
            hand.btn.config(state="disabled")

    def active(self):
        for hand in hands:
            hand.btn.config(state="normal")

    def move(self, plyr, comp):
        global y, a, n

        if y < 0.4:
            a = 0.01
        if y > 0.6:
            a = -0.01
        y += a
        n -= 1
        if n == 0:
            comp_hand.config(image=comp)
            plyr_hand.config(image=plyr)
            n = 120
            global plyr_score, comp_score
            if self.comp == self.plyr:
                pass

            elif self.comp == "rock":
                if self.plyr == "paper":
                    plyr_score.set(plyr_score.get()+1)
                else:
                    comp_score.set(comp_score.get()+1)

            elif self.comp == "paper":
                if self.plyr == "scissor":
                    plyr_score.set(plyr_score.get() + 1)
                else:
                    comp_score.set(comp_score.get() + 1)

            elif self.comp == "scissor":
                if self.plyr == "rock":
                    plyr_score.set(plyr_score.get() + 1)
                else:
                    comp_score.set(comp_score.get() + 1)

            self.active()
            return 0

        plyr_hand.place(rely=y)
        comp_hand.place(rely=y)
        root.after(5, lambda: self.move(plyr, comp))


bottom = Frame(root, width=500)
bottom.pack()
bottom.place(x=-12, y=400)

hands.append(Hand(bottom, "./player/rock.png", "./player/rock-s.png"))
hands.append(Hand(bottom, "./player/paper.png", "./player/paper-s.png"))
hands.append(Hand(bottom, "./player/scissor.png", "./player/scissor-s.png"))

footer = Frame(root, style="dark",)
footer.pack(side=BOTTOM)
Label(footer, text="©2024 Seiyaf Ahmed", style="inverse-dark", justify="right",).pack(padx=193)

root.mainloop()

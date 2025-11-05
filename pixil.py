import tkinter as tk
from tkinter import ttk
import random

root = tk.Tk()
root.title("Pixil")

c = tk.Canvas(width=1200, height=700, background="black")
c.grid(row=0, column=0, rowspan=10)
c.focus_set()

def points():
    global x, y, l
    points = [(x+l, y-10*l), 
            (x+l, y-8*l), 
            (x+2*l, y-8*l), 
            (x+2*l, y-7*l),
            (x+3*l, y-7*l), 
            (x+3*l, y-6*l),
            (x+4*l, y-6*l), 
            (x+4*l, y-5*l),
            (x+5*l, y-5*l), 
            (x+5*l, y-4*l),
            (x+12*l, y-4*l),
            (x+12*l, y-5*l),
            (x+13*l, y-5*l),
            (x+13*l, y-6*l),
            (x+14*l, y-6*l),
            (x+14*l, y-7*l),
            (x+15*l, y-7*l),
            (x+15*l, y-10*l),
            (x+16*l, y-10*l),
            (x+16*l, y-9*l),
            (x+17*l, y-9*l),
            (x+17*l, y-11*l),
            (x+15*l, y-11*l),
            (x+15*l, y-13*l),
            (x+18*l, y-13*l),
            (x+18*l, y-14*l),
            (x+16*l, y-14*l),
            (x+16*l, y-15*l),
            (x+20*l, y-15*l),
            (x+20*l, y-18*l),
            (x+19*l, y-18*l),
            (x+19*l, y-19*l),
            (x+13*l, y-19*l),
            (x+13*l, y-18*l),
            (x+12*l, y-18*l),
            (x+12*l, y-13*l),
            (x+11*l, y-13*l),
            (x+11*l, y-12*l),
            (x+10*l, y-12*l),
            (x+10*l, y-11*l),
            (x+9*l, y-11*l),
            (x+9*l, y-10*l),
            (x+8*l, y-10*l),
            (x+8*l, y-9*l),
            (x+7*l, y-9*l),
            (x+7*l, y-8*l),
            (x+6*l, y-8*l),
            (x+6*l, y-7*l),
            (x+4*l, y-7*l),
            (x+4*l, y-8*l),
            (x+3*l, y-8*l),
            (x+3*l, y-9*l),
            (x+2*l, y-9*l),
            (x+2*l, y-10*l),
            ]
    return points

def idle(x, y):
    leg1 = [(x+6*l, y-4*l),
            (x+6*l, y),
            (x+8*l, y),
            (x+8*l, y-l),
            (x+7*l, y-l),
            (x+7*l, y-2*l),
            (x+8*l, y-2*l),
            (x+8*l, y-3*l),
            (x+9*l, y-3*l),
            (x+9*l, y-4*l)
            ]
    leg2 = [(x+10*l, y-4*l),
            (x+10*l, y-3*l),
            (x+11*l, y-3*l),
            (x+11*l, y),
            (x+13*l, y),
            (x+13*l, y-l),
            (x+12*l, y-l),
            (x+12*l, y-4*l)
            ]
    return leg1, leg2


def step(x, y, n):
    if n == 0:
        leg1 = [(x+6*l, y-4*l),
                (x+6*l, y-3*l),
                (x+7*l, y-3*l),
                (x+7*l, y-2*l),
                (x+9*l, y-2*l),
                (x+9*l, y-3*l),
                (x+8*l, y-3*l),
                (x+8*l, y-4*l)
                ]
        leg2 = [(x+10*l, y-4*l),
            (x+10*l, y-3*l),
            (x+11*l, y-3*l),
            (x+11*l, y),
            (x+13*l, y),
            (x+13*l, y-l),
            (x+12*l, y-l),
            (x+12*l, y-4*l)
            ]
    elif n == 1:
        leg2 = [(x+11*l, y-4*l),
                (x+11*l, y-2*l),
                (x+13*l, y-2*l),
                (x+13*l, y-3*l),
                (x+12*l, y-3*l),
                (x+12*l, y-4*l)]
        leg1 = [(x+6*l, y-4*l),
            (x+6*l, y),
            (x+8*l, y),
            (x+8*l, y-l),
            (x+7*l, y-l),
            (x+7*l, y-2*l),
            (x+8*l, y-2*l),
            (x+8*l, y-3*l),
            (x+9*l, y-3*l),
            (x+9*l, y-4*l)
            ]
    return leg1, leg2

def hurt(x,y):
    white = c.create_rectangle(x+l*16.5, y-18.5*l, x+l*13.5, y-15.5*l, fill="white")
    black = c.create_rectangle(x+l*15.5, y-17.5*l, x+l*14.5, y-16.5*l, fill="black", outline="")
    return black, white

def make_stone():
    global thing_pos, l
    s_x = random.randint(1210, 2100)
    s_y = random.choice(thing_pos)
    stone_p = [(s_x, s_y-5*l),
            (s_x, s_y-3*l),
            (s_x+1*l, s_y-3*l),
            (s_x+1*l, s_y-2*l),
            (s_x+2*l, s_y-2*l),
            (s_x+2*l, s_y-l),
            (s_x+3*l, s_y-l),
            (s_x+3*l, s_y),
            (s_x+7*l, s_y),
            (s_x+7*l, s_y-l),
            (s_x+8*l, s_y-l),
            (s_x+8*l, s_y-2*l),
            (s_x+9*l, s_y-2*l),
            (s_x+9*l, s_y-3*l),
            (s_x+10*l, s_y-3*l),
            (s_x+10*l, s_y-4*l),
            (s_x+11*l, s_y-4*l),
            (s_x+11*l, s_y-5*l),
            (s_x+11*l, s_y-7*l),
            (s_x+10*l, s_y-7*l),
            (s_x+10*l, s_y-8*l),
            (s_x+9*l, s_y-8*l),
            (s_x+9*l, s_y-9*l),
            (s_x+8*l, s_y-9*l),
            (s_x+8*l, s_y-10*l),
            (s_x+7*l, s_y-10*l),
            (s_x+7*l, s_y-11*l),
            (s_x+6*l, s_y-11*l),
            (s_x+6*l, s_y-10*l),
            (s_x+5*l, s_y-10*l),
            (s_x+5*l, s_y-9*l),
            (s_x+4*l, s_y-9*l),
            (s_x+4*l, s_y-8*l),
            (s_x+3*l, s_y-8*l),
            (s_x+3*l, s_y-7*l),
            (s_x+2*l, s_y-7*l),
            (s_x+2*l, s_y-6*l),
            (s_x+l, s_y-6*l),
            (s_x+l, s_y-5*l)
            ]
    return stone_p

def small_heart(h_x, h_y):
    global l
    s_heart_points = [
        (h_x+l, h_y),
        (h_x+l, h_y+l),
        (h_x, h_y+l),
        (h_x, h_y+3*l),
        (h_x+l, h_y+3*l),
        (h_x+l, h_y+4*l),
        (h_x+2*l, h_y+4*l),
        (h_x+2*l, h_y+5*l),
        (h_x+3*l, h_y+5*l),
        (h_x+3*l, h_y+6*l),
        (h_x+4*l, h_y+6*l),
        (h_x+4*l, h_y+5*l),
        (h_x+5*l, h_y+5*l),
        (h_x+5*l, h_y+4*l),
        (h_x+6*l, h_y+4*l),
        (h_x+6*l, h_y+3*l),
        (h_x+7*l, h_y+3*l),
        (h_x+7*l, h_y+l),
        (h_x+6*l, h_y+l),
        (h_x+6*l, h_y),
        (h_x+4*l, h_y),
        (h_x+4*l, h_y+l),
        (h_x+3*l, h_y+l),
        (h_x+3*l, h_y)
    ]
    return s_heart_points

def big_heart():
    global l, thing_pos
    s_x = random.randint(1210, 2100)
    s_y = random.choice(thing_pos)
    b_heart_points = [
        (s_x+6*l, s_y),
        (s_x+7*l, s_y),
        (s_x+7*l, s_y-l),
        (s_x+8*l, s_y-l),
        (s_x+8*l, s_y-2*l),
        (s_x+9*l, s_y-2*l),
        (s_x+9*l, s_y-3*l),
        (s_x+10*l, s_y-3*l),
        (s_x+10*l, s_y-4*l),
        (s_x+11*l, s_y-4*l),
        (s_x+11*l, s_y-5*l),
        (s_x+12*l, s_y-5*l),
        (s_x+12*l, s_y-6*l),
        (s_x+13*l, s_y-6*l),
        (s_x+13*l, s_y-8*l),
        (s_x+12*l, s_y-8*l),
        (s_x+12*l, s_y-9*l),
        (s_x+11*l, s_y-9*l),
        (s_x+11*l, s_y-10*l),
        (s_x+10*l, s_y-10*l),
        (s_x+10*l, s_y-11*l),
        (s_x+8*l, s_y-11*l),
        (s_x+8*l, s_y-10*l),
        (s_x+7*l, s_y-10*l),
        (s_x+7*l, s_y-9*l),
        (s_x+6*l, s_y-9*l),
        (s_x+6*l, s_y-10*l),
        (s_x+5*l, s_y-10*l),
        (s_x+5*l, s_y-11*l),
        (s_x+3*l, s_y-11*l),
        (s_x+3*l, s_y-10*l),
        (s_x+2*l, s_y-10*l),
        (s_x+2*l, s_y-9*l),
        (s_x+l, s_y-9*l),
        (s_x+l, s_y-8*l),
        (s_x, s_y-8*l),
        (s_x, s_y-6*l),
        (s_x+l, s_y-6*l),
        (s_x+l, s_y-5*l),
        (s_x+2*l, s_y-5*l),
        (s_x+2*l, s_y-4*l),
        (s_x+3*l, s_y-4*l),
        (s_x+3*l, s_y-3*l),
        (s_x+4*l, s_y-3*l),
        (s_x+4*l, s_y-2*l),
        (s_x+5*l, s_y-2*l),
        (s_x+5*l, s_y-l),
        (s_x+6*l, s_y-l)
    ]
    return b_heart_points

def dino_move(mode, x, y):
    global legs, one, two, count
    try:
        for i in legs:
            c.delete(i)
    except NameError:
        return
    if mode == "idle" or mode == "hurt":
        leg1, leg2 = idle(x, y)
    elif mode =="step":
        leg1, leg2 = step(x, y, count)
        if count == 0:
            count = 1
        else:
            count = 0
    one = c.create_polygon(leg1, fill=new_color_dino, outline="")
    two = c.create_polygon(leg2, fill=new_color_dino, outline="")
    legs = [one, two]
    if mode == "hurt":
        black, white = hurt(x, y)
        legs.append(black)
        legs.append(white)


mode = "idle"
l = 8

def change_bg():
    global num_bg, bg_color, fg_color, widgets
    if num_bg.get() == 0:
        c.config(bg="white")
        for i in ch_widgets:
            i.config(bg="white", fg="black")
        bg_color = "white"
        fg_color="black"
    else:
        c.config(bg="black")
        for i in ch_widgets:
            i.config(bg="black", fg="white")
        bg_color = "black"
        fg_color="white"

def dino_color_selected(v_name, index, write):              
    global dino_color, new_color_dino, body, legs
    n_color = d_color.get()
    print(f"New color = {n_color}")
    if n_color == "green":
        new_color_dino = "chartreuse"
    elif n_color == "red":
        new_color_dino = "crimson"
    elif n_color == "blue":
        new_color_dino = "dodgerblue"
    elif n_color == "gold":
        new_color_dino = "gold"
    elif n_color == "purple":
        new_color_dino = "mediumpurple"
    elif n_color == "pink":
        new_color_dino = "fuchsia"
    else:
        try:
            if n_color:
                c.itemconfig(body, fill=n_color)
                new_color_dino = n_color
        except tk.TclError:
            pass
    c.itemconfig(body, fill=new_color_dino)
    for i in legs:
        c.itemconfig(i, fill=new_color_dino)



def stone_fce():
    global stone_list, score_num, score, obj_speed
    stone_color = ["magenta", "cyan", "gray", "chocolate", "peru", "darkorange"]
    for i in stone_list:
        c.move(i, -obj_speed, 0)
        if c.bbox(i)[2] <= random.randint(-100, -10):
            c.itemconfig(i, fill=random.choice(stone_color))
            if c.bbox(i)[0] <= 0:
                score_num += 1
                score.set(score_num)
            if c.bbox(i)[3] > 600:
                n_y = random.choice([0, -200, -400])
            elif c.bbox(i)[3] < 300:
                n_y = random.choice([0, 200, 400])
            else:
                n_y = random.choice([0, 200, -200])
            c.move(i, random.randint(1210, 1800), n_y)

def move_up(event):
    global body, one, two, eye, legs, x, y, mode, new_color_dino
    if mode == "step":
        if c.bbox(body)[3] > 300:
            c.delete(body)
            c.delete(eye)
            for i in legs:
                c.delete(i)
            y -= 200
            body = c.create_polygon(points(), fill=new_color_dino, outline="")
            dino_move(mode, x, y)
            eye = c.create_rectangle(x+l*15.5, y-17.5*l, x+l*14.5, y-16.5*l, fill="black", outline="")

    

def move_down(event):
    global body, one, two, eye, legs, x, y, mode, new_color_dino
    if mode == "step":
        if c.bbox(body)[3] < 600:
            c.delete(body)
            c.delete(eye)
            for i in legs:
                c.delete(i)
            y += 200
            body = c.create_polygon(points(), fill=new_color_dino, outline="")
            dino_move(mode, x, y)
            eye = c.create_rectangle(x+l*15.5, y-17.5*l, x+l*14.5, y-16.5*l, fill="black", outline="")

def collisions():
    global stone_list, collis, s_hearts_list, l
    for i in stone_list:
        stone_box = c.bbox(i)
        dino_box = c.bbox(body)
        if not (stone_box[2] < dino_box[0] or  
                stone_box[0] > dino_box[2] or  
                stone_box[3] < dino_box[1] or  
                stone_box[1] > dino_box[3]):
            collis = True
            c.delete(s_hearts_list[-1])
            break


def recursion():
    global stone_list, score_num, stone2, stone_list, speed, nn, done, obj_speed
    c.after(speed, lambda: dino_move(mode, x, y))
    c.after(speed, stone_fce)
    c.after(speed, collisions)
    if score_num == 20 and done == False:
        stone2 = c.create_polygon(make_stone(), fill="cyan", outline="")
        stone_list.append(stone2)
        done = True
    if score_num == 25:
        done = False
    if score_num == 40 and done == False:
        stone3 = c.create_polygon(make_stone(), fill="chocolate", outline="")
        stone_list.append(stone3)
        done = True
    if score_num >= nn:
        speed -= 1
        obj_speed += 5
        nn += nn+1
    if collis == False:
        c.after(speed, recursion)
    else:
        for i in stone_list:
            c.delete(i)
            stone_list = []
        menu()


def game_start():
    global widgets, mode, body, legs, eye, one, two, x, y, count, stone_list, collis, real_name, score_num, score, nn, s_heart, s_hearts_list
    for i in widgets:
        c.delete(i)
    collis = False
    mode = "step"
    x = 100
    y = 480
    nn = 2
    real_name = name_Str.get()
    score.set(0)
    score_num = 0
    c.focus_set()
    c.delete(body)
    c.delete(eye)
    for i in legs:
        c.delete(i)
    body = c.create_polygon(points(), fill=new_color_dino, outline="")
    eye = c.create_rectangle(x+l*15.5, y-17.5*l, x+l*14.5, y-16.5*l, fill="black", outline="")
    count = 0
    leg1, leg2 = step(x, y, count)
    one = c.create_polygon(leg1, fill=new_color_dino, outline= "")
    two = c.create_polygon(leg2, fill=new_color_dino, outline= "")
    legs = one, two
    stone0 = c.create_polygon(make_stone(), fill="gray", outline="")
    stone1 = c.create_polygon(make_stone(), fill="magenta", outline="")
    stone_list = [stone0, stone1]
    s_heart = c.create_polygon(small_heart(1100, 20), fill="red", outline="")
    s_hearts_list = [s_heart]
    recursion()


def menu():
    global mode, x, y, l, body, eye, name_Str, num_bg, widgets, one, two, legs, bg_color, fg_color, ch_widgets, real_name, dino_color, d_color, new_color_dino, high_score, s_heart
    x = 150
    y = 480
    if collis == True:
        mode = "hurt"
        c.delete(body)
        c.delete(eye)
        for i in legs:
            c.delete(i)
        body = c.create_polygon(points(), fill=new_color_dino, outline="")
        white = c.create_rectangle(x+l*16.5, y-18.5*l, x+l*13.5, y-15.5*l, fill="white")
        eye = c.create_rectangle(x+l*15.5, y-17.5*l, x+l*14.5, y-16.5*l, fill="black", outline="")
        leg1, leg2 = idle(x, y)
        one = c.create_polygon(leg1, fill=new_color_dino, outline= "")
        two = c.create_polygon(leg2, fill=new_color_dino, outline= "")
        legs = [one, two, white]
        c.after(1000, lambda: dino_move("idle", x, y))
    else:
        body = c.create_polygon(points(), fill=new_color_dino, outline="")
        dino_move(mode, x, y)
        eye = c.create_rectangle(x+l*15.5, y-17.5*l, x+l*14.5, y-16.5*l, fill="black", outline="")
    label_name = tk.Label(root, text = "Your name", font=100, bg = bg_color, fg=fg_color)
    label_w = c.create_window(900, 150, window=label_name)
    name_Str = tk.StringVar(value=real_name)
    name = tk.Entry(root, font=100,  textvariable = name_Str)
    name_w = c.create_window(900, 190, window=name)
    start = tk.Button(root, font=200, text = "Start game", command=game_start,  bg="violet")
    start_w = c.create_window(900, 300, window=start)
    num_bg = tk.IntVar()
    light = tk.Radiobutton(root, font = 70, text="light mode", value = 0, bg = bg_color, fg=fg_color, variable = num_bg, command = change_bg)
    dark = tk.Radiobutton(root, font = 70, text="dark mode", value = 1, bg = bg_color, fg=fg_color, variable = num_bg, command = change_bg)
    dark_w = c.create_window(900, 400, window=light)
    light_w = c.create_window(900, 430, window=dark)
    d_color = tk.StringVar()
    d_color.trace_add("write", dino_color_selected)
    dino_color = ttk.Combobox(root, width=20, textvariable=d_color) 
    dino_color["values"] = ("green", "red", "blue", "gold", "purple", "pink") 
    color_w = c.create_window(975, 500, window=dino_color)
    text = tk.Label(root, text = "Dino color: ", font=70, bg = bg_color, fg=fg_color)
    text_w = c.create_window(825, 500, window=text)
    ch_widgets = [label_name, light, dark, text, score]      #dino_color, name, start
    widgets = [label_w, light_w, dark_w, text_w, start_w, name_w, color_w] 
    if high_score < score_num:
            high_score = score_num
            label_high = tk.Label(root, font=200, bg = bg_color, fg=fg_color)
            if real_name:
                label_high.config(text = f"Congrats {real_name}!!")
            else:
                label_high.config(text = f"Congrats you nameless idiot!!")
            high_w = c.create_window(350, 150, window=label_high)
            label_got = tk.Label(root, text = "You got new high score!!", font=200, bg = bg_color, fg=fg_color)
            got_w = c.create_window(350, 200, window=label_got)
            if label_high not in ch_widgets:
                ch_widgets.append(label_high)
            if high_w not in ch_widgets:
                widgets.append(high_w)
            if label_got not in ch_widgets:
                ch_widgets.append(label_got)
            if got_w not in widgets:
                widgets.append(got_w)

    
mode = "idle"
l = 8
collis = False
count = 0
legs = []
body = None
c.bind_all("w", move_up)
root.bind("<Up>", move_up)
c.bind_all("s", move_down)
root.bind("<Down>", move_down)
d_color = tk.StringVar()
d_color.trace_add("write", dino_color_selected)
dino_color = ttk.Combobox(root, width=20, textvariable=d_color, state = "r")
dino_color["values"] = ("green", "red", "blue", "gold", "purple", "pink")
dino_color.current(0)
new_color_dino = "chartreuse"
bg_color="black"
fg_color="white"
real_name = ""
score_num = 0
score = tk.IntVar(value=score_num)
score_text = tk.Label(root, textvariable = score, font=("Arial", 25, "bold"), bg = bg_color, fg=fg_color)
score_w = c.create_window(100, 50, window=score_text)
high_score = 0
thing_pos = [470, 270, 670]
speed = 75
nn = 2
obj_speed = 20
done = False

menu()

root.mainloop()
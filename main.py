from tkinter import *
from ctransformers import AutoModelForCausalLM

# LLM
llm = AutoModelForCausalLM.from_pretrained("model\\llama-2-7b-chat.ggmlv3.q2_K.bin", model_type="llama", gpu_layers=32)

def send_prompt():
    global label, entry
    default_prompt="You are an assistant named Rocky. Please answer my question as simple as possible."
    label.config(text=llm(default_prompt+" "+entry.get()))

# tkinter configuration
root = Tk()
root.config(bg = '#add123')
root.wm_attributes('-transparentcolor','#add123')
root.wm_attributes('-fullscreen', 'True')

total_frame = Frame(root, background="#add123")
total_frame.place(x=1500, y=500)

# text, inputbox, button elements
frame1 = Frame(total_frame, background="light yellow")
frame1.pack()
default_text = """
   Do you need any help?  
"""
label= Label(frame1, text=default_text, font= ('Helvetica 11 bold'), foreground= "black", background="light yellow", width=25, wraplength=200)
label.pack(padx=10)
entry = Entry(frame1)
entry.pack(pady=5)
button = Button(frame1, text="Enter", command=send_prompt, borderwidth=1, relief="ridge", background="light yellow")
button.pack(pady=5)

# assistant image
frameCnt = 2
frames = [PhotoImage(file='assets\\rocky.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    img_label.configure(image=frame, background="#add123")
    root.after(200, update, ind)

img_label = Label(total_frame)
img_label.pack()
root.after(50, update, 0)

# start tkinter
root.mainloop()


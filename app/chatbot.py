from tkinter import *
from main import entry

##sample chatbot UI in tkinter bc I don't wanna install more dependecies 

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 13"
FONT_BOLD = "Helvetica 12 bold"

# Send function
def send():

	
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user_question = e.get()
	results = entry(user_question)
	
	txt.insert(END, "\n" + f"Bot -> {results}")
	e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Chinook Chatbot :)", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
txt.insert(END, "Assistant -> Hello there!" 
        + "\n" + 
		"Please input your question based on chinook's Database here!" 
        + "\n" + 
        "For Example: Who are the top 5 most popular artists based on total albums?")

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

root.mainloop()

import tkinter as tk
import sqlite3

conn = sqlite3.Connection('data.db')
c = conn.cursor()


# execute the below line to create the table
# c.execute("""CREATE TABLE expenses (
# 	            name text,
# 	            date Date,
# 	            item text,
# 	            price integer )""")


c.close()
conn.close()


# this class contains method which makes a template for entry and returns entry to access the value entered
class CreateFrame:
	def FrameTemplate(self, yind, heading):
		frame = tk.Frame(root, bg='#80c1ff', bd=5)
		frame.place(relx=0.5, rely=yind, relwidth=0.75, relheight=0.1, anchor='n')

		entry = tk.Entry(frame, font=40)
		entry.place(relwidth=0.65, relheight=1)

		head = tk.Label(frame, text=heading, font=40)
		head.place(relx=0.7, relheight=1, relwidth=0.3)

		return entry


# this class contains method which makes a template frame for button and returns frame in ehich the button can be placed
class ButtonFrame:
	def ButtonTemplate(self, yind):
		frame = tk.Frame(root, bg='#80c1ff', bd=5)
		frame.place(relx=0.5, rely=yind, relwidth=0.5, relheight=0.1, anchor='n')

		return frame


# this method is called when the submit button is clicked
# it inserts the data in the database
def insertData(name, date, item, price):
	conn = sqlite3.Connection('data.db')
	c = conn.cursor()
	c.execute("INSERT INTO expenses VALUES (?, ?, ?, ?)", (name, date, item, price))
	c.close()
	conn.commit()
	conn.close()
	print("hello")
	

# this method is called when the get expenditure button is clicked
# it calculates the total expenditure till present
def getTotal():
	conn = sqlite3.Connection('data.db')
	c = conn.cursor()
	c.execute("SELECT SUM(price) FROM expenses")
	conn.commit()
	res = c.fetchall()
	c.close()
	print("hi")
	label = tk.Label(root, text=res[0][0])
	label.pack()


root = tk.Tk()

root.title("Expense - Tracker")

HEIGHT = 500
WIDTH = 600

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


nameFrame = CreateFrame()
n = nameFrame.FrameTemplate(0.1, "Name")

dateFrame = CreateFrame()
d = dateFrame.FrameTemplate(0.25, "Date")

itemFrame = CreateFrame()
i = itemFrame.FrameTemplate(0.4, "Item")

priceFrame = CreateFrame()
p = priceFrame.FrameTemplate(0.55, "Price")

# creating frame for submit button
submit = ButtonFrame()
sframe = submit.ButtonTemplate(0.7)


submit = tk.Button(sframe, text="SUBMIT", height=1, command=lambda :insertData(n.get(), d.get(), i.get(),
                                                                            p.get()))
submit.place(relx=0, relheight=1, relwidth=1)



# creating frame for get expenditure button
get = ButtonFrame()
gframe = get.ButtonTemplate(0.85)

get = tk.Button(gframe, text="Get Expenditure", height=1, command=lambda :getTotal())
get.place(relx=0, relheight=1, relwidth=1)

root.mainloop()
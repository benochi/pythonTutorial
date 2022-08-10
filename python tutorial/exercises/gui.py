import tkinter as tk
import tkinter.ttk as ttk

#create an instance of Tk class
window = tk.Tk()

#height and width are measure in text units, 1 horizontal TU = the width of the character 0, height is 1 tu char 0 height
headline = tk.Label(
  text = "This is our sweet GUI. I am a TKinter Label with lots of text to test my layout inside of this box.",
  foreground="#f4f3f7",
  background="#212431",
  width=70,
  height=10
  )
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="#45bac4",
    fg="#212431",
)
nameEntry = tk.Label(
  text = "Enter your name",
  foreground="#f4f3f7",
  background="#212431",
  )
entry = tk.Entry(fg="yellow", bg="blue", width=50)
nameEntry.pack()
entry.pack()
headline.pack()
button.pack()
#colors: red, orange, yellow, green, blue, purple, white, black.  Hexadecimal colors also work.
#blue green theme = #f4f3f7 #f25464 #4fcec2 #45bac4 #212431


#window.update()

"""
Label	  A widget used to display text on the screen
Button	A button that can contain text and can perform an action when clicked
Entry	  A text entry widget that allows only a single line of text
Text	  A text entry widget that allows multiline text entry
Frame	  A rectangular region used to group related widgets or provide padding between widgets
"""
name = entry.get()
print(name)




#when running from a python file an application wont run without this at the end.
window.mainloop()
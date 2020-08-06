from tkinter import *
import api

def getSelectedBook(event):
    try:
        global selectedBook 
        index = listBox.curselection()[0]
        selectedBook = listBox.get(index)
        titleEntry.delete(0,END)
        titleEntry.insert(END, selectedBook[1])
        authorEntry.delete(0,END)
        authorEntry.insert(END, selectedBook[2])
        yearEntry.delete(0,END)
        yearEntry.insert(END, selectedBook[3])
        isbnEntry.delete(0,END)
        isbnEntry.insert(END, selectedBook[4])
    except IndexError:
        pass    
def viewBooks():
    listBox.delete(0, END)
    for row in api.viewBooks():
        listBox.insert(END, row)

def searchBook():
    listBox.delete(0, END)
    for row in api.searchBook(titleText.get(), authorText.get(), yearText.get(), isbnText.get()):
        listBox.insert(END, row)

def addEntry():
    api.insertBook(titleText.get(), authorText.get(), yearText.get(), isbnText.get())
    viewBooks()

def deleteBook():
    api.deleteBook(selectedBook[0])
    viewBooks()

def updateBook():
     api.update(selectedBook[0], titleText.get(), authorText.get(), yearText.get(), isbnText.get())
     viewBooks() 

def closeApp():
    window.destroy()
window = Tk()
window.wm_title("Book Store")
titleLabel = Label(window, text = "Title")
titleLabel.grid(row = 0, column = 0)
authorLabel = Label(window, text = "Author")
authorLabel.grid(row = 0, column = 2)
yearLabel = Label(window, text = "Year")
yearLabel.grid(row = 1, column = 0)
isbnLabel = Label(window, text = "ISBN") 
isbnLabel.grid(row = 1, column = 2)

titleText = StringVar()
titleEntry = Entry(window, textvariable = titleText)
titleEntry.grid(row = 0, column = 1)
authorText = StringVar()
authorEntry = Entry(window, textvariable = authorText)
authorEntry.grid(row = 0, column = 3)
yearText = StringVar()
yearEntry = Entry(window, textvariable = yearText)
yearEntry.grid(row = 1, column = 1)
isbnText = StringVar()
isbnEntry = Entry(window, textvariable = isbnText)
isbnEntry.grid(row = 1, column = 3)

listBox = Listbox(window, height=6, width = 35)
listBox.grid(row = 2, column = 0, rowspan = 6, columnspan = 2)
listBox.bind('<<ListboxSelect>>', getSelectedBook)
listScrollBar = Scrollbar(window)
listScrollBar.grid(row = 2, column = 2, rowspan = 6)
listBox.configure(yscrollcommand = listScrollBar.set)

listScrollBar.configure(command = listBox.yview)

viewAllButton = Button(window, text = "View All", width = 12, command = viewBooks)
viewAllButton.grid(row = 2, column = 3)
searchEntryButton = Button(window, text = "Search Entry", width = 12, command = searchBook)
searchEntryButton.grid(row = 3, column = 3)
addEntryButton = Button(window, text = "Add Entry", width = 12, command = addEntry)
addEntryButton.grid(row = 4, column = 3)
updateButton = Button(window, text = "Update Selected", width = 12, command = updateBook)
updateButton.grid(row = 5, column = 3)
deleteButton = Button(window, text = "Delete Selected", width = 12, command = deleteBook)
deleteButton.grid(row = 6, column = 3)
closeButton = Button(window, text = "Close", width = 12, command = closeApp)
closeButton.grid(row = 7, column = 3)

window.mainloop()


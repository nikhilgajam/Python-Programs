import pyperclip as pc

x = input("Enter something to copy to the clipboard: ")
pc.copy(x)
print(pc.paste(), "Copied")

from tkinter import *


# Very simple encryption program.
def shift(shift_input, shift_key):
    temp = ''
    temp_key = key_format(shift_input, shift_key.upper())
    for x, y in zip(shift_input, temp_key):
        if x == " ":  # if space in input, return space.
            temp += " "
        elif ord(x) + (ord(y) - 64) <= ord("~"):
            temp += chr(ord(x) + (ord(y) - 64))
        else:
            temp += chr(ord(x) + ord(y) - 64 - ord("~") + ord(" "))  # ASCII bounds check, loops around when exceeding limits.
    return temp


def key_format(key_format_input, key_format_key):
    if len(key_format_input) > len(key_format_key):
        key_temp = key_format_key
        counter = 0
        for i in range(len(key_format_input) - len(key_format_key)):
            key_temp += key_format_key[counter]
            counter += 1
            if counter >= len(key_format_key):
                counter = 0
        return key_temp

    if len(key_format_input) < len(key_format_key):
        key_temp = key_format_key[:len(key_format_key) - (len(key_format_key) - len(key_format_input))]
        return key_temp
    if len(key_format_input) == len(key_format_key):
        return key_format_key


def reverse_shift(rshift_input, rshift_key):
    temp = ''
    temp_key = key_format(rshift_input, rshift_key.upper())
    for x, y in zip(rshift_input, temp_key):
        if x == " ":  # if 'space' in input, return space.
            temp += " "
        elif ord(x) - (ord(y) - 64) >= ord("!"):
            temp += chr(ord(x) - (ord(y) - 64))
        else:
            temp += chr(ord(x) - (ord(y) - 64) + (ord("~") - ord(
                " ")))  # if it goes out of ASCII boundaries, let it loop back around from beginning.
    return temp


# GUI
root = Tk()
root.title("Ez Encrypt")

keyEntry = Entry(root, width=50, borderwidth=5)
messageEntry = Entry(root, width=50, borderwidth=5)

enc_graphic_output = StringVar()
enc_graphic_output.set("")
encrypt_message_out = Entry(root, textvariable=enc_graphic_output, fg="black", bg="white", bd=0, width=100, state="readonly")
encrypt_message_out.pack()


def encrypted_graphic_output():
    enc_graphic_output.set("Output: " + str(shift(messageEntry.get(), keyEntry.get())))
    encrypt_message_out = Entry(root, width=50, textvariable=enc_graphic_output, fg="white", bg="white", bd=0)
    with open("Output.txt", "w") as text_file:
        print("Encrypted Message: {0}".format(shift(messageEntry.get(), keyEntry.get())), file=text_file)


dec_graphic_output = StringVar()
dec_graphic_output.set("")
decMessageOutput = Entry(root, textvariable=dec_graphic_output, fg="black", bg="white", bd=0, state="readonly")


def dec_graphic_output():
    enc_graphic_output.set("Output: " + str(reverse_shift(messageEntry.get(), keyEntry.get())))
    encrypt_message_out = Entry(root, textvariable=dec_graphic_output, fg="black", bg="white", bd=0, width=50)
    with open("Output.txt", "w") as text_file:
        print("Decrypted Message: {0}".format(shift(messageEntry.get(), keyEntry.get())), file=text_file)


eButton = Button(root, text="Encrypt", width=25, command=encrypted_graphic_output)
dButton = Button(root, text="Decrypt", width=25, command=dec_graphic_output)

mainWindow = Label(root, text="Key (can only english letters and is NOT case sensitive):")
mainWindow2 = Label(root, text="Message:")
mainWindow.pack()
keyEntry.pack()
mainWindow2.pack()
messageEntry.pack()
eButton.pack()
dButton.pack()

# MAIN
root.mainloop()

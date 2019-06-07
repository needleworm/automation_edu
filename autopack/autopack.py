import win32api, win32con, win32gui

keymap = {
    "backspace" : 0x08,
    "tab" : 0x09,
    "enter" : 0x0D,
    "shift" : 0x10,
    "control" : 0x11,
    "alt" : 0x12,
    "caps_lock" : 0x14,
    "kor_eng" : 0x15,
    "esc" : 0x1B,
    "spacebar" : 0x20,
    "page_up" : 0x21,
    "page_down" : 0x22,
    "end" : 0x23,
    "home" : 0x24,
    "left_arrow" : 0x25,
    "up_arrow" : 0x26,
    "right_arrow" : 0x27,
    "down_arrow" : 0x28,
    "print_screen" : 0x2C,
    "insert" : 0x2D,
    "delete" : 0x2E,
    "0" : 0x30,
    "1" : 0x31,
    "2" : 0x32,
    "3" : 0x33,
    "4" : 0x34,
    "5" : 0x35,
    "6" : 0x36,
    "7" : 0x37,
    "8" : 0x38,
    "9" : 0x39,
    "a" : 0x41,
    "b" : 0x42,
    "c" : 0x43,
    "d" : 0x44,
    "e" : 0x45,
    "f" : 0x46,
    "g" : 0x47,
    "h" : 0x48,
    "i" : 0x49,
    "j" : 0x4A,
    "k" : 0x4B,
    "l" : 0x4C,
    "m" : 0x4D,
    "n" : 0x4E,
    "o" : 0x4F,
    "p" : 0x50,
    "q" : 0x51,
    "r" : 0x52,
    "s" : 0x53,
    "t" : 0x54,
    "u" : 0x55,
    "v" : 0x56,
    "w" : 0x57,
    "x" : 0x58,
    "y" : 0x59,
    "z" : 0x5A,
    "left_window" : 0x5B,
    "right_window" : 0x5C,
    "numpad_0" : 0x60,
    "numpad_1" : 0x61,
    "numpad_2" : 0x62,
    "numpad_3" : 0x63,
    "numpad_4" : 0x64,
    "numpad_5" : 0x65,
    "numpad_6" : 0x66,
    "numpad_7" : 0x67,
    "numpad_8" : 0x68,
    "numpad_9" : 0x69,
    "numpad_+" : 0x6B,
    "numpad_-" : 0x6D,
    "numpad_." : 0x6E,
    "/" : 0x6F,
    "f1" : 0x70,
    "f2" : 0x71,
    "f3" : 0x72,
    "f4" : 0x73,
    "f5" : 0x74,
    "f6" : 0x75,
    "f7" : 0x76,
    "f8" : 0x77,
    "f9" : 0x78,
    "f10" : 0x79,
    "f11" : 0x7A,
    "f12" : 0x7B,
    "num_lock" : 0x90,
    "scroll_lock" : 0x91,
    "left_shift" : 0xA0,
    "right_shhift" : 0xA1,
    "left_control" : 0xA2,
    "right_control" : 0xA3,
    "browser_back" : 0xA6,
    "browser_forward" : 0xA7,
    "browser_refresh" : 0xA8,
    "browser_stop" : 0xA9,
    "browser_search" : 0xAA,
    "browser_favorites" : 0xAB,
    "volume_mute" : 0xAD,
    "volume_down" : 0xAE,
    "volume_up" : 0xAF,
    ";" : 0xBA,
    "=" : 0xBB,
    "," : 0xBC,
    "-" : 0xBD,
    "." : 0xBE,
    "/" : 0xBF,
    "`" : 0xC0,
    "[" : 0xDB,
    "\\" : 0xDC,
    "]" : 0xDD,
    "'" : 0xDE,
}

# mouse control
def move_mouse(location):
    x, y = location
    win32api.SetCursorPos(location)
    return x, y


def click(location):
    x, y = move_mouse(location)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def drag_drop(frm, to):
    x1, y1 = move_mouse(frm)
    x2, y2 = to
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x2-x1, y2-y1, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# keyboard control
def type_in(string):
    command = 'echo ' + string.strip() + '| clip'
    os.system(command)
    win32api.keybd_event(0x11, 0, 0x00, 0)
    win32api.keybd_event(0x56, 0, 0x00, 0)
    win32api.keybd_event(0x11, 0, 0x02, 0)
    win32api.keybd_event(0x56, 0, 0x02, 0)


def key_press_once(string):
    global keymap
    key_code = keymap[string.lower()]
    win32api.keybd_event(key_code, 0, 0x00, 0)
    win32api.keybd_event(key_code, 0, 0x02, 0)


def key_press_on(string):
    global keymap
    key_code = keymap[string.lower()]
    win32api.keybd_event(key_code, 0, 0x00, 0)


def key_off(string):
    global keymap
    key_code = keymap[string.lower()]
    win32api.keybd_event(key_code, 0, 0x02, 0)

# window control
def get_color(location):
    x, y = location
    return hex(win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y))

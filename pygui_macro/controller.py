from pynput import keyboard, mouse


class Controller:
    original = (0, 0)
    keyboard_controller = keyboard.Controller()
    mouse_controller = mouse.Controller()

    @classmethod
    def mouse_move(cls, x, y):
        _x, _y = cls.original
        cls.mouse_controller.position = (int(_x + float(x)), int(_y + float(y)))

    @classmethod
    def mouse_click(cls, button, count=1):
        cls.mouse_controller.click(mouse.Button.__dict__[button], count)

    @classmethod
    def mouse_press(cls, button, is_auto_release=False):
        cls.mouse_controller.press(mouse.Button.__dict__[button])
        if is_auto_release:
            cls.mouse_controller.release(mouse.Button.__dict__[button])

    @classmethod
    def mouse_release(cls, button):
        cls.mouse_controller.release(mouse.Button.__dict__[button])

    @classmethod
    def mouse_scroll(cls, x, y, dx, dy):
        cls.mouse_controller.scroll(int(dx), int(dy))

    @classmethod
    def key_press(cls, key, is_auto_release=False):
        if key in keyboard.Key.__dict__:
            cls.keyboard_controller.press(keyboard.Key[key])
        else:
            cls.keyboard_controller.press(key)

        if is_auto_release:
            cls.keyboard_controller.release()

    @classmethod
    def key_release(cls, key):
        if key in keyboard.Key.__dict__:
            cls.keyboard_controller.release(keyboard.Key[key])
        else:
            cls.keyboard_controller.release(key)

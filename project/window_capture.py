import win32gui, win32ui, win32con
import numpy as np

class WindowCapture:
    """
    https://learncodebygaming.com/blog/fast-window-capture
    """
    width = 0
    height = 0
    height_window = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    def __init__(self, window_name):  # sourcery skip: raise-specific-error
        self.height_window = win32gui.FindWindow(None, window_name)
        if not self.height_window:
            raise Exception(f'Window not found: {window_name}')

        window_rect = win32gui.GetWindowRect(self.height_window)
        self.width = window_rect[2] - window_rect[0]
        self.height = window_rect[3] - window_rect[1]

        border_pixels = 8
        titlebar_pixels = 30
        self.width = self.width - (border_pixels * 2)
        self.height = self.height - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):
        wDC = win32gui.GetWindowDC(self.height_window)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.width, self.height)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.width, self.height), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.height, self.width, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.height_window, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]
        img = np.ascontiguousarray(img)

        return img

    def list_window_names(self):
        def winEnumHandler(height_window, ctx):
            if win32gui.IsWindowVisible(height_window):
                print(hex(height_window), win32gui.GetWindowText(height_window))
        win32gui.EnumWindows(winEnumHandler, None)

    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)

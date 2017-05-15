#coding:utf-8
import win32gui
from PIL import ImageGrab
import win32con
#from Utility.Colors import DEFAULT, RED

hwnd = win32gui.FindWindow("Edit", "")
if not hwnd:
    print( 'window not found!')
else:
    print(hwnd)

win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 强行显示界面后才好截图
win32gui.SetForegroundWindow(hwnd)  # 将窗口提到最前
#  裁剪得到全图
game_rect = win32gui.GetWindowRect(hwnd)
src_image = ImageGrab.grab(game_rect)
# src_image = ImageGrab.grab((game_rect[0] + 9, game_rect[1] + 190, game_rect[2] - 9, game_rect[1] + 190 + 450))
src_image.show()
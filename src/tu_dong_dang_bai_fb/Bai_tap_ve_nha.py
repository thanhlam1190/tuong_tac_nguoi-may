import pyautogui
import time

# Tìm chorme icon
coors = pyautogui.locateOnScreen('img\\chorme_icon.png', grayscale=True,confidence=0.7 )
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x), (coors_center.y))

# Gõ facebook
pyautogui.hotkey('alt', 'd')
pyautogui.write("facebook.com")
pyautogui.press('enter')
time.sleep(3)

# Chọn thanh gõ
coors = pyautogui.locateOnScreen('img\\box.png', grayscale=True,confidence=0.7 )
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x), (coors_center.y))
time.sleep(2    )       
pyautogui.write('mat khau wifi!', interval=0)

# Nhấn vào nút đăng
coors = pyautogui.locateOnScreen('img\\post.png', grayscale=True,confidence=0.7 )
coors_center = pyautogui.center(coors)
pyautogui.click((coors_center.x), (coors_center.y))
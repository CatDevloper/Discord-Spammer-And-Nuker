import pyautogui, time
print("o-----------------------------------------------------------------------------------------------------------------o")
print("      $$$$$$\                                                                                        $$\   ")
print("     $$  __$$\                                                                                     $$$$ |  ")
print("     $$ /  \__| $$$$$$\   $$$$$$\  $$$$$$\$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\        $$\    $$\\_$$ |  ")
print("     \$$$$$$\  $$  __$$\  \____$$\ $$  _$$  _$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\       \$$\  $$  | $$ |  ")
print("      \____$$\ $$ /  $$ | $$$$$$$ |$$ / $$ / $$ |$$ / $$ / $$ |$$$$$$$$ |$$ |  \__|       \$$\$$  /  $$ |  ")
print("     $$\   $$ |$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$ | $$ | $$ |$$   ____|$$ |              \$$$  /   $$ |  ")
print("     \$$$$$$  |$$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$$\ $$ |               \$  /  $$$$$$\ ")
print("      \______/ $$  ____/  \_______|\__| \__| \__|\__| \__| \__| \_______|\__|                \_/   \______|")
print("               $$ |                                                                                        ")
print("               $$ |                                                                                        ")
print("               \__|                                                                                        ")
print("                                                                                                           ")
print("                                                                                                           ")
print("                 The cookies army is waiting!                                             By UltraWolf#0001")
print("o----------------------------------------------------------------------------------------------------------------o")
message = input("Messaage: ")
duration = input("Duration Set 0 for a best result: ")
repeats = input("Repeats: ")
print(" (??????????? ?????) The army is ready! Wait")

time.sleep(5)

for i in range(int(repeats)):
    pyautogui.write(message)
    pyautogui.press("enter")
    time.sleep(int(duration))

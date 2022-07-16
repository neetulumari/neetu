# drinling water notification
import time
from plyer import notification
# Plyer is a platform independent module in python, that helps us to access features of our hardware / platforms
# Time: There is a popular time module available in Python which provides many ways of representing time in code, such as objects, numbers, and strings.

if __name__ == "__main__":
    while True:
        notification.notify(title = "Reminder: please Drink Water Now",
                    message = "To prevent dehydration , health authorities commonly recomended 8 glasses water ,which equals to 2 litre.",
                    app_name = "Water reminder" ,
                    timeout = 10)
        time.sleep(60*60)
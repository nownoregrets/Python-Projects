import time
from plyer import notification

while True:

    if __name__ == "__main__":

        notification.notify(
            title="Water Reminder",
            message="Getting enough water every day is important for your health. Drinking water can prevent dehydration, a condition that can cause unclear thinking, result in mood change, cause your body to overheat, and lead to constipation and kidney stones.",
            app_icon="Water Glass.ico",
            timeout=15
        )
        time.sleep(60*60)

# https://plyer.readthedocs.io/en/latest/index.html?highlight=notification#plyer.facades.Notification
# https://pypi.org/project/plyer/

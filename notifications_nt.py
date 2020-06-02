from plyer import notification

def send_notif(title, msg, /, app_name="Python", duration=5, icon=None):
  "send a notification toast"
  notification.notify(title=title, message=msg, app_name=app_name, timeout=duration, app_icon=icon)

if __name__ == "__main__":
  send_notif("test custom_module", "Check successful!", app_name="custom_module", duration=3)

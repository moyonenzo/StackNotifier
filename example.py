from StackNotification import Notifier,RoundedNotifier
import time

notifier = Notifier("BOTTOM")
rounded_notifier = RoundedNotifier("TOP")

for i in range(4):
    notifier.SendNotification("TITLE %s" % i, "DESCRIPTION") # disappear after 10 seconds
    rounded_notifier.SendNotification("TITLE %s" % i, "DESCRIPTION") # disappear after 10 seconds
    time.sleep(.5)
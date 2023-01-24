# StackNotifier

### USAGE ( `WINDOWS 10/11 ONLY` )

> 1. IMPORTATION
```
from StackNotification import Notifier,RoundedNotifier
```

> 2. INITIALISATION ( You can use `Notifier` or `RoundedNotifier` as you want with parameter `BOTTOM` or `TOP` )

```
notifier = Notifier("BOTTOM") 
rounded_notifier = RoundedNotifier("TOP")
```

> 3. Notification Sending ( disapear after 10 seconds )

```
notifier.SendNotification("TITLE", "DESCRIPTION")
rounded_notifier.SendNotification("TITLE", "DESCRIPTION")

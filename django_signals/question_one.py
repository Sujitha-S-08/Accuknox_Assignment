import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler started at {timezone.now()}")
    time.sleep(5)  # Simulate a delay
    print(f"Signal handler ended at {timezone.now()}")
def create_user():
    print(f"Main function started at {timezone.now()}")
    user = User.objects.create(username="test_user")
    print(f"Main function ended at {timezone.now()}")
create_user()

# By default, Django signals are executed synchronously. 
# When a signal is sent, any connected signal handlers are triggered immediately,
# and the main execution flow waits for all handlers to complete before continuing. 
# This synchronous behavior can be demonstrated by timing the execution of a signal 
# handler and observing that the main thread waits for the handler's completion before 
# moving forward.

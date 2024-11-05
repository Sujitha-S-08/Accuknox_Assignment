import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")
def create_user():
    print(f"Caller thread ID: {threading.get_ident()}")
    user = User.objects.create(username="test_user")
create_user()

# Yes, by default, Django signals run in the same thread as the caller. 
# When a signal is triggered, its connected signal handlers execute in the same thread 
# as the code that sent the signal. We can prove this by printing the thread ID 
# of both the calling function and the signal handler, and confirming they match.

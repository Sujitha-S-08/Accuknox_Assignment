from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import connection

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler running...")
    instance.username = "modified_in_signal"
    instance.save()
def create_user():
    with transaction.atomic():
        user = User.objects.create(username="original_user")
        print("User created within transaction")
        raise Exception("Rolling back transaction")
try:
    create_user()
except Exception as e:
    print("Transaction rolled back due to exception:", e)
print("Checking if user exists with the modified username...")
user_exists = User.objects.filter(username="modified_in_signal").exists()
print(f"User with modified username exists: {user_exists}")

# Yes, by default, Django signals run in the same database transaction as the caller. 
# When a signal is triggered (such as post_save), it executes within the same database 
# transaction as the operation that triggered it. 
# This behavior can be demonstrated by using a post_save signal and 
# rolling back the transaction to see if changes made in the signal handler 
# are also rolled back.
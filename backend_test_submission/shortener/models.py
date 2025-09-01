from django.db import models
from django.utils import timezone
from datetime import timedelta
import string, random

def generate_shortcode(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

class ShortURL(models.Model):
    url = models.URLField()
    shortcode = models.CharField(max_length=10, unique=True, blank=True)
    expiry = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.shortcode:  # auto generate if not given
            self.shortcode = generate_shortcode()
        super().save(*args, **kwargs)

import os
from django.db import models
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402


if __name__ == '__main__':
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'

    total_cards = Passcard.objects.count()
    active_passcards = Passcard.objects.filter(is_active=True).count()
    print('Всего пропусков:', total_cards)
    print('Активных пропусков:', active_passcards)

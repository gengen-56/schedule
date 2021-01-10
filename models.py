from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class Schedule(models.Model):
    summary = models.CharField(("概要"), max_length=50)
    description = models.TextField(("詳細な説明", blank=True, null=True))
    start_time = models.TimeField(("開始時間"), default=datetime.time(7, 0, 0))
    end_time = models.TimeField(("終了時間"), default=datetime.time(7, 0, 0))
    date = models.DateField(("日付"), default=timezone.now)
    created_at = models.DateField(("作成日"), default=timezone.now)

    def __str__(self):
        return self.summary

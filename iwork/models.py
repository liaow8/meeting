# coding=utf8
from django.db import models

# Create your models here.


class WorkRecord(models.Model):
    theme = models.CharField(u"会议主题", max_length=64)
    content = models.TextField(u"会议内容", null=True, blank=True)
    record_time = models.DateTimeField(u"会议时间", auto_now_add=True)
    operator = models.CharField(u"记录人", max_length=20)

    def __unicode__(self):
        return self.theme

    class Meta:
        ordering = ['-id']
        verbose_name = u"会议记录"
        verbose_name_plural = u"会议记录"

from django.db import models
from django.utils.timezone import now


class BasePaper(models.Model):
    title = models.CharField("标题", max_length=512, null=False)
    sub_title = models.CharField("副标题", max_length=512, null=True, default="")
    author = models.CharField("作者", max_length=256)
    keywords = models.CharField("关键词", max_length=512)
    filepath = models.CharField("文件路径", max_length=512)

    create_time = models.DateTimeField("创建时间", default=now)
    update_time = models.DateTimeField("修改时间", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class JournalPaper(BasePaper):
    journal = models.CharField("期刊", max_length=512)
    volume = models.CharField("卷", max_length=32)
    pages = models.CharField("页", max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = '期刊文献'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
        db_table = 'paper_journal'


class ConferencePaper(BasePaper):
    conference = models.CharField("会议", max_length=512)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = '会议文献'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
        db_table = 'paper_conference'


class ThesisPaper(BasePaper):
    university = models.CharField("学校", max_length=128)
    degree = models.CharField("学位", max_length=32)
    mentor = models.CharField("导师", max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
        verbose_name = '学位文献'
        verbose_name_plural = verbose_name
        get_latest_by = 'id'
        db_table = 'paper_thesis'


class Publication(models.Model):
    # TODO 期刊会议等
    ...

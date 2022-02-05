from django.db import models

# Create your models here.
class myusers(models.Model):
    # 用户名
    username = models.CharField('用户名', blank=False, max_length=15, unique=True)
    # 密码
    password = models.CharField('密码', max_length=15, blank=False, unique=True)
    # 创建时间，只有在新增的时候生效
    createTime = models.DateTimeField(auto_now_add=True)
    # 修改时间，添加和修改都会改变时间
    modifyTime = models.DateTimeField(auto_now=True)
    # 模拟删除
    is_active =models.BooleanField(default=False)

    class Meta:
        db_table = 'myusers'
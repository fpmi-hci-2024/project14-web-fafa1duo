from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=200)  # 待办事项的标题
    completed = models.BooleanField(default=False)  # 标记待办事项是否完成
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间，自动添加

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # 按创建时间倒序排列


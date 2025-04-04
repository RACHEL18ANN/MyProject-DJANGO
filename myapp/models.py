from django.db import models  

class Post(models.Model):  
    title = models.CharField(max_length=200)  
    content = models.TextField()  

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, blank=True, null=True)
    deadline = models.DateField(max_length=10, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

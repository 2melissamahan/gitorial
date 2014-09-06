from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True)
    avatar_url = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    repo_url = models.CharField(max_length=100)
    owner = models.ForeignKey(User)
    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=100)
    content_before = models.CharField(max_length=500)
    content_after = models.CharField(max_length=500)
    tutorial = models.ForeignKey(Tutorial)
    def __str__(self):
        return self.title

class Commit(models.Model):
    commit_url = models.CharField(max_length=100)
    code_url = models.CharField(max_length=100)
    step = models.OneToOneField(Step)
    def __str__(self):
        return commit_url

class File(models.Model):
    commit = models.ForeignKey(Commit)
    name = models.CharField(max_length=100)
    def __str__(self):
        return name

class Line(models.Model):
    src_file = models.ForeignKey(File)
    number = models.IntegerField()
    content = models.CharField(max_length=200)
    addition = models.BooleanField()
    deletion = models.BooleanField()
    def __str__(self):
        return content

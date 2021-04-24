from django.db import models


class Dag(models.Model):
    name = models.CharField(max_length=12)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Tweet(models.Model):
    text = models.CharField(max_length=256)
    photo = models.URLField(max_length=256, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'[{self.author.username}] {self.text}'


class Follow(models.Model):
    #User(username=Саша, follows[Саша->Миша], followers[])
    follower = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='follows')
    #User(username=Миша, folows[], followers[Саша->Миша])
    follows = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='followers')
    followed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower.username} -> {self.follows.username}'

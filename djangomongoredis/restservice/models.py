from djongo import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    producer=models.CharField(max_length=100,null=True)
    entertainment=models.CharField(max_length=100,null=True)
    tracknum=models.IntegerField()
    def __str__(self):
        return self.title
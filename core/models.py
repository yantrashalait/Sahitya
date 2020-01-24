from django.db import models


class AudioBook(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=225)
    publication = models.CharField(max_length=225)
    audio_file = models.FileField(upload_to="audios/")
    added_date = models.DateTimeField(auto_now=True)
    price = models.CharField(max_length=100, help_text="In rupees")
    image = models.ImageField(upload_to="audios/image", null=True, blank=True)

    def __str__(self):
        return self.author

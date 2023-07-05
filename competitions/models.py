from django.db import models

# Create your models here.
class Competition(models.Model):
    # Default behaviour - Django creates primary keys for you title = models.CharField(max_length=140)
    title = models.TextField()
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self): 
        return self.title

class Entry(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE) 
    member_id = models.CharField(max_length=8)
    email = models.EmailField()
    entry_date_time = models.DateTimeField(default="1900-01-01 00:00:00")

    def get_entry_date_time(self):
        return self.entry_date_time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"{self.get_entry_date_time()}\t{self.member_id}\t{self.competition.__str__()}"
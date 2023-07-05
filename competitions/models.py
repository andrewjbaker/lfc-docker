from django.db import models

# Create your models here.
class Competition(models.Model):
    """Competition class for the competitions section of the website
    
    :param models.Model: `Model` class used by django db
    :type models.Model: `Model`
    :param title: The title of the competition
    :type title: `str`
    :param body: The body of text describing the competition
    :type body: `str`
    :param date: The date on which the competition was launched
    :type date: `datetime`
    """

    # Default behaviour - Django creates primary keys for you title = models.CharField(max_length=140)
    title = models.TextField()
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self): 
        """Returns a string representation of the Competition class
        :param self: 
        :type self: `Competition`
        :return: The title of the competition
        :rtype: `str`
        """
        return self.title

class Entry(models.Model):
    """Competition class for the competitions section of the website
    
    :param models.Model: `Model` class used by django db
    :type models.Model: `Model`
    :param competition: The foreign key which links the `Entry` to a given `Competition` whose primary key is its title
    :type competition: `str`
    :param email: The email address of the entrant
    :type email: `str`
    :param entry_date_time: The date and time the entry was submitted, defaults to 01/01/1900 00:00:00
    :type entry_date_time: `datetime`
    """

    competition = models.ForeignKey(Competition, on_delete=models.CASCADE) 
    member_id = models.CharField(max_length=8)
    email = models.EmailField()
    entry_date_time = models.DateTimeField(default="1900-01-01 00:00:00")

    def get_entry_date_time(self):
        """Returns a string representation of the date and time of the entry
        :param self: 
        :type self: `Entry`
        :return: The date and time of the entry in the format YYYY-MM-DD hh:mm:ss
        :rtype: `str`
        """
        return self.entry_date_time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        """Returns a string representation of the Entry class
        :param self: 
        :type self: `Entry`
        :return: A string containing the date and time of the entry, the member id and the competition title
        :rtype: `str`
        """
        return f"{self.get_entry_date_time()}\t{self.member_id}\t{self.competition.__str__()}"
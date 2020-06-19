from django.db import models

# Create your models here.

class Sport(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('id', 'name')
    
class Market(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, related_name='markets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '|' + self.sport.name
    
    class Meta:
        ordering = ('id', 'name', 'sport')

class Selection(models.Model):
    name = models.CharField(max_length=100)
    odds = models.FloatField()
    market = models.ForeignKey(Market, related_name='selections', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id', 'name', 'odds','market')

class MatchManager(models.Manager):
    """Custom Manager for Match model
    with two additional methods to
    count active and inactive matches.
    And override get_queryset method
    """
    def get_queryset(self):
        return super().get_queryset()
    
    def count_active(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM demo_app_match
                WHERE status = 1
                """)
            for row in cursor.fetchall():
                count = row[0]
        return count
    
    def count_inactive(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT COUNT(*)
                FROM demo_app_match
                WHERE status = 0
                """)
            for row in cursor.fetchall():
                count = row[0]
        return count

class Match(models.Model):
    name = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    sport = models.ForeignKey(Sport, related_name='matches', on_delete=models.CASCADE)
    market = models.ForeignKey(Market, related_name='matches', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    objects = MatchManager() 

    class Meta:
        ordering = ('id', 'name','startTime', 'sport', 'market')
        verbose_name_plural = 'Matches'

    def __str__(self):
        return self.name
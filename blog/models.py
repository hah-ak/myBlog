from django.db import models
from django.urls import reverse
from django.utils import timezone

class Algorithm(models.Model):
        sites = (
                ('SSEA','SSEA'),
                ('programmers','programmers')
        )
        site = models.CharField(max_length= 20, choices = sites)
        title = models.CharField(max_length=200)
        problem_content = models.TextField()
        coding_content = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        

        def get_absolute_url(self):
                return reverse('codes-detail', kwargs={'sort': self.site ,'pk': self.pk})

        def publish(self):
                self.published_date = timezone.now()
                self.save()

        def __str__(self):
                return self.title


# class Site_sort(models.Model):
#         site_name = models.CharField(primary_key = True, max_length = 20)

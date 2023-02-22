from django.db import models

    
# Create your models here.
class RemoteSite(models.Model):
    BranchId = models.AutoField(primary_key=True)
    BranchName = models.CharField(max_length=200)
    BranchCode = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    lastFiveSecCpu = models.IntegerField()
    lastOneMinCpu = models.IntegerField()
    lastFiveMinCpu = models.IntegerField()
    primaryPower = models.CharField(max_length=200)
    secondaryPower = models.CharField(max_length=200)
    fan = models.CharField(max_length=200)
    temp = models.FloatField(max_length=200)
    interface_Brief = models.TextField(default="")
    loggs = models.TextField(default="")
    time = models.DateTimeField(auto_now_add=True)


    
    def __str__(self):
        return self.BranchName +" - " + str(self.ip )
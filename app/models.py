from django.db import models

# Create your models here.
class Employe(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField()
    deptno=models.IntegerField()

    def __str__(self):
        return self.ename
from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.db import models

class WorkType(models.Model):
    name = models.CharField(max_length=100)
    cost_per_sqm = models.DecimalField(max_digits=10, decimal_places=2)
    time_per_sqm = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    type_of_work = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Проект для {self.client} - {self.type_of_work}"
    
class FeedBack(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=64)
    message = models.CharField(max_length=1024)

class SelectedWork(models.Model):
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.work_type.cost_per_sqm * self.area

    @property
    def total_time(self):
        return self.work_type.time_per_sqm * self.area

    def __str__(self):
        return f"{self.work_type.name} - {self.area} m²"
    
    
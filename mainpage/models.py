from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name='Имя клиента')
    last_name = models.CharField(max_length=32, verbose_name='Фамилия клиента')
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Work(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название вида работы')
    cost_per_sqm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость за кв.м')
    time_per_sqm = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Длительность на кв.м (часы)')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вид работы'
        verbose_name_plural = 'Виды работ'

class Project(models.Model):
    title = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects',  verbose_name='Клиент')
    name = models.CharField(max_length=255, verbose_name='Название проекта')
    start_date = models.DateField(verbose_name='Дата начала')
    finish_date = models.DateField(verbose_name='Дата завершения', null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=255, verbose_name='Статус проекта')
    address = models.CharField(max_length=512, verbose_name='Адрес объекта')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Общая стоимость')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def total_cost(self):
        result = self.project_works.aggregate(total=sum('work_cost'))
        return result['total'] if result['total'] else 0

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class ProjectWork(models.Model):
    project = models.ForeignKey(Project, related_name='project_works', on_delete=models.CASCADE)
    work = models.ForeignKey(Work, related_name='project_works', on_delete=models.CASCADE)
    volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Объем работ')
    multiplier = models.IntegerField(verbose_name='Множительный коэффициент')
    details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.work.name} в проекте {self.project.name}, объем {self.area} m²"

    @property
    def work_cost(self):
        return self.volume * self.work.cost_per_sqm * self.multiplier

    @property
    def work_duration(self):
        return self.volume * self.work.time_per_sqm

    class Meta:
        verbose_name = 'Работа в проекте'
        verbose_name_plural = 'Работы в проектах'

class FeedBack(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='feedbacks')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    feedback_text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)

    class Meta:
        unique_together = ('project', 'client')

    def __str__(self):
        return f"Feedback for Project '{self.project.title}' by Client '{self.client}'"
from django.db import models
# Create your models here.

class Medico(models.Model):
    ESPECIALIDADES_CHOICES = (
        ('Pediatra', 'pediatra'),
        ('Cardiologia', 'padiatra'),
        ('Cirurgia plástica', 'Cirurgia plástica'),
        ('Neurologia', 'Neurologia'),
        ('Radiologia','Radiologia'),
        ('Nenhuma das opções', 'Nenhuma das opções')
    )
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=200, choices=ESPECIALIDADES_CHOICES, blank=False, null=False)
    crm = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Medico"



class Consulta(models.Model):
    STATUS_CHOICES = (
        ('agendado', 'agendado'),
        ('realizado', 'realizado'),
        ('cancelado', 'cancelado')
    )
    paciente = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    Medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.paciente

    class Meta:
        verbose_name_plural = "Consulta"


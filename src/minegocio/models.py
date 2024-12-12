from django.db import models

# Create your models here.

class Vendedor(models.Model):
    nombre = models.CharField(max_length=13)
    dni = models.PositiveIntegerField(max_length=8, unique=True)

    def _str_(self):
        return f"{self.nombre}, {self.dni}"
    
class Producto(models.Model):  
    categorias = [("C","Celulares"),
                 ("AU","Auriculares"),
                 ("PE","Pequeños electrodomesticos"),
                 ("T","Tablets")]
    categoria = models.CharField(max_length=50,choices=categorias,default="PE")
    

class Transaccion(models.Model):
    dni = models.ForeignKey(Vendedor,on_delete=models.SET_NULL)
    fecha = models.DateField(null=True,blank=True)
    cantidad = models.PositiveIntegerField(max_length=5)
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)


class Reporte(models.Model):
    dni = models.ForeignKey(Vendedor,on_delete=models.SET_NULL,null=True)
    año = models.PositiveIntegerField()
    informe = models.CharField(max_length=25)
    categorias = models.ForeignKey(Producto, on_delete=models.CASCADE,null=True)
    periodos = [
        ('MENSUAL', 'Mensual'),
        ('TRIMESTRAL', 'Trimestral'),
        ('ANUAL', 'Anual'),
    ]
    periodo = models.CharField(max_length=10,choices=periodos,default='ANUAL')


    class Meta():
        constraints = [models.UniqueConstraint(fields=["año","categorias","periodo"], name="unico_informe_por_año")]
from django.db import models

# def normalizar_texto(texto: str) -> str:
#     """Transforma el texto a una forma normalizada NFD
#     (Normalization Form Decomposition).
#     Esto significa que los caracteres compuestos,
#     como las letras con tildes o diacríticos,
#     se descomponen en su forma base y sus marcas diacríticas separadas.
#     Ej: la letra "é" se descompone en "e" + un carácter de tilde combinable (U+0301).
#     Convierte la cadena en bytes usando la codificación ASCII.
#     Si un carácter no puede representarse en ASCII (por ejemplo, una "ñ" o una "é"),
#     se ignora debido al parámetro "ignore".
#     Luego, convierte los bytes resultantes nuevamente a una cadena de texto utilizando la codificación UTF-8."""
#     texto = unicodedata.normalize("NFD", texto)
#     texto = texto.encode("ascii", "ignore").decode("utf-8")
#     return texto"

# Create your models here.

class Vendedor(models.Model):
    nombre = models.CharField(max_length=13)
    dni = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return f"{self.nombre}, {self.dni}"
    

class Transaccion(models.Model):
    dni = models.ForeignKey(Vendedor,on_delete=models.CASCADE)
    fecha = models.DateField(null=True,blank=True)
    cantidad = models.PositiveIntegerField()
    monto = models.DecimalField(max_digits=10,decimal_places=2)
    productos = [
        ("C", "Celulares"),
        ("AU", "Auriculares"),
        ("PE", "Pequeños electrodomésticos"),
        ("T", "Tablets")]
    producto = models.CharField(max_length=50, choices=productos, default="PE")
    def __str__(self):
        return self.producto

class Reporte(models.Model):
    dni = models.ForeignKey(Vendedor,on_delete=models.CASCADE,null=True)
    año = models.PositiveIntegerField()
    informe = models.CharField(max_length=25)
    producto= models.ForeignKey(Transaccion, on_delete=models.CASCADE,null=True)
    periodos = [
        ('MENSUAL', 'Mensual'),
        ('TRIMESTRAL', 'Trimestral'),
        ('ANUAL', 'Anual'),
    ]
    periodo = models.CharField(max_length=10,choices=periodos,default='ANUAL')


    class Meta():
        constraints = [models.UniqueConstraint(fields=["año","producto","periodo"], name="unico_informe_por_año")]
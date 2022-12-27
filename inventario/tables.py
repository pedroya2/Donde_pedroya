import django_tables2 as tables
from .models import *

class TodosProductosTabla(tables.Table):
    id=tables.Column(verbose_name= 'ID') #lo que está a la izquierda del "igual" es el nombre del campo en el modelo, lo qeu esta después de "verbose name" es el nombre que se muestra, es como un alias (como el AS de SQL)
    codbar=tables.Column(verbose_name= 'Codigo Barra')
    descripcion=tables.Column(verbose_name= 'Nombre Producto')
    category_id_Categoria__nombrecatg=tables.Column(verbose_name= 'Categoria')
    precio=tables.Column(verbose_name= 'Precio Producto')
    disponible=tables.Column(verbose_name= 'Unidades Disponibles')
    class Meta:
        attrs = {'class': 'paleblue'}

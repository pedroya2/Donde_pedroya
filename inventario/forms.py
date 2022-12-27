from django import forms
from .models import Producto,Cliente, Proveedor, Usuario, Opciones,Categoria,Marca

from django.forms import ModelChoiceField

from django.forms.widgets import DateInput
from django.contrib.auth.forms import AuthenticationForm
from django.forms import CheckboxInput

# Test For SearchView
# from searchview.forms import SearchForm

class MisProductos(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.descripcion

class MisCategorias(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.nombrecatg

class MisMarcas(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.NombreMarca

class MisPrecios(ModelChoiceField):
    def label_from_instance(self,obj):
        return "%s" % obj.precio

class MisDisponibles(ModelChoiceField):
    def label_from_instance(self,obj):
        return "%s" % obj.disponible


class ProductoDescripcionFilterForm(forms.Form):
     descripcion =forms.CharField()

class SeleCategoriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['category'].queryset = Categoria.objects.all()
        self.fields['category'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Activo'].widget.attrs.update({'class': 'form-control'})
        self.fields['tiene_iva'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Producto
        fields = ['category','Activo','tiene_iva','Deposito','Nivel']


class SeleMarcaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['category'].queryset = Categoria.objects.all()
        self.fields['marca'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Activo'].widget.attrs.update({'class': 'form-control'})
        self.fields['tiene_iva'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Producto
        fields = ['marca','Activo','tiene_iva','Deposito','Nivel']

class LoginFormulario(forms.Form):
    username = forms.CharField(label="Tu nombre de usuario",widget=forms.TextInput(attrs={'placeholder': 'Tu nombre de usuario',
        'class': 'form-control underlined', 'type':'text','id':'user'}))

    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña',
        'class': 'form-control underlined', 'type':'password','id':'password'}))

class CategoriaFormulario(forms.ModelForm):


    class Meta:
        model = Categoria
        fields = ['nombrecatg','reference']
        labels = {
        'nombrecatg': 'Categoria Producto',
        'reference': 'Referencia ',
            }
        widgets = {
        'nombrecatg': forms.TextInput(attrs={'placeholder': 'Categoria Productos',
        'id':'nombrecatg','class':'form-control'} ),
        'reference': forms.TextInput(attrs={'placeholder': 'Referencia',
        'id':'reference','class':'form-control'} )
        }

class MarcaFormulario(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['NombreMarca']
        labels = {
        'NombreMarca': 'Marca Producto',
            }
        widgets = {
        'NombreMarca': forms.TextInput(attrs={'placeholder': 'Marca Productos',
        'id':'NombreMarca','class':'form-control'} )
        }

class ProductoFormulario(forms.ModelForm):

    precio = forms.DecimalField(
        min_value = 0,
        label = 'Precio',
        widget = forms.NumberInput(
        attrs={'placeholder': 'Precio del producto',
        'id':'precio','class':'form-control'}),
        )

    productos= Categoria.CatRegistradas()

    category= MisCategorias(queryset=productos,
    widget=forms.Select(attrs={'placeholder': 'Categoria del Producto','id':'Category_id',
    'class':'form-control'}))

    Marcas= Marca.MarkRegistradas()

    marca= MisMarcas(queryset=Marcas,
    widget=forms.Select(attrs={'placeholder': 'Marcas del Producto','id':'marca_id',
    'class':'form-control'}))

    class Meta:
        model = Producto
        fields = ['codbar','descripcion','descripcionAmp','disponible','precio','Deposito','MinUnidades','MaxUnidades','categoria','tiene_iva','Activo','category','marca']

        labels = {
        'category': 'Categoria del Producto',
        'marca': 'Marca del Producto',
        'descripcion': 'Nombre',
        'Activo': 'Esta Activo?',
        'tiene_iva': 'Incluye IVA?',
                # 'category': 'Categoria del Producto'
        }
        widgets = {
        'codbar': forms.TextInput(attrs={'placeholder': 'Codigo de Barra',
        'id':'codbar','class':'form-control'} ),
        'descripcion': forms.TextInput(attrs={'placeholder': 'Nombre del producto',
        'id':'descripcion','class':'form-control'} ),
        'descripcionAmp':forms.TextInput(attrs={'placeholder': 'Descripcion Detallada',
        'id':'descripcionAmp','class':'form-control'} ),
        'Deposito':forms.TextInput(attrs={'plnaceholder': 'Localizacion fisica del producto',
        'id':'Deposito','class':'form-control'} ),
        'disponible':forms.TextInput(attrs={'placeholder': 'Existencias Disponible',
        'id':'Disponible','class':'form-control'} ),
        'MinUnidades':forms.TextInput(attrs={'placeholder': 'Minimo en Stock',
        'id':'MinUnidades','class':'form-control'} ),
        'MaxUnidades':forms.TextInput(attrs={'placeholder': 'Maximo en Stock',
        'id':'MinUnidades','class':'form-control'} ),
        'categoria': forms.Select(attrs={'class':'form-control','id':'Tipo de Medida','class':'form-control'}),
        'activo': forms.CheckboxInput(attrs={'id':'activo'}),
        'tiene_iva': forms.CheckboxInput(attrs={'id':'tiene_iva'})


                }




class ImportarProductosFormulario(forms.Form):
    importar = forms.FileField(
        max_length = 100000000000,
        label = 'Escoger archivo',
        widget = forms.ClearableFileInput(
        attrs={'id':'importar','class':'form-control'}),
        )

class ImportarClientesFormulario(forms.Form):
    importar = forms.FileField(
        max_length = 100000000000,
        label = 'Escoger archivo',
        widget = forms.ClearableFileInput(
        attrs={'id':'importar','class':'form-control'}),
        )

class ExportarProductosFormulario(forms.Form):
    desde = forms.DateField(
        label = 'Desde',
        widget = forms.DateInput(format=('%d-%m-%Y'),
        attrs={'id':'desde','class':'form-control','type':'date'}),
        )

    hasta = forms.DateField(
        label = 'Hasta',
        widget = forms.DateInput(format=('%d-%m-%Y'),
        attrs={'id':'hasta','class':'form-control','type':'date'}),
        )

class ExportarClientesFormulario(forms.Form):
    desde = forms.DateField(
        label = 'Desde',
        widget = forms.DateInput(format=('%d-%m-%Y'),
        attrs={'id':'desde','class':'form-control','type':'date'}),
        )

    hasta = forms.DateField(
        label = 'Hasta',
        widget = forms.DateInput(format=('%d-%m-%Y'),
        attrs={'id':'hasta','class':'form-control','type':'date'}),
        )


class ClienteFormulario(forms.ModelForm):
    tipoC =  [ ('1','V'),('2','E'),('3','J'),('4','G') ]

    telefono2 = forms.CharField(
        required = False,
        label = 'Segundo numero telefonico',
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte el telefono alternativo del cliente',
        'id':'telefono2','class':'form-control'}),
        )

    correo2 = forms.CharField(
        required=False,
        label = 'Segundo correo electronico',
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte el correo alternativo del cliente',
        'id':'correo2','class':'form-control'}),
        )

    tipoCedula = forms.CharField(
        label="Tipo de cedula",
        max_length=2,
        widget=forms.Select(choices=tipoC,attrs={'placeholder': 'Tipo de cedula',
        'id':'tipoCedula','class':'form-control'}
        )
        )



    class Meta:
        model = Cliente
        fields = ['tipoCedula','cedula','nombre','apellido','direccion','nacimiento','telefono','correo','telefono2','correo2','activo']
        labels = {
        'cedula': 'Cedula del cliente',
        'nombre': 'Nombre del cliente',
        'apellido': 'Apellido del cliente',
        'direccion': 'Direccion del cliente',
        'nacimiento': 'Fecha de nacimiento del cliente',
        'telefono': 'Numero telefonico del cliente',
        'correo': 'Correo electronico del cliente',
        'telefono2': 'Segundo numero telefonico',
        'correo2': 'Segundo correo electronico',
        'activo': 'Esta activo?'
        }
        widgets = {
        'cedula': forms.TextInput(attrs={'placeholder': 'Inserte la cedula de identidad del cliente',
        'id':'cedula','class':'form-control'} ),
        'nombre': forms.TextInput(attrs={'placeholder': 'Inserte el primer o primeros nombres del cliente',
        'id':'nombre','class':'form-control'}),
        'apellido': forms.TextInput(attrs={'class':'form-control','id':'apellido','placeholder':'El apellido del cliente'}),
        'direccion': forms.TextInput(attrs={'class':'form-control','id':'direccion','placeholder':'Direccion del cliente'}),
        'nacimiento':forms.DateInput(format=('%Y-%m-%d'),attrs={'id':'nacimiento','class':'form-control','type':'date'} ),
        'telefono':forms.TextInput(attrs={'id':'telefono','class':'form-control',
        'placeholder':'El telefono del cliente'} ),
        'correo':forms.TextInput(attrs={'placeholder': 'Correo del cliente',
        'id':'correo','class':'form-control'} ),
        'activo': forms.CheckboxInput(attrs={'id':'activo'})
        }


class EmitirFacturaFormulario(forms.Form):
    def __init__(self, *args, **kwargs):
       elecciones = kwargs.pop('cedulas')
       super(EmitirFacturaFormulario, self).__init__(*args, **kwargs)

       if(elecciones):
            self.fields["cliente"] = forms.CharField(label="Cliente a facturar",max_length=50,
            widget=forms.Select(choices=elecciones,
            attrs={'placeholder': 'La cedula del cliente a facturar',
            'id':'cliente','class':'form-control'}))

    productos = forms.IntegerField(label="Numero de productos",widget=forms.NumberInput(attrs={'placeholder': 'Numero de productos a facturar',
        'id':'productos','class':'form-control'}))

class DetallesFacturaFormulario(forms.Form):
    productos = Producto.productosRegistrados()

    descripcion = MisProductos(queryset=productos,widget=forms.Select(attrs={'placeholder': 'El producto a debitar','class':'form-control select-group','onchange':'establecerOperaciones(this)'}))

    vista_precio = MisPrecios(required=False,queryset=productos,label="Precio del producto",widget=forms.Select(attrs={'placeholder': 'El precio del producto','class':'form-control','disabled':'true'}))

    cantidad = forms.IntegerField(label="Cantidad a facturar",min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Introduzca la cantidad del producto','class':'form-control','value':'0','onchange':'calculoPrecio(this);calculoDisponible(this)', 'max':'0'}))

    cantidad_disponibles = forms.IntegerField(required=False,label="Stock disponible",min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Introduzca la cantidad del producto','class':'form-control','value':'0', 'max':'0', 'disabled':'true'}))

    selec_disponibles = MisDisponibles(queryset=productos,required=False,widget=forms.Select(attrs={'placeholder': 'El producto a debitar','class':'form-control','disabled':'true','hidden':'true'}))

    subtotal = forms.DecimalField(required=False,label="Sub-total",min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Monto sub-total','class':'form-control','disabled':'true','value':'0'}))

    valor_subtotal = forms.DecimalField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Monto sub-total','class':'form-control','hidden':'true','value':'0'}))


class EmitirPedidoFormulario(forms.Form):
    def __init__(self, *args, **kwargs):
       elecciones = kwargs.pop('cedulas')
       super(EmitirPedidoFormulario, self).__init__(*args, **kwargs)

       if(elecciones):
            self.fields["proveedor"] = forms.CharField(label="Proveedor",max_length=50,
            widget=forms.Select(choices=elecciones,attrs={'placeholder': 'La cedula del proveedor que vende el producto',
            'id':'proveedor','class':'form-control'}))

    productos = forms.IntegerField(label="Numero de productos",widget=forms.NumberInput(attrs={'placeholder': 'Numero de productos a comprar',
        'id':'productos','class':'form-control'}))


class DetallesPedidoFormulario(forms.Form):
    productos = Producto.productosRegistrados()
    precios = Producto.preciosProductos()

    descripcion = MisProductos(queryset=productos,widget=forms.Select(attrs={'placeholder': 'El producto a debitar','class':'form-control','onchange':'establecerPrecio(this)'}))

    vista_precio = MisPrecios(required=False,queryset=productos,label="Precio del producto",widget=forms.Select(attrs={'placeholder': 'El precio del producto','class':'form-control','disabled':'true'}))

    cantidad = forms.IntegerField(label="Cantidad",min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Introduzca la cantidad del producto','class':'form-control','value':'0','onchange':'calculoPrecio(this)'}))

    subtotal = forms.DecimalField(required=False,label="Sub-total",min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Monto sub-total','class':'form-control','disabled':'true','value':'0'}))

    valor_subtotal = forms.DecimalField(min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Monto sub-total','class':'form-control','hidden':'true','value':'0'}))




class ProveedorFormulario(forms.ModelForm):
    tipoC =  [ ('1','V'),('2','E'),('3','J'),('4','G') ]

       
    telefono2 = forms.CharField(
        required = False,
        label = 'Segundo numero telefonico( Opcional )',
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte el telefono alternativo del proveedor',
        'id':'telefono2','class':'form-control'}),
        )

    correo2 = forms.CharField(
        required=False,
        label = 'Segundo correo electronico( Opcional )',
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte el correo alternativo del proveedor',
        'id':'correo2','class':'form-control'}),
        )

    tipoCedula = forms.CharField(
        label="Tipo de cedula",
        max_length=2,
        widget=forms.Select(choices=tipoC,attrs={'placeholder': 'Tipo de cedula',
        'id':'tipoCedula','class':'form-control'}
        )
        )


    class Meta:
        model = Proveedor
        fields = ['tipoCedula','cedula','nombre','apellido','direccion','nacimiento','telefono','correo','telefono2','correo2','activo']
        labels = {
        'cedula': 'Cedula del proveedor',
        'nombre': 'Nombre del proveedor',
        'apellido': 'Apellido del proveedor',
        'direccion': 'Direccion del proveedor',
        'nacimiento': 'Fecha de nacimiento del proveedor',
        'telefono': 'Numero telefonico del proveedor',
        'correo': 'Correo electronico del proveedor',
        'telefono2': 'Segundo numero telefonico',
        'correo2': 'Segundo correo electronico',
        'activo': 'Esta Activo'
        }
        widgets = {
        'cedula': forms.TextInput(attrs={'placeholder': 'Inserte la cedula de identidad del proveedor',
        'id':'cedula','class':'form-control'} ),
        'nombre': forms.TextInput(attrs={'placeholder': 'Inserte el primer o primeros nombres del proveedor',
        'id':'nombre','class':'form-control'}),
        'apellido': forms.TextInput(attrs={'class':'form-control','id':'apellido','placeholder':'El apellido del proveedor'}),
        'direccion': forms.TextInput(attrs={'class':'form-control','id':'direccion','placeholder':'Direccion del proveedor'}),
        'nacimiento':forms.DateInput(format=('%Y-%m-%d'),attrs={'id':'hasta','class':'form-control','type':'date'} ),
        'telefono':forms.TextInput(attrs={'id':'telefono','class':'form-control',
        'placeholder':'El telefono del proveedor'} ),
        'correo':forms.TextInput(attrs={'placeholder': 'Correo del proveedor',
        'id':'correo','class':'form-control'} ),
        'activo': forms.CheckboxInput(attrs={'id':'activo'})
        }


class UsuarioFormulario(forms.Form):
    niveles =  [ ('1','Administrador'),('0','Usuario') ]

    username = forms.CharField(
        label = "Nombre de usuario",
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un nombre de usuario',
        'id':'username','class':'form-control','value':''} ),
        )

    first_name = forms.CharField(
        label = 'Nombre',
        max_length =100,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un nombre',
        'id':'first_name','class':'form-control','value':''}),
        )

    last_name = forms.CharField(
        label = 'Apellido',
        max_length = 100,
        widget = forms.TextInput(attrs={'class':'form-control','id':'last_name','placeholder':'Inserte un apellido','value':''}),
        )

    email = forms.CharField(
        label = 'Correo electronico',
        max_length=100,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un correo valido',
        'id':'email','class':'form-control','type':'email','value':''} )
        )

    level =  forms.CharField(
        required=False,
        label="Nivel de acceso",
        max_length=2,
        widget=forms.Select(choices=niveles,attrs={'placeholder': 'El nivel de acceso',
        'id':'level','class':'form-control','value':''}
        )
        )

class NuevoUsuarioFormulario(forms.Form):
    niveles =  [ ('1','Administrador'),('0','Usuario') ]

    username = forms.CharField(
        label = "Nombre de usuario",
        max_length=50,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un nombre de usuario',
        'id':'username','class':'form-control','value':''} ),
        )

    first_name = forms.CharField(
        label = 'Nombre',
        max_length =100,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un nombre',
        'id':'first_name','class':'form-control','value':''}),
        )

    last_name = forms.CharField(
        label = 'Apellido',
        max_length = 100,
        widget = forms.TextInput(attrs={'class':'form-control','id':'last_name','placeholder':'Inserte un apellido','value':''}),
        )

    email = forms.CharField(
        label = 'Correo electronico',
        max_length=100,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte un correo valido',
        'id':'email','class':'form-control','type':'email','value':''} )
        )

    password = forms.CharField(
        label = 'Clave',
        max_length=100,
        widget = forms.TextInput(attrs={'placeholder': 'Inserte una clave',
        'id':'password','class':'form-control','type':'password','value':''} )
        )

    rep_password = forms.CharField(
        label = 'Repetir clave',
        max_length=100,
        widget = forms.TextInput(attrs={'placeholder': 'Repita la clave de arriba',
        'id':'rep_password','class':'form-control','type':'password','value':''} )
        )

    level =  forms.CharField(
        label="Nivel de acceso",
        max_length=2,
        widget=forms.Select(choices=niveles,attrs={'placeholder': 'El nivel de acceso',
        'id':'level','class':'form-control','value':''}
        )
        )


class ClaveFormulario(forms.Form):
    #clave = forms.CharField(
        #label = 'Ingrese su clave actual',
        #max_length=50,
        #widget = forms.TextInput(
        #attrs={'placeholder': 'Inserte la clave actual para verificar su identidad',
        #'id':'clave','class':'form-control', 'type': 'password'}),
        #)

    clave_nueva = forms.CharField(
        label = 'Ingrese la clave nueva',
        max_length=50,
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte la clave nueva de acceso',
        'id':'clave_nueva','class':'form-control', 'type': 'password'}),
        )

    repetir_clave = forms.CharField(
        label="Repita la clave nueva",
        max_length=50,
        widget = forms.TextInput(
        attrs={'placeholder': 'Vuelva a insertar la clave nueva',
        'id':'repetir_clave','class':'form-control', 'type': 'password'}),
        )


class ImportarBDDFormulario(forms.Form):
    archivo = forms.FileField(
        widget=forms.FileInput(
            attrs={'placeholder': 'Archivo de la base de datos',
            'id':'customFile','class':'custom-file-input'})
        )

class OpcionesFormulario(forms.Form):
    moneda = forms.CharField(
        label = 'Moneda a emplear en el sistema',
        max_length=20,
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte la abreviatura de la moneda que quiere usar (Ejemplo: $)',
        'id':'moneda','class':'form-control'}),
        )

    valor_iva = forms.DecimalField(
        label="Valor del IVA",
        min_value=0,widget=forms.NumberInput(
            attrs={'placeholder': 'Introduzca el IVA actual',
            'class':'form-control','id':'valor_iva'}))

    mensaje_factura = forms.CharField(
        label = 'Mensaje personal que va en las facturas',
        max_length=50,
        widget = forms.TextInput(
        attrs={'placeholder': 'Inserte el mensaje personal que ira en el pie de la factura',
        'id':'mensaje_factura','class':'form-control'}),
        )

    nombre_negocio = forms.CharField(
        label = 'Nombre actual del negocio',
        max_length=50,
        widget = forms.TextInput(
        attrs={'class':'form-control','id':'nombre_negocio',
            'placeholder':'Coloque el nombre actual del negocio'}),
        )

    imagen = forms.FileField(required=False,widget = forms.FileInput(
        attrs={'class':'custom-file-input','id':'customFile'}))

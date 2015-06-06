from django.db import models

# Create your models here.
class ProblemaSalud(models.Model):
    Name = models.CharField(max_length=100)
    Active = models.BooleanField()
    def __str__(self):
        return '%s' % self.Name

class Beneficio(models.Model):
    Name = models.CharField(max_length=100)
    Active = models.BooleanField()
    def __str__(self):
        return '%s' % self.Name

class Table(models.Model):
    Name = models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class Field(models.Model):
    Name = models.CharField(max_length=255)
    Table = models.OneToOneField(Table)
    def __str__(self):
        return '%s' % self.Name

class GrupoFamiliar(models.Model):
    OPCIONES_TIPO_FAMILIA = [('nuclear', 'Nuclear'),
                             ('binuclear', 'Binuclear')]

    direccion = models.CharField(max_length=100)
    historia_clinica = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    tipo_familia = models.CharField(max_length=50, choices=OPCIONES_TIPO_FAMILIA)
    def __str__(self):
        return '%s' % self.direccion


class Entrevista(models.Model):
    relevamiento = models.ForeignKey('Relevamiento')
    numero_entrevista = models.PositiveIntegerField()
    grupo_familiar = models.ForeignKey('GrupoFamiliar')
    entrevistador = models.ForeignKey("auth.User")
    entrevistado = models.ForeignKey('Persona')
    fecha = models.DateTimeField(auto_now=True)

class Persona(models.Model):
    VINCULO_TYPE = (
            ('Padre','Padre'),
            ('Hijo/a','Hijo'),
            ('Madre','Madre'),
            ('Abuelo/a','Abuelo'),
    )
    grupo_familiar = models.ForeignKey('GrupoFamiliar')

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30, choices=(('m', 'masculino'), ('f', 'femenino')))
    fecha_nacimiento = models.DateField()
    nacionalidad  = models.CharField(max_length=30)
    dni = models.IntegerField()
    vinculo = models.CharField(max_length=50,choices=VINCULO_TYPE)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

class CapitalFisico(models.Model):
    SIT_DOMINIAL_TYPE = (
            ('propietarioVivienda','Propietario de la Vivienda'),
            ('comodato','Comodato'),
            ('alquiler','Alquiler'),
            ('otro','Otro'),
        )
    CALEFACCION = (('gas_natural', 'Gas Natural',), ('gas_envasado', 'Gas Envasado'))
    entrevista = models.ForeignKey('Entrevista')
    habitaciones = models.PositiveIntegerField('Nº de Habitaciones')
    propietario_terreno = models.BooleanField()
    situacion_vivienda = models.CharField(max_length=50, choices=SIT_DOMINIAL_TYPE)

    pisos = models.BooleanField(help_text="La vivienda tiene pisos de baldosa, cerámicos y mosaicos")
    paredes = models.BooleanField(help_text="La vivienda tiene paredes exteriores de hormigón, ladrillo o bloque con revoque o revestimiento externo")
    techo = models.BooleanField(help_text="Techo de chapa de metal, fibrocemento, cielorraso, baldosa o losa")
    calefaccion = models.CharField(max_length=50, choices=CALEFACCION)

class CapitalSocial(models.Model):
    entrevista = models.ForeignKey('Entrevista')
    energia_electrica = models.BooleanField()
    recoleccion_residuo = models.BooleanField(help_text="Recolección de Residuos (mínimo 2 v/sem")
    transporte_publico = models.BooleanField(help_text="Transporte Público <300m")
    calle_pavimentada = models.BooleanField(help_text="Calle Mejorada/Pavimentada <300m")
    jardin_infantes = models.BooleanField(help_text="Jardín de Infantes (<=5 cuadras)")
    escuela_primaria = models.BooleanField(help_text="Escuela Primaria (<= 12 cuadras)")
    escuela_secundaria = models.BooleanField(help_text="Escuela Secundaria (<= 20 cuadras)")
    comisaria = models.BooleanField(help_text="Comisaria (<= 50 cuadras)")
    bomberos = models.BooleanField(help_text="Bomberos (<= 50 cuadras)")

class Relevamiento(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    zona = models.CharField(max_length=50, null=True, blank=True)
    nombre_zona = models.CharField(max_length=50, null=True, blank=True, help_text="ej: Villa el Libertador")

    def __str__(self):
        return "Relevamiento %s - %s" % (self.fecha_inicio, self.fecha_final)

from odoo import api, models, fields

class Moneda(models.Model):
    _name = 'm.moneda'
    cod = fields.Integer(required=True)
    es_variante = fields.Boolean()
    desc_error = fields.Char()
    color= fields.Selection(selection=[('rojo','rojo'), ('verde','verde'), ('azul','azul')], string='Color')
    ejemplar= fields.One2many(comodel_name='m.ejemplar', inverse_name='moneda')

class Ejemplar(models.Model):
    _name = 'm.ejemplar'
    cod = fields.Integer(required=True)
    num_correlativo = fields.Integer()
    fecha_compra = fields.Date()
    precio_compra = fields.Integer()
    fecha_venta = fields.Date()
    precio_venta = fields.Integer()
    moneda= fields.Many2one(comodel_name='m.moneda', string='moneda')

class Molde(models.Model):
    _name = 'm.molde'
    cod = fields.Integer(required=True)
    anyo_acunyacion = fields.Date()
    descripcion = fields.Char()
    fecha_estrellas = fields.Date()

class Modelo(models.Model):
    _name = 'm.modelo'
    cod = fields.Integer(required=True)
    unidad = fields.Char()
    diametro= fields.Integer()
    peso= fields.Integer()

class Modelo_Metal(models.Model):
    _name = 'm.modelo_metal'
    proporcion= fields.Integer() 
    ley= fields.Integer()  

class Metal(models.Model):
    _name = 'm.metal'
    nombre= fields.Char() 
from odoo import api, models, fields

class cerveza(models.Model):
    _name = 'ex.cerveza'
    tipo= fields.Char()
    nombre=fields.Char()
    Descripcion=fields.Text()
    contenido_de_alcohol=fields.Float()
    precio_por_unidad=fields.Float()
    volumen_por_unidad_ml=fields.Float()
    Disponible=fields.Boolean()
    lote_produccion=fields.One2many(comodel_name='ex.lote_produccion', inverse_name='cerveza')
    ingredientes=fields.Many2many(comodel_name='ex.ingrediente', string='ingredientes')

class lote_produccion (models.Model):
    _name = 'ex.lote_produccion'
    cerveza= fields.Many2one(comodel_name='ex.cerveza', string='cerveza')
    fecha_inicio_produccion=fields.Date()
    fecha_estimada_finalizacion=fields.Date()
    cantidad_producida=fields.Integer()
    estado=fields.Selection(selection=[('pr','En proceso'), 
                                        ('cm','Completo'), 
                                        ('em'," En espera de empaquetado")], 
                                        required=True, string='Estado')
    empaquetado= fields.Many2one(comodel_name='ex.empaquetado', string='empaquetado')

class ingrediente (models.Model):
    _name = 'ex.ingrediente'
    nombre=fields.Char()
    cantidad_disponible=fields.Float()
    tipo=fields.Selection(selection=[('ma','Malta'), 
                                    ('lu','Lúpulo'), 
                                    ('le','Levadura'), 
                                    ('ag','Agua'), 
                                    ('ot'," Otro")], 
                                    required=True, string='Tipo Ingrediente')

#Lote de Producción -> el empaquetado está asociado a uno o varios lotes de producción

class empaquetado (models.Model):
    _name = 'ex.empaquetado'
    lote_de_produccion=fields.Char()
    fecha_empaquetado=fields.Date()
    cantidad_empaquetada=fields.Integer()
    lote_produccion=fields.One2many(comodel_name='ex.lote_produccion', inverse_name='empaquetado')

class distribuidor (models.Model):
    _name = 'ex.distribuidor'
    nombre=fields.Char()
    direccion=fields.Text()
    telefono_contacto=fields.Integer()
    cervezas_suministradas=fields.Many2many(comodel_name='ex.cerveza', string='cerv')
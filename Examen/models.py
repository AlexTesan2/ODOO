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

    @api.constrains('contenido_de_alcohol', 'nombre')
    def _porciento(self):
        for record in self:
            if record.contenido_de_alcohol < 0:
                raise models.ValidationError("En una bebida, el porcentaje no puede ser menor de cero")
            elif record.contenido_de_alcohol > 100:
                raise models.ValidationError("En una bebida, el porcentaje, no puede ser mas de 100 ")
            else:
                pass

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
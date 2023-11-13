from odoo import api, models, fields
class Cliente(models.Model):
    _name = 'pr.cliente'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    edad= fields.Integer()
    altura = fields.Float()
    peso = fields.Float()
    imc = fields.Float(compute='_compute_imc', store=True)
    vendedor = fields.Many2one(comodel_name='pr.vendedor', string='vendedor')   #comodel: modelo con el que se relaciona
    proveedor = fields.Many2many(comodel_name='pr.proveedor', string='proveedor')

    @api.constrains('edad', 'name')
    def _check_edad(self):
        # solo se ejecuta una vez
        for record in self:
            if record.edad < 18:
                raise models.ValidationError("El cliente "+record.name+" debe ser mayor de edad")
            elif record.edad > 100:
                raise models.ValidationError("El cliente "+record.name+"  no puede ser tan viejo")
            else:
                pass
    
    @api.depends('altura', 'peso')
    def _compute_imc(self):
        for record in self:
            if record.altura > 0:
                record.imc = record.peso / (record.altura * record.altura)
            else:
                record.imc = 0

class Vendedor(models.Model):
    _name = 'pr.vendedor'
    name = fields.Char(required=True)
    company = fields.Char()
    fecha_incorporacion = fields.Date()
    fecha_despido = fields.Date(index=True)
    cliente = fields.One2many(comodel_name='pr.cliente', inverse_name='vendedor')

class proveedor(models.Model):
    _name = 'pr.proveedor'
    name = fields.Char(required=True)
    cif = fields.Char(required=True)
    titular = fields.Char()
    #cliente = fields.Many2many(comodel_name='pr.cliente', string='cliente')
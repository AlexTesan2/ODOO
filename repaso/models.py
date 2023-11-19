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

#Herencia:

# imaginad que esta en otro modulo
class Colores(models.Model):
    _name = 'pr.colores'
    name = fields.Char(required=True, string='Nombre')
    color = fields.Selection(selection=[('rojo','Color rojo'), 
                                        ('verde','Color verde'), 
                                        ('azul',"Color Azul")], 
                                        required=True, string='Color RGB')

class AdicionColorida(models.Model):
    # NO genera una new tabla en la bas e de datos; no tiene _name
    # Solamente extiende la tabla de la que hereda
    _inherit = 'pr.colores'
    color_secundario = fields.Selection(selection=[('cyan','Color cyan'), 
                                            ('magenta','Color magenta'), 
                                            ('yellow',"Color yellow")], 
                                            required=True, string='AdicionColorida')

class Artes(models.Model):
    # SI genera una new tabla en la bas e de datos; tiene _name
    # Tendra todos los campos de la tabla que hereda, inclidos los de AdicionColorida, mas los propios
    _inherit = 'pr.colores'
    _name = 'pr.arte'
    tipo_arte = fields.Selection(selection=[('esc','Escultura'),
                                                ('pin','Pintura'), 
                                                ('mu',"Musica")],
                                                required=True, string='Arte')


# Herencia de modulo

class canicas(models.Model):
    _inherit = 'm.modelo'
    _name = 'pr.canica'
    color_canica = fields.Selection(selection=[('a','Color cyan'), 
                                                ('r','Color magenta'), 
                                                ('v',"Color verde")], 
                                                required=True, string='color_canica')
    fabricante = fields.Char()
    unidades_vendidas = fields.Integer()
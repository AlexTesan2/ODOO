from odoo import api, models, fields

class mascota(models.Model):
    _name = 'vet.mascota'
    cod = fields.Integer(required=True)
    nombre = fields.Char()
    especie= fields.Selection(selection=[('pe','perro'), ('ga','gato'),
                                        ('co','conejo'),('ro','pequenos_roedores'),
                                        ('pa','pajaro'),('ot','otro')], string='Especie')
    
    sexo= fields.Selection(selection=[('m','macho'),('h','hembra')], string='sexo')
    edad = fields.Integer()
    commentario = fields.Char()
    castrado = fields.Boolean()
    vivo = fields.Boolean()
    dueno = fields.Many2one(comodel_name='vet.dueno', string='dueno')


class dueno(models.Model):
    _name = 'vet.dueno'
    cod = fields.Integer(required=True)
    nombre = fields.Char()
    apellidos = fields.Char()
    telefono = fields.Integer()
    dni = fields.Char()
    commentario = fields.Char()
    mascotas= fields.One2many(comodel_name='vet.mascota', inverse_name='dueno')
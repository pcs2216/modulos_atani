# -*- coding: utf-8 -*-

from odoo import api, fields, models


class x_Partner(models.Model):

    _inherit = 'res.partner'

    x_phone2 = fields.Char(string="Teléfono 2")
    x_nombreComercial = fields.Char(string='Nombre Comercial')
    

    x_marcas = fields.Many2many('x.model.marcas',
                               string='Principales marcas que maneja',
                               ondelete='set null',
                               )   

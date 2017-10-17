# -*- coding: utf-8 -*-

from odoo import api, fields, models


class x_Marcas(models.Model):
    _name =  'x.model.marcas'

    
    x_name = fields.Char(
        string='Marca',
    )
    
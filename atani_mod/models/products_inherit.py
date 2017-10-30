# -*- coding: utf-8 -*-

from odoo import api, fields, models


class x_Products(models.Model):

    _inherit = 'product.template'

    
    x_marcaProducto  = fields.Many2one('x.model.marcas',
        string='Marca',        
        ondelete='set null',
    )
    
    
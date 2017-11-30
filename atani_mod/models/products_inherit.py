# -*- coding: utf-8 -*-

from odoo import api, fields, models


class x_Products(models.Model):

    _inherit = 'product.template'

    
    x_marcaProducto  = fields.Many2one('x.model.marcas',
        string='Marca',        
        ondelete='set null',
    )
    
    
    x_etiqueta = fields.Selection(
        string=u'Etiqueta Moneda',
        help='Agregar etiqueta del tipo de moneda para filtrar y actualizarlos',
        selection=[('MXN', 'MXN'), ('USD', 'USD')]
    )
    
    x_descripcion = fields.Text(
        string='Descripción',
    )
    
    
    
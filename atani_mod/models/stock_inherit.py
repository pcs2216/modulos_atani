# -*- coding: utf-8 -*-

from odoo import api, fields, models


class x_Stock(models.Model):

    _inherit = 'stock.picking'

    x_responsable = fields.Many2one('hr.employee',
                                    string='Responsable',
                                    ondelete='set null',
                                    )

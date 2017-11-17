# -*- coding: utf-8 -*-

from odoo import api, fields, models


class x_Empleado(models.Model):

    _inherit = 'hr.employee'

    
    x_tiempoCasaTrabajo = fields.Float(
        string='Distancia Casa-Trabajo', help='En Horas'
    )
    
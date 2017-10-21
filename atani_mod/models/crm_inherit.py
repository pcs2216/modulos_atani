# -*- coding: utf-8 -*-

from odoo import api, fields, models


class x_CRM_LEAD(models.Model):

    _inherit = 'crm.lead'
    #_description='Modificaciones al modelo crm.lead'

    
    x_cuentaPlanos = fields.Boolean(
        string='¿Cuenta con planos?',
    )
    x_planosURL = fields.Char(
        string='URL de planos',
    )
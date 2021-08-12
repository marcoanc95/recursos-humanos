# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    backup = fields.Many2one('hr.employee', string="Backup")

from odoo import models, fields, api


class Stamps(models.Model):
    _name = 'stamps.stamps'
    _description = 'Sellos'
    
    employee_ids = fields.Many2one(
        "hr.employee", 
        string="Entregado por",
        required=True
    )
    employee_recibe_ids = fields.Many2one(
        "hr.employee", 
        string="Recibido por",
        required=True
    )
    amount_deliver = fields.Integer(
        string="Cantidad",
        required=True)

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
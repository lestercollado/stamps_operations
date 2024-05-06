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

    date = fields.Date(
        string="Fecha"
    )
    
    letter = fields.Char('Prefijo')
    
    stamps_start = fields.Integer('Número Sello Inicial')
    
    stamps_end = fields.Integer(
        string= 'Número Sello Final',
        compute='_compute_stamps_end'
    )
    
    area = fields.Selection([
        ('Tren', 'Tren'),
        ('Muelle', 'Muelle'),
        ('Salida', 'Salida'),
        ('Explanada', 'Explanada'),
    ], string='Área')
            
    @api.multi
    @api.depends('employee_ids','employee_recibe_ids')
    def name_get(self):
        result = []
        for account in self:
            name = account.employee_ids.name + ' a ' + account.employee_recibe_ids.name
            result.append((account.id, name))
        return result
    
    @api.depends('stamps_start','amount_deliver')
    def _compute_stamps_end(self):
        for record in self:
            record.stamps_end = record.stamps_start + record.amount_deliver
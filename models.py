from odoo import tools, models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date,datetime

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    @api.depends('product_id')
    def _compute_category_id(self):
        for rec in self:
            if rec.product_id and rec.product_id.categ_id:
                rec.category_id = rec.product_id.categ_id.id
            else:
                rec.category_id = None

    category_id = fields.Many2one('product.category','Category',store=True,compute=_compute_category_id)

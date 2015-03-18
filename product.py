# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Product(models.Model):
    _inherit = 'product.template'

    @api.one
    @api.depends('length', 'width', 'height', 'dimensional_uom')
    def compute_volume(self):
        if not self.length or not self.height or not self.width or not self.dimensional_uom:
            self.volume = False
        else:
            self.volume = self.length * self.height * self.width / pow(self.dimensional_uom.factor, 3)

    length = fields.Float(
        string='Length'
    )

    width = fields.Float(
        string='Width'
    )

    height = fields.Float(
        string='Height'
    )

    volume = fields.Float(
        string='Volume',
        help='The volume in m³.',
        store=True,
        compute=compute_volume
    )

    dimensional_uom = fields.Many2one(
        'product.uom',
        'Dimensional UOM',
        help='UOM for dimensions'
        # TODO: A _reliable_ domain to filter out other than length UOM's.
    )

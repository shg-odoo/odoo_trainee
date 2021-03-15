from odoo import models, fields, api

class Labourers(models.TransientModel):
	_name='manufacturer.labourers.wizard'

	manufacturer_id = fields.Many2one('manufacturer')

	def add_manufacturer(self):
		active_ids = self._context.get('active_ids')
		self.env['manufacturer.labourers'].browse(active_ids).write({'manufacturer_id': self.manufacturer_id})

	role_id = fields.Many2one('labourers.roles')

	def add_role(self):
		active_ids = self._context.get('active_ids')
		self.env['manufacturer.labourers'].browse(active_ids).write({'role_id': self.role_id})

	
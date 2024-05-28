# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Room(models.Model):
    _name = 'hotelitic.room'

    name = fields.Char(string="Numero d'habitació")
    capacity = fields.Integer(string='Capacitat')
    hasTV = fields.Boolean(string='TV', default=True)
    floor = fields.Integer(compute='_compute_floor',string='Pis')

    client_ids = fields.One2many('hotelitic.client','room_id')

    @api.depends('name')
    def _compute_floor(self):
        for record in self:
            if record.name.isdigit():
                record.floor = int(record.name[0])
            else:
                record.floor = None

    @api.constrains('client_ids','capacity')
    def _check_clients(self):
        for record in self:
            if record.capacity and len(record.client_ids) > record.capacity:
                raise ValidationError('The room has only place for '+str(record.capacity)+ ' people')
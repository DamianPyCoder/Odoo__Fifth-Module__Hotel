# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Client(models.Model):
    _name = 'hotelitic.client'

    name = fields.Char(string="Nom")
    dni = fields.Char(string='DNI')
    birthday = fields.Date(string='Data de naixement')

    room_id = fields.Many2one('hotelitic.room')
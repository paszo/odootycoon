# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odootycoon_gamemanager(models.Model):
    _name = 'odootycoon.gamemanager'
    name = fields.Char("Game Name", default="New Game")
    day = fields.Integer("Current Day", default=1)
    cash = fields.Float("Cash", default=5000)

    def nextday(self):
        # Easy way ... bu two to the Postgres server
        #self.day += 1
        #self.cash -= 100

        # This is the efficeint way
        self.write({'day': self.day + 1, 'cash': self.cash - 100})

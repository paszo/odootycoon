# -*- coding: utf-8 -*-

from odoo import models, fields, api

class odootycoon_producttemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    unlockcost = fields.Float('Unlock Cost', default=750)
    unlocked = fields.Boolean('Unlocked', default=False)



class odootycoon_gamemanager(models.Model):
    _name = 'odootycoon.gamemanager'
    name = fields.Char("Game Name", default="New Game")
    day = fields.Integer("Current Day", default=1)
    cash = fields.Float("Cash", default=1000)

    def nextday(self):

        # Process Unlocked Products
        products = self.env['product.template'].search([('unlocked', '=', True)])
        cash = 0
        for product in products:
            cash += product.list_price *10



        # Easy way ... bu two to the Postgres server
        #self.day += 1
        #self.cash -= 100

        # This is the efficeint way
        self.write({'day': self.day + 1, 'cash': self.cash + cash})

    def skip5days(self):
        for i in range(0,5):
            print(i)
            self.nextday()

    def skip30days(self):
        for i in range(0,30):
            print(i)
            self.nextday()

    def resetgame(self):
        self.write({'day': 1, 'cash': 1000})
        self.env['product.template'].search([('unlocked', '=', True)]).write({'unlocked': False})

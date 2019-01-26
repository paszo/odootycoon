# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import Warning
from random import randint

class odootycoon_producttemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    unlockcost = fields.Float('Unlock Cost', default=750)
    unlocked = fields.Boolean('Unlocked', default=False)

    def unlockproduct(self):
        # record id = 6 is the one we have active in the database
        # this is a bad code - need to be upgraded
        gamemanager = self.env['odootycoon.gamemanager'].search([('id', '=', 6)])
        if gamemanager.cash >= self.unlockcost:
            self.unlocked = True
            gamemanager.cash -= self.unlockcost
        else:
            raise Warning("You do not have enough money to unlock the %s product!" % self.name)




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
            numsold = randint(5,25)
            print(numsold)
            cash += product.list_price * numsold



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

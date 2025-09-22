# -*- coding: utf-8 -*-
from odoo import models, fields

class AccountGeneralLedgerCustom(models.Model):
    _name = "account.general.ledger.custom"
    _description = "Grand Livre Personnalisé"
    _auto = False

    id = fields.Integer(string="ID", readonly=True)
    date = fields.Date(string="Date")
    account_id = fields.Integer(string="Compte")  
    journal_id = fields.Integer(string="Journal")
    move_id = fields.Integer(string="Écriture")
    partner_id = fields.Integer(string="Partenaire")

    initial_balance = fields.Float(string="Solde Initial")
    debit = fields.Float(string="Débit")
    credit = fields.Float(string="Crédit")
    final_balance = fields.Float(string="Solde Final")

    def init(self):
        self.env.cr.execute("""
            -- Supprime la vue si elle existe pour éviter les conflits
            DROP VIEW IF EXISTS account_general_ledger_custom;
            
            CREATE VIEW account_general_ledger_custom AS
            SELECT
                l.id AS id,
                l.date AS date,
                l.account_id AS account_id,
                l.journal_id AS journal_id,
                l.move_id AS move_id,
                l.partner_id AS partner_id,
                0.0 AS initial_balance,
                l.debit AS debit,
                l.credit AS credit,
                (0.0 + l.debit - l.credit) AS final_balance
            FROM account_move_line l
            WHERE l.parent_state = 'posted';
        """)


class AccountTrialBalanceCustom(models.Model):
    _name = "account.trial.balance.custom"
    _description = "Balance Personnalisée"
    _auto = False

    id = fields.Integer(string="ID", readonly=True)
    account_id = fields.Integer(string="Compte")
    partner_id = fields.Integer(string="Partenaire")
    date = fields.Date(string="Date") 
    initial_balance = fields.Float(string="Solde Initial")
    debit = fields.Float(string="Débit")
    credit = fields.Float(string="Crédit")
    final_balance = fields.Float(string="Solde Final")

    def init(self):
        self.env.cr.execute("""
            DROP VIEW IF EXISTS account_trial_balance_custom;

            CREATE VIEW account_trial_balance_custom AS
            SELECT
                row_number() OVER() AS id,
                l.account_id AS account_id,
                l.partner_id AS partner_id,
                l.date AS date,                 -- <--- Ajout du champ date
                0.0 AS initial_balance,
                SUM(l.debit) AS debit,
                SUM(l.credit) AS credit,
            (   0.0 + SUM(l.debit) - SUM(l.credit)) AS final_balance
            FROM account_move_line l
            WHERE l.parent_state = 'posted'
            GROUP BY l.account_id, l.partner_id, l.date;  -- <--- Grouper par date
        """)

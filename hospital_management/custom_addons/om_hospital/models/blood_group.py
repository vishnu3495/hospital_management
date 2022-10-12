from odoo import models,fields

class BloodBank(models.Model):
    _name='hospital.blood_bank'
    _rec_name ="blood_group"


    blood_group=fields.Char(string="Blood Group")



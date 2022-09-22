from odoo import models,fields


class HospitalDoctors(models.Model):
    # _inherit = 'hospital.patient'
    _name="hospital.doctors"
    _description = "Hospital Doctors"
    _rec_name = "doctor_name"

    doctor_name=fields.Char(string='Doctor Name')
    age = fields.Integer(string='Age')
    place=fields.Char(string='Place')
    specialise=fields.Char(string='Specialisation')

    patient_ids=fields.One2many('hospital.patient','doctor_detail_id',string='Patient')


   # gender=fields.Selection(selection_add=[('other','other')])


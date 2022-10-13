from odoo import models, fields,_,api
from datetime import datetime,date

class HospitalDoctors(models.Model):
    # _inherit = 'hospital.patient'
    _name = "hospital.doctors"
    _description = "Hospital Doctors"
    _rec_name = "doctor_name"


    doctor_name = fields.Char(string='Doctor Name')
    age = fields.Integer(string='Age')
    place = fields.Char(string='Place')
    specialise = fields.Char(string='Specialisation')
    image = fields.Binary(string="Patient Image")
    patient_ids = fields.One2many('hospital.patient', 'doctor_detail_id', string='Patient')
    refs = fields.Char(string="Reference")


# gender = fields.Selection(selection_add=[('other', 'other')])


    def copy(self,default=None):
        if default is None:
            default={}
        if not default.get('doctor_name'):
            default['doctor_name'] = _("%s -Duplicate",self.doctor_name)
        return super(HospitalDoctors, self).copy(default)

    @api.model
    def create(self, vals):
        vals['refs'] = self.env['ir.sequence'].next_by_code('hospital.doctors')
        return super(HospitalDoctors, self).create(vals)

    def write(self, vals):
        if not self.refs:
            vals['refs'] = self.env['ir.sequence'].next_by_code('hospital.doctors')
        return super(HospitalDoctors, self).write(vals)








from odoo import models,fields

class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description="Hospital Patient"


    name=fields.Char(string='Name')
    age=fields.Integer(string='Age')
    gender=fields.Selection(
        [('male','Male'),
         ('female','Female')])
    remarks=fields.Text(string='Remarks')
    date=fields.Date(string='Date')
    datetime=fields.Datetime(string='Date/Time')
    completed=fields.Boolean(string="Completed",status="False")

    blood_id = fields.Many2one('hospital.blood_bank', string='Blood')
    doctor_ids=fields.Many2many('hospital.doctors','doctor_patient_rel','doctor_id', 'patient_id',string='Doctors')

    doctor_detail_id=fields.Many2one('hospital.doctors',string='Doctors List')












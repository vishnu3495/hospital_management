from odoo import models, fields,api


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _rec_name = "patient_id"

    patient_id=fields.Many2one('hospital.patient',string="Patient")
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female'),
         ('other','Other')],string="Gender")
    age=fields.Integer(string="Age",copy=False)
    date = fields.Date(string='Date')
    remarks = fields.Text(string='Remarks')


    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.gender = self.patient_id and self.patient_id.gender or ''
        self.age = self.patient_id and self.patient_id.age or ''
        self.date = self.patient_id and self.patient_id.date or ''
        self.remarks = self.patient_id and self.patient_id.remarks or ''

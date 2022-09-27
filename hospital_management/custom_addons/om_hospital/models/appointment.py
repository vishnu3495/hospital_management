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
    age=fields.Integer(string="Age")
    date = fields.Date(string='Date')
    remarks = fields.Text(string='Remarks')

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        if self.patient_id:
            if self.patient_id.gender:
                self.gender=self.patient_id.gender
            if self.patient_id.age:
                self.age=self.patient_id.age
            if self.patient_id.date:
                self.date=self.patient_id.date
            if self.patient_id.remarks:
                self.remarks=self.patient_id.remarks
        else:
            self.gender=''
            self.age=''
            self.date=''
            self.remarks=''




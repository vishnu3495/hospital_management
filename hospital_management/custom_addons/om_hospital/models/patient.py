from odoo import models,fields,api
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name="hospital.patient"
    _description="Hospital Patient"



    name=fields.Char(string='Name',required=True)
    age=fields.Integer(string='Age')
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female'),
         ('other', 'Other')], string="Gender")
    remarks=fields.Text(string='Remarks')
    date=fields.Date(string='Date')
    datetime=fields.Datetime(string='Date/Time')
    completed=fields.Boolean(string="Completed",status="False")

    appointment_count=fields.Integer(string='Appointment Count',compute="_compute_appointment_count")

    blood_id = fields.Many2one('hospital.blood_bank', string='Blood',ondelete='cascade')
    doctor_ids=fields.Many2many('hospital.doctors','doctor_patient_rel','doctor_id', 'patient_id',string='Doctors')
    doctor_detail_id=fields.Many2one('hospital.doctors',string='Doctors List')

    state=fields.Selection([('draft','Draft'),('submit','Submit')],default='draft',string='Status')


    def _compute_appointment_count(self):
        for rec in self:
            appointment_count=self.env['hospital.appointment'].search_count([('patient_id','=',rec.id)])
            rec.appointment_count=appointment_count

    @api.model
    def default_get(self,fields):
        res=super(HospitalPatient,self).default_get(fields)
        res['state']='draft'
        return res

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            patients=self.env['hospital.patient'].search([('name','=',rec.name),('id','!=',rec.id)])
            if patients:
                raise ValidationError(("Name %s Already Exists" % rec.name))


    def action_submit(self):
        self.state='submit'









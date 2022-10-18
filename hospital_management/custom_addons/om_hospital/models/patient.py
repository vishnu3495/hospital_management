from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import datetime,date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _rec_name = "ref"


    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female'),
         ('other', 'Other')], string="Gender")

    ref = fields.Char(string="Reference")
    image=fields.Binary(string="Patient Image")
    remarks = fields.Text(string='Remarks')
    date = fields.Date(string='Date')
    datetime = fields.Datetime(string='Date/Time')
    completed = fields.Boolean(string="Completed", status="False")


    appointment_count = fields.Integer(string='Appointment Count', compute="_compute_appointment_count")

    blood_id = fields.Many2one('hospital.blood_bank', string='Blood', ondelete='cascade')
    doctor_ids = fields.Many2many('hospital.doctors', 'doctor_patient_rel', 'doctor_id', 'patient_id', string='Doctors')
    doctor_detail_id = fields.Many2one('hospital.doctors', string='Doctors List')

    state = fields.Selection([('draft', 'Draft'), ('submit', 'Submit'),('scheduled','Scheduled')], default='draft', string='Status')

    def action_submit(self):
        self.state = 'submit'

    def _compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])
            rec.appointment_count = appointment_count


    #EITHER DRAFT IN STATE OR DO BY DEFAULT_GET

    @api.model
    def default_get(self, fields):
        res = super(HospitalPatient, self).default_get(fields)
        res['state'] = 'draft'
        return res

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            patients = self.env['hospital.patient'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if patients:
                raise ValidationError(_("Name %s Already Exists" % rec.name))

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        if not self.ref:
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    def unlink(self):
        if self.gender == 'male':
            raise ValidationError(_("You Cannot Delete %s because gender is male" % self.name))
        return super(HospitalPatient, self).unlink()

    @api.constrains('name')
    def validate_name(self):
        for types in self.search([('id', '!=', self.id)]):
            if types.name:
                if ((self.name.upper()) == types.name.upper()):
                    raise ValidationError(_('The Name Must Be unique !'))


    def name_get(self):
        result = []
        for rec in self:
            ref = '[' + rec.ref + ']--' + str(rec.name)
            result.append((rec.id, ref))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('ref', operator, name), ('name', operator, name)]
        return self._search(domain + args, limit=limit)


    def _get_values_in_report(self):
        now = datetime.strftime(fields.Datetime.context_timestamp(self, datetime.now()), "%d-%m-%Y %H:%M:%S")
        return now

    @api.model
    def test_cron_job(self):
        schedule=self.env['hospital.patient'].search([('date', '=', date.today())])
        for rec in schedule:
            if rec.date:
                rec['state']='scheduled'
        return rec








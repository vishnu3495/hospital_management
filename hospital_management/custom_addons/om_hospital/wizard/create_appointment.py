from odoo import api,fields,models

class CreateAppointmentWizard(models.TransientModel):
    _name="create.appointment.wizard"
    _description="Create Appointment Wizard"

    patient_id=fields.Many2one('hospital.patient',string='Patient ID')
    name=fields.Char(string='Name',required=True)


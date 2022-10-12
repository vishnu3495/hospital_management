from odoo import models


class PatientDoctorXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_doctor_id_card_xls'
    _inherit = 'report.report_xlsx.abstract'


    def generate_xlsx_report(self, workbook, data, patients):
        sheet = workbook.add_worksheet('Patient Doctor')
        format = workbook.add_format({'bold': True, 'font_color': 'red', 'align': 'center'})
        format_3= workbook.add_format({'bold': True, 'font_color': 'blue', 'align': 'center'})
        format_1 = workbook.add_format({'bold': True, 'font_color': 'green', 'align': 'left'})
        format_2 = workbook.add_format({'bold': True, 'font_color': 'black', 'align': 'left'})


        sheet.set_column('A:B', 13)
        sheet.set_column('C:D', 20)


        sheet.merge_range('A1:D1', 'PATIENT DOCTOR', format)
        row = 1
        col = 0

        sheet.merge_range(row, col, row, col + 1, 'DOCTORS', format_3)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'PATIENT', format_3)

        for obj in patients:
            row = row + 1
            col = 0
            sheet.merge_range(row, col, row, col + 1, obj.doctor_name, format_2)
            col = col + 2

            list = []
            for line in obj.patient_ids:
                list.append(line.name)
                sheet.merge_range(row, col, row, col + 1, ','.join(list),format_1)
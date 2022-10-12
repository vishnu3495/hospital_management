from odoo import models

class PatientCardXlsx(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_id_card_xls'
    _inherit = 'report.report_xlsx.abstract'


    # def generate_xlsx_report(self, workbook, data, patients):
    #     sheet = workbook.add_worksheet('Hospital Record')
    #     bold = workbook.add_format({'bold': True})
    #     format_1=workbook.add_format({'bold':True,'align':'center','bg_color':'grey'})
    #     row=0
    #     col=0
    #     sheet.set_column('A:A',13)
    #     sheet.set_column('E:E',13)
    #
    #     for obj in patients:
    #         row+=1
    #         sheet.merge_range(row,col,row,col+1,'Hospital Record',format_1)
    #
    #         row+=1
    #         sheet.write(row, col,'Name',bold)
    #         sheet.write(row,col+1,obj.name)
    #         row += 1
    #         sheet.write(row, col, 'Age', bold)
    #         sheet.write(row, col+1, obj.age)
    #         row += 1
    #         sheet.write(row, col, 'Gender', bold)
    #         sheet.write(row, col+1, obj.gender)


    def generate_xlsx_report(self, workbook, data, patients):
        sheet = workbook.add_worksheet('Hospital Record')
        format = workbook.add_format({'bold': True, 'font_color': 'black', 'align': 'center', 'border':7})
        format_1 = workbook.add_format({'bold': True, 'font_color': 'blue', 'align': 'left'})
        format_2 = workbook.add_format({'bold': True, 'font_color': 'red', 'align': 'center', 'bg_color': 'gray'})
        format_3 = workbook.add_format({'bold': True, 'font_color': 'green', 'align': 'right'})
        date=workbook.add_format({'bold':True,'font_color':'blue','num_format':'dd-mm-yyyy','align':'right'})

        sheet.set_column('A:B', 8)
        sheet.set_column('C:D', 8)
        sheet.set_column('E:F', 8)
        sheet.set_column('G:H', 8)
        sheet.set_column('I:J', 8)
        sheet.set_column('K:L', 13)
        sheet.set_column('M:N', 8)
        sheet.set_column('O:P',8)
        sheet.set_column('Q:R', 15)


        sheet.merge_range('A1:R1', 'HOSPITAL RECORD', format_2)
        row = 1
        col = 0

        sheet.merge_range(row, col, row, col + 1, 'REFERENCE', format)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'NAME', format)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'AGE', format)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'GENDER', format)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'DATE', format)
        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'APPOINTMENT COUNT', format)
        col=col+2
        sheet.merge_range(row,col,row,col+1,'TOTAL',format)

        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'BLOOD GROUP', format)

        col = col + 2
        sheet.merge_range(row, col, row, col + 1, 'DOCTORS', format)


        for obj in patients:

            row = row + 1
            col = 0
            sheet.merge_range(row, col, row, col + 1, obj.ref, format_1)
            col += 2
            sheet.merge_range(row, col, row, col + 1, obj.name, format_1)
            col += 2
            sheet.merge_range(row, col, row, col + 1, obj.age, format_3)

            col += 2
            gender=dict(obj._fields['gender'].selection).get(obj.gender) or False
            sheet.merge_range(row, col, row, col + 1,gender, format_1)

            col+=2
            sheet.merge_range(row, col, row, col + 1, obj.date, date)

            col += 2
            sheet.merge_range(row, col, row, col + 1, obj.appointment_count, format_3)

            col+=2
            Total=obj.age+obj.appointment_count
            sheet.merge_range(row,col,row,col+1,Total,format_3)

            col += 2
            sheet.merge_range(row, col,row,col+1,obj.blood_id.blood_group,format_1)

            col = col + 2
            list = []
            for line in obj.doctor_ids:
                list.append(line. doctor_name)
                sheet.merge_range(row, col, row, col + 1, ','.join(list),format_1)







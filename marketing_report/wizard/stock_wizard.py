from odoo import models, fields, api
from odoo.tools import ustr
from io import BytesIO
import base64
import xlsxwriter
from datetime import datetime


class StockLocationWizard(models.TransientModel):
    _name = 'stock.val.wizard'

    date_from = fields.Date()
    date_to = fields.Date()

    def print_xls(self):
        output = BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Crm Report')

        title_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'font_color': 'purple',
            'font_size': 14,
            'bg_color': '#D3DFEE'
        })

        section_header_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
            'bg_color': '#F2F2F2'
        })

        header_format = workbook.add_format({
            'bold': True,
            'align': 'center',
            'valign': 'vcenter',
        })

        cell_format = workbook.add_format({
            'align': 'center',
            'valign': 'vcenter',
        })

        report_title = 'Marketing Report as of {}'.format(datetime.today().strftime('%d/%m/%Y'))
        worksheet.merge_range('A1:P1', report_title, title_format)

        worksheet.merge_range('A2:H2', 'Customer Information', section_header_format)
        worksheet.merge_range('I2:P2', 'Potential Information', section_header_format)

        headers = ['S.No', 'Sales Staff Name', 'Hospital/Clinic Name', 'Contact Person (Purchase)', 'Contact No.',
                   'Email Id', 'Area/City', 'Emirates', 'Date Visited', 'Current Uniform Details',
                   'Approximate No of Staffs', 'Last Purchase',
                   'Approximate Budget', 'Future Purchase Plan', 'Activities', 'Remarks']
        for col, header in enumerate(headers):
            worksheet.write(2, col, header, header_format)

        worksheet.set_column('A:O', 20)

        records = self.env['crm.lead'].search(
            [("create_date", '>=', self.date_from), ('create_date', '<=', self.date_to), ('type', '=', 'opportunity')])

        row = 3
        sequence_number = 1
        for record in records:
            worksheet.write(row, 0, sequence_number, cell_format)
            worksheet.write(row, 1, ustr(record.partner_id.name)) if record.partner_id.user_id.name else ""
            worksheet.write(row, 2, ustr(record.name)) if record.name else ""
            worksheet.write(row, 3, ustr(record.partner_id.buyer_id.name),
                            ) if record.partner_id.buyer_id.name else ""
            worksheet.write(row, 4, record.phone, cell_format) if record.phone else ""
            worksheet.write(row, 5, ustr(record.email_from)) if record.email_from else ""
            worksheet.write(row, 6, ustr(record.area_city), cell_format) if record.area_city else ""
            worksheet.write(row, 7, ustr(record.partner_id.country_id.name),
                            cell_format) if record.partner_id.country_id.name else ""
            worksheet.write(row, 8, record.date_visited or '', cell_format) if record.date_visited else ""
            worksheet.write(row, 9, (ustr(record.current_uniform_details)),
                            cell_format) if record.current_uniform_details else ""
            worksheet.write(row, 10, ustr(record.approx_no_off_staff) or '',
                            cell_format) if record.approx_no_off_staff else ""
            worksheet.write(row, 11, ustr(record.last_purchase), cell_format) if record.last_purchase else ""
            worksheet.write(row, 12, ustr(record.approx_budget)) if record.approx_budget else ""
            worksheet.write(row, 13, ustr(record.future_purchase_plan),
                            cell_format) if record.future_purchase_plan else ""
            worksheet.write(row, 14, ustr(record.activities), cell_format) if record.activities else ""
            worksheet.write(row, 15, ustr(record.remarks)) if record.remarks else ""
            row += 1
            sequence_number += 1

        workbook.close()
        output.seek(0)
        xls_data = base64.b64encode(output.read())

        attachment = self.env['ir.attachment'].create({
            'name': 'Crm_Report.xlsx',
            'datas': xls_data,
            'res_model': 'crm.lead',
            'res_id': self.ids[0],
            'type': 'binary'
        })

        return {
            'type': 'ir.actions.act_url',
            'url': 'web/content/%s?download=true' % attachment.id,
            'target': 'self',
        }

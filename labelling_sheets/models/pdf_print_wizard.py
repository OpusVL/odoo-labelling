# -*- coding: utf-8 -*-

##############################################################################
#
# Print on labelling sheets
# Copyright (C) 2016 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api

class LabellingSheetsPrintWizard(models.TransientModel):
    _name = 'labelling.sheets.print.wizard'

    @api.multi
    def print_pdf(self):
        self.ensure_one()
        return self.env['report'].get_action(self, 'labelling_sheets.label_pdf_report')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

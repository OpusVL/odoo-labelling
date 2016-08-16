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

import logging
_logger = logging.getLogger(__name__)

class LabellingSheetsPrintWizard(models.TransientModel):
    _name = 'labelling.sheets.print.wizard'

    object_ids = fields.Char(
        required=True,
        readonly=True,
        default=lambda self: self._default_object_ids(),
    )

    @api.model
    def _default_object_ids(self):
        return ','.join(map(str, self.env.context['active_ids']))

    content_template_id = fields.Many2one(
        comodel_name='labelling.content.template',
        required=True,
        string="Content Template",
        help="This defines what goes on each label.",
    )

    spec_id = fields.Many2one(
        comodel_name='labelling.sheets.spec',
        required=True,
        string="Sheet Specification",
        help="This defines how the labels are laid out on the page",
    )

    print_borders = fields.Boolean(
        help="Prints black borders around the labels.  Useful for previewing and testing.",
    )

    number_of_copies = fields.Integer(
        default=1,
        required=True,
        help="Each label will be repeated this number of times in succession.",
    )

    def get_print_options(self):
        return {'number_of_copies': self.number_of_copies}

    @api.multi
    def print_pdf(self):
        self.ensure_one()
        _logger.info("Context: {}".format(self.env.context))
        return self.env['report'].get_action(self, 'labelling_sheets.label_pdf_report')
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

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
import labels

class LabellingSheetsPaperSpec(models.Model):
    _name = 'labelling.sheets.spec'

    name = fields.Char(required=True, unique=True)
    
    sheet_width = fields.Float(required=True)
    sheet_height  = fields.Float(required=True)
    label_width = fields.Float(required=True)
    label_height = fields.Float(required=True)
    label_corner_radius = fields.Float(required=True)
    label_left_padding = fields.Float(required=True, default=0)
    label_right_padding = fields.Float(required=True, default=0)
    label_top_padding = fields.Float(required=True, default=0)
    label_bottom_padding = fields.Float(required=True, default=0)
    column_gap = fields.Float(required=True)
    row_gap = fields.Float(required=True)
    num_columns = fields.Integer(required=True)
    num_rows = fields.Integer(required=True)

    def get_specification(self):
        """Return the labels.Specification for this spec.
        """
        self.ensure_one()
        return labels.Specification(
            self.sheet_width,
            self.sheet_height,
            self.num_columns,
            self.num_rows,
            self.label_width,
            self.label_height,
            corner_radius=self.label_corner_radius,
            column_gap=self.column_gap,
            row_gap=self.row_gap,
            left_padding=self.label_left_padding,
            right_padding=self.label_right_padding,
            top_padding=self.label_top_padding,
            bottom_padding=self.label_bottom_padding,
        )

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

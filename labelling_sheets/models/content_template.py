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

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import labels

class LabellingContentRenderer(models.AbstractModel):
    _name = 'labelling.content.renderer'

    @api.model
    def populate_sheet(self, sheet, objects):
        """Populate sheet with objects.

        sheet: A labels.Sheet object
        objects: A recordset of objects

        The default implementation sends each object from objects
        in turn to the sheet's drawing_callable, which will
        be render_label unless you've overriden get_pdf
        on labelling.content.template to do something else.

        No return value expected.

        You might want to override this if, for example, you
        want to generate labels for all child objects instead of the
        objects themselves.

        e.g. sheet.add_labels(objects.mapped('lines'))
        """
        sheet.add_labels(objects)

    @api.model
    def render_label(self, label, width, height, obj):
        """ABSTRACT: Renders obj onto the label.

        You should override this method.

        The bound version of this method works as the drawing_callable
        passed into a Sheet constructor.

        label: The label object - you should draw reportlab objects
               onto this.
        width: The width (in points) you have available
        height: The height (in points) you have available
        obj: The object's browse record you're working with.

        """
        raise NotImplementedError("Override render_label")


class LabellingContentTemplate(models.Model):
    _name = 'labelling.content.template'

    name = fields.Char(
        required=True,
        unique=True,
    )

    model_id = fields.Many2one(
        comodel_name="ir.model",
        string="Model",
        required=True,
    )

    renderer_model_id = fields.Many2one(
        comodel_name="ir.model",
        string="Renderer Model",
        required=True,
        help="The model defining what should go on each label",
    )

    @api.multi
    def get_objects(self, ids):
        """Return the objects to be reported on given integer ids.

        They are retrieved from the model selected in model_id.
        """
        self.ensure_one()
        return self.env[self.model_id.model].browse(ids)

    @api.multi
    def get_pdf(self, spec, objects, border=False):
        """Return PDF data for labels of objects.

        spec: A labels.Specification object describing the sheets
        objects: A recordset of objects to report on
        border: Whether to print borders on the sheets
        """
        self.ensure_one()

        renderer = self.get_renderer()

        sheet = labels.Sheet(spec,
                             renderer.render_label,
                             border=border)
        renderer.populate_sheet(sheet, objects)
        pdfbuf = StringIO()
        sheet.save(pdfbuf)
        pdf = pdfbuf.getvalue()
        return pdf

    @api.multi
    def get_renderer(self):
        return self.env[self.renderer_model_id.model]


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

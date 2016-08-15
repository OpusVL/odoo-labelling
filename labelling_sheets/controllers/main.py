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

from openerp.addons.web.http import Controller, route, request

from openerp.addons.web.controllers.main import _serialize_exception, content_disposition


import labels
from reportlab.graphics import shapes

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import os
    
import logging
_logger = logging.getLogger(__name__)

class LabelsController(Controller):
    @route('/labelling/sheet/pdf/download/<wizard_id>', type='http', auth='user')
    def labels_download(self, wizard_id):
        cr, uid, context = request.cr, request.uid, request.context

        wizard_model = request.registry['labelling.sheets.print.wizard']
        wizard = wizard_model.browse(cr, uid, int(wizard_id), context=context)


        specs = wizard.spec_id.get_specification()

        # Create a function to draw each label. This will be given the ReportLab drawing
        # object to draw on, the dimensions (NB. these will be in points, the unit
        # ReportLab uses) of the label, and the object to render.
        def draw_label(label, width, height, obj):
            # Just convert the object to a string and print this at the bottom left of
            # the label.
            label.add(shapes.String(2, 2, str(obj), fontName="Helvetica", fontSize=40))

        # Create the sheet.
        sheet = labels.Sheet(specs, draw_label, border=wizard.print_borders)

        # Add a couple of labels.
        sheet.add_label("Hello")
        sheet.add_label("World")

        # We can also add each item from an iterable.
        sheet.add_labels(range(3, 22))

        # Note that any oversize label is automatically trimmed to prevent it messing up
        # other labels.
        sheet.add_label("Oversized label here")

        pdfbuf = StringIO()
        sheet.save(pdfbuf)
        pdf = pdfbuf.getvalue()
        pdfhttpheaders = [
            ('Content-Type', 'application/pdf'),
            ('Content-Length', len(pdf)),
            ('Content-Disposition', content_disposition("labels.pdf")),
        ]
        # This is to assist with debugging
        dump_dir = os.getenv('ODOO_LABELLING_DUMP_DIR')
        if dump_dir:
            dump_filepath = os.path.join(dump_dir, 'labels.pdf')
            with open(dump_filepath, 'wb') as df:
                df.write(pdf)
            _logger.info('Dumped labels to {}'.format(dump_filepath))
        return request.make_response(pdf, headers=pdfhttpheaders)




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

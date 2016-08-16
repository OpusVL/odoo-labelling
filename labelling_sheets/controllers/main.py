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


        spec = wizard.spec_id.get_specification()

        template = wizard.content_template_id

        ids_str = wizard.object_ids
        obj_ids = map(int, ids_str.split(',')) if ids_str else []
        objects = template.get_objects(obj_ids)
        pdf = template.get_pdf(spec, objects, border=wizard.print_borders, print_options=wizard.get_print_options())

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

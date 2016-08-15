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


{
    'name': 'Print on labelling sheets',
    'version': '0.1',
    'author': 'OpusVL',
    'website': 'http://opusvl.com/',
    'summary': 'Print data on labelling sheets',
    
    'category': 'Reporting',
    
    'description': """Print data on labelling sheets,
""",
    'images': [
    ],
    'depends': [
        'web',
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'reports/labels_pdf_controller.xml',
        'views/pdf_print_wizard.xml',
        'views/specs.xml',
        'views/content_template.xml',
        'views/menus.xml',
        'data/sheet_specs.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

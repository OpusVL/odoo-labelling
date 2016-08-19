# -*- coding: utf-8 -*-

##############################################################################
#
# Labelling Sheets with Simple Lines
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
    'name': 'Labelling Sheets with Simple Lines',
    'version': '0.1',
    'author': 'OpusVL',
    'website': 'http://opusvl.com/',
    'summary': 'A renderer plugin for Labelling Sheets that writes a series of text fields, line by line, to the label',
    
    'category': 'Reporting',
    
    'description': """A renderer plugin for Labelling Sheets that writes a series of text fields, line by line, to the label,
""",
    'images': [
    ],
    'depends': [
        'labelling_sheets',
    ],
    'data': [
        'data/plugin.xml',
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

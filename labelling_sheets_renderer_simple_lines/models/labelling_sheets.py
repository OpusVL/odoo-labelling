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

from openerp import models, fields, api

from openerp.addons.labelling_sheets.util import LineWriter

from openerp.tools.safe_eval import safe_eval


class LabellingContentRendererPluginSimpleLines(models.AbstractModel):
    _name = 'labelling.content.renderer.plugin.simple_lines'
    _inherit = 'labelling.content.renderer.base_plugin'

    @api.model
    def objects_for_labels(self, objects, template_config, print_options):
        """Return objects mapped with 'mapped' field if provided in template_config.
        """
        template_config = template_config or {}
        mapspec = template_config.get('mapped')
        if mapspec:
            return objects.mapped(mapspec)
        return mapped
            
    @api.model
    def render_label(self, label, width, height, line, template_config):
        tconf = template_config or {}
        lw = LineWriter(label, 2, width, height,
                        font_name=tconf.get('font_name', 'Helvetica'),
                        base_font_size=tconf.get('font_size', 12),
                        pad_extra=tconf.get('line_gap', 6))
        for expr in template_config['lines']:
            lw.write_line(safe_eval(expr, {'o': line}, {}))
    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

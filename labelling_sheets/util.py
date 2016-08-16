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

from reportlab.graphics import shapes

from reportlab.pdfbase.pdfmetrics import stringWidth

class LineWriter(object):
    """Simple wrapper class for writing a series of lines to a label
    top to bottom.
    """
    def __init__(self, label, x, width, height, font_name, base_font_size, pad_extra):
        """
        label: The label object
        x: The x position to position the left hand side of each line
        width: The available width of the label in points
        height: The available height of the label in points
        font_name: The name of the font to use.
        base_font_size: The largest font size to use.  This size will be reduced to fit in long lines.
        pad_extra: Extra padding, in points, to place between labels.
        """
        self.label = label
        self.width = width
        self.x = x
        self.y = height
        self.font_name = font_name
        self.pad_extra = pad_extra
        self.base_font_size = base_font_size

    def write_line(self, text):
        """Write a line of text.

        Each call to this will place a new line base_font_size + pad_extra
        points further down the label.
        """
        font_size = squeeze_in(text, self.width, self.font_name, self.base_font_size)
        self.y -= (self.base_font_size + self.pad_extra)
        self.label.add(
            shapes.String(self.x, self.y, text,
                          fontName=self.font_name, fontSize=font_size))
    
def squeeze_in(astr, width, font_name, base_font_size):
    """Return font size needed to squeeze astr into width.

    width and base_font_size must be in points.
    """
    font_size = base_font_size
    str_width = stringWidth(astr, font_name, font_size)
    while str_width > width:
        font_size *= 0.8
        str_width = stringWidth(astr, font_name, font_size)
    return font_size


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

# Print on Labelling Sheets
## Purpose

Provides an action 'More -> Print Sheet Labels' which will allow you to print
labels for one or more objects from the Odoo GUI.

This uses the pyLabels module to lay your labels out on a page.

All you need to do is provide code to draw on each label.

The layout of the label sheets is configurable in the database.

The system is designed to be extensible with renderers, so you can
draw on your labels anything supported by reportlab (assuming it will
physically fit on one of the labels) by writing code in an
Odoo addon.

## Limitations

* There is not currently a renderer that takes options from the database,
so you need to hard-code your per-label printing logic in a model.
However, with some extra development work it should be possible to write
a plugin that takes parameters from your template object, defining which fields
to render and which fonts you wish to use.


# Copyright and License

Copyright (C) 2016 OpusVL

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

If you require assistance, support, or further development of this
software, please contact OpusVL using the details below:

Telephone: +44 (0)1788 298 410
Email: community@opusvl.com
Web: http://opusvl.com

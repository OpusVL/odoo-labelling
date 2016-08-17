
openerp.labelling_sheets = function(session) {
    var _t = session.web._t;
    session.web.Sidebar = session.web.Sidebar.extend({
        start: function() {
            var self = this;
            this._super(this);
            var Actions = new openerp.Model('ir.actions.act_window');
            Actions.call(
                'for_xml_id',
                ['labelling_sheets', 'action_sheets_print_wizard']
            ).done(function (action) {
                self.add_items('other', [{
                    label: _t('Print Sheet Labels'),
                    'action': action,
                }]);
            });
        }
    });
};

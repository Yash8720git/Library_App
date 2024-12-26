frappe.ui.form.on('Book Transaction', {
    status: function(frm) {
        // Show Return Date field only when status is "Return"
        frm.toggle_display('return_date', frm.doc.status === 'Return');
    },
    refresh: function(frm) {
        // Ensure Return Date visibility on form load
        frm.trigger('status');
    }
});

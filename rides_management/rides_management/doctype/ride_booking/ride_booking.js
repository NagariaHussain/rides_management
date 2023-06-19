// Copyright (c) 2023, Hussain and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Booking", {
  refresh(frm) {
    frm.add_custom_button("Create Ride", () => {
      let dialog = new frappe.ui.Dialog({
        title: "Select Driver",
        fields: [
          {
            fieldtype: "Link",
            fieldname: "driver",
            label: "Driver",
            options: "Driver",
          },
        ],
        primary_action_label: "Create Ride",
        primary_action: (data) => {
          console.log(data);
          let { driver } = data;

          frappe.new_doc("Ride", {
            vehicle: frm.doc.vehicle,
            driver: driver,
            ride_booking: frm.doc.name,
          });
        },
      });

      dialog.show();
    });
  },
});

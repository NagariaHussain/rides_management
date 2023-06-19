frappe
  .call({
    method: "frappe.client.get_list",
    args: {
      doctype: "Vehicle",
    },
  })
  .then((response) => {
    console.log(response);
  });

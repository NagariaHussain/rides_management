# Copyright (c) 2023, Hussain and contributors
# For license information, please see license.txt

import frappe

from frappe.query_builder.functions import Sum


def execute(filters=None):
	columns, data = [
		{
			"label": "Make",
			"fieldname": "make",
			"fieldtype": "Data",
			"width": 230,
		},
		{"label": "Revenue", "fieldname": "revenue", "fieldtype": "float", "width": 200},
	], []

	ride = frappe.qb.DocType("Ride")
	vehicle = frappe.qb.DocType("Vehicle")

	data = frappe.qb.from_(ride).left_join(vehicle).on(ride.vehicle == vehicle.name).groupby(
		vehicle.make
	).select(vehicle.make, Sum(ride.total_amount).as_("revenue")).run(as_dict=True)

	chart = {
		"data": {
			"labels": [d.make for d in data],
			"datasets": [{"name": "Revenue by Make", "values": [d.revenue for d in data]}],
		},
		"type": "pie",
	}

	return columns, data, None, chart, None

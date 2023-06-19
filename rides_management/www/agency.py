import frappe


def get_context(context):
	vehicles = frappe.get_list(
		"Vehicle",
		filters={"is_published": 1},
		fields=["name", "make", "model", "vehicle_image"],
		order_by="make desc"
	)
	context.vehicles = vehicles

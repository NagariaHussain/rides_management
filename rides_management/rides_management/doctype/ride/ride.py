# Copyright (c) 2023, Hussain and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Ride(Document):
	def before_save(self):
		cost_breakup = self.cost_breakup

		total_hours = 0
		for item in cost_breakup:
			total_hours += item.hours
		
		self.total_hours = total_hours

		self.total_amount = self.total_hours * self.rate_per_hours


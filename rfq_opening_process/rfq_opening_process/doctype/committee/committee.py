# Copyright (c) 2022, Navari Limited and contributors
# For license information, please see license.txt

import frappe
from frappe import _, throw
from frappe.utils import cint
from frappe.model.document import Document


class Committee(Document):

    def validate(self):
        if (
            not cint(self.opening_minutes)
            and not cint(self.committee_register)
            and not cint(self.evaluation_minutes)
            and not cint(self.disabled)
        ):
            throw(_("At least one of the Applicable Templates should be selected"))

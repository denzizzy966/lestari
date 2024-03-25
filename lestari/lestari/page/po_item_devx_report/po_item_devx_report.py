# Copyright (c) 2021, Patrick Stuhlmüller and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def contoh_report():
    po = []
    list_doc = frappe.get_list("Purchase Order")
    no = 0
    for row in list_doc:
        doc = frappe.get_doc("Purchase Order", row)
        for col in doc.items:
            no+=1
            baris_baris = {
                'no' : no,
                'item_code' : col.item_code,
                'item_name' : col.item_name,
                'description' : col.description,
                'per_qty' : col.qty,
                'per_uom' : col.uom,
                'item_group' : frappe.db.get_value("Item", col.item_code, "item_group"),
                'rate': col.rate,
                'amount' : col.amount,
                'warehouse': col.warehouse,
                'name' : doc.name,
                'Transaction_Date' : frappe.format(doc.transaction_date,{'fieldtype':'Date'}),
                'Schedule_Date' : frappe.format(doc.schedule_date,{'fieldtype':'Date'}),
                'pajak' : doc.pajak,
                'ppn' : doc.ppn,
                'No_Faktur' : doc.no_faktur,
                'Supplier' : doc.supplier,
                'Total_Qty' : doc.total_qty,
                'Mata_Uang' : doc.currency,
                # 'total' : frappe.utils.fmt_money(doc.total,currency=frappe.db.get_value("Currency",doc.currency,"Symbol")),
                'Total' : doc.total,
                'Status' : doc.status
            }
            po.append(baris_baris)
    # frappe.msgprint(str(po))  
    return po   
import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class BookTransaction(Document):
    def before_save(self):
        # Handle book status and return date based on transaction type

        # Fetch the linked book document
        book = frappe.get_doc("Books", self.books)

        if self.status == "Issue":
            if book.status == "Available":
                # Update book status to "Issued"
                book.status = "Issued"
                book.save()
            else:
                frappe.throw(f"The book '{book.title}' is already issued.")

        elif self.status == "Return":
            # Automatically fill the return date if not provided
            if not self.return_date:
                self.return_date = nowdate()

            if book.status == "Issued":
                # Update book status to "Available"
                book.status = "Available"
                book.save()
            else:
                frappe.throw(f"The book '{book.title}' is not currently issued.")

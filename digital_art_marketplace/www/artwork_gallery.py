import frappe

def get_context(context):
    context.artworks = frappe.get_all("Artwork", fields=["title", "artist", "price"])
    return context

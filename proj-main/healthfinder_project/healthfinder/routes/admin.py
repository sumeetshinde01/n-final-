from flask import Blueprint, render_template, request

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin/medicine_availability', methods=['GET', 'POST'])
def medicine_availability():
    medicine_name = request.form.get('medicine_name', '')
    results = []
    if medicine_name:
        results = [
            {'pharmacy_name': 'City Pharmacy', 'quantity': 10},
            {'pharmacy_name': 'Local Pharmacy', 'quantity': 5},
        ]
    return render_template('admin_medicine_availability.html', results=results, medicine_name=medicine_name)

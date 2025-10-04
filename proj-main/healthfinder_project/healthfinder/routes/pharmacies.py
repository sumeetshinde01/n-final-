from flask import Blueprint, render_template
from flask_login import login_required

pharmacies_bp = Blueprint('pharmacies', __name__)

@pharmacies_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('pharmacy_dashboard.html')

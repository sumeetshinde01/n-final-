from flask import Blueprint, render_template
from flask import request, redirect, url_for
from flask import Blueprint, render_template, request

users_bp = Blueprint('users_bp', __name__)
admin_bp = Blueprint('admin', __name__)

@users_bp.route('/')
def index():
    return render_template('index.html')


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Add your authentication logic here.
        # If admin credentials are correct:
        return redirect(url_for('users_bp.admin_dashboard'))  # Redirect after login
    return render_template('login.html')

@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Registration logic here (save user etc.)
        return redirect(url_for('users_bp.login'))  # Redirect to login after registration
    return render_template('register.html')


@users_bp.route('/results')
def results():
    return render_template('results.html')

@users_bp.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')
    
@admin_bp.route('/admin/medicine_availability', methods=['GET', 'POST'])
def medicine_availability():
    medicine_name = request.form.get('medicine_name', '')
    results = []
    # Your DB querying logic here, if implemented
    return render_template('admin_medicine_availability.html', results=results, medicine_name=medicine_name)
    
from flask import Blueprint, render_template

hospitals_bp = Blueprint('hospitals', __name__)

@hospitals_bp.route('/hospitals')
def hospitals():
    return render_template('hospitals.html')

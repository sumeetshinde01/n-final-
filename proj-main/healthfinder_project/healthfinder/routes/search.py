from flask import Blueprint, render_template, request
from flask import Blueprint, render_template, request, jsonify
from healthfinder.models import Hospital, Pharmacy, Medicine

search_bp = Blueprint('search', __name__)

# Removing this route as it conflicts with the one in medicines.py
# @search_bp.route('/medicines')
# def medicines():
#     # Optionally fetch medicine data here
#     return render_template('medicines.html')

@search_bp.route('/')
def search():
    query = request.args.get('query', '')
    # Search for hospitals
    hospitals = Hospital.query.filter(Hospital.name.ilike(f"%{query}%")).all()
    
    # Search for pharmacies
    pharmacies = Pharmacy.query.filter(Pharmacy.name.ilike(f"%{query}%")).all()
    
    return render_template('search_results.html', 
                           query=query, 
                           hospitals=hospitals, 
                           pharmacies=pharmacies)
from flask import Blueprint, render_template

search_bp = Blueprint('search', __name__)


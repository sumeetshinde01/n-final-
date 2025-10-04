from flask import Blueprint, render_template, current_app, request
from healthfinder.models import Medicine, db

medicines_bp = Blueprint("medicines", __name__)

@medicines_bp.route("/medicines")
def medicines():
    # Get page number from query parameters, default to 1
    page = request.args.get('page', 1, type=int)
    per_page = 260  # Increased number of medicines per page
    
    # Get search query if provided
    search_query = request.args.get('query', '')
    
    # Check if we have medicines in the database
    medicine_count = Medicine.query.count()
    
    # If no medicines, add some sample ones
    if medicine_count == 0:
        from healthfinder_project.init_db import add_sample_medicines
        add_sample_medicines()
        db.session.commit()
    
    # Create base query
    query = Medicine.query
    
    # Apply search filter if search query is provided
    if search_query:
        query = query.filter(Medicine.name.ilike(f'%{search_query}%'))
        print(f"Searching for medicines with name like: {search_query}")
    
    # Fetch medicines with pagination
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    medicines = pagination.items
    
    # Debug info
    print(f"Total medicines: {medicine_count}")
    print(f"Medicines on this page: {len(medicines)}")
    if search_query:
        print(f"Search results for '{search_query}': {len(medicines)} found")
    
    return render_template("medicines.html", medicines=medicines, pagination=pagination, search_query=search_query)

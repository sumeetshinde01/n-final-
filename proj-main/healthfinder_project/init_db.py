import csv
import os
from flask import render_template, request
from healthfinder import create_app
from healthfinder.db import db
from healthfinder.models import Medicine, Pharmacy, MedicineStock

def init_db():
    """Initialize the database with sample data."""
    app = create_app()
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Clear existing medicines and repopulate
        Medicine.query.delete()
        db.session.commit()
        print("Cleared existing medicines to repopulate the database.")
        
        # Path to the CSV file
        csv_file_path = os.path.join(os.path.dirname(__file__), 'medicines.csv')
        
        if os.path.exists(csv_file_path):
            # Import medicines from CSV file
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                count = 0
                for row in csv_reader:
                    # Convert string 'True'/'False' to boolean
                    prescription_required = row.get('prescription_required', 'False') == 'True'
                    # Convert price to float
                    try:
                        price = float(row['price'])
                    except ValueError:
                        try:
                            price = float(row['price'].replace('$', '').strip())
                        except ValueError:
                            # Set a default price if conversion fails
                            price = 0.0
                            print(f"Warning: Could not convert price '{row['price']}' for medicine '{row['name']}'. Using default price.")
                    
                    medicine = Medicine(
                        name=row['name'],
                        description=row['description'],
                        category=row['category'],
                        price=price,
                        manufacturer=row['manufacturer'],
                        prescription_required=prescription_required
                    )
                    db.session.add(medicine)
                    count += 1
                    
                    # Commit in batches to avoid memory issues
                    if count % 100 == 0:
                        db.session.commit()
                        print(f"Imported {count} medicines so far...")
                    
                    db.session.commit()
                print(f"{count} medicines added to database from CSV file!")
        else:
            # Fallback to hardcoded medicines if CSV file doesn't exist
            print("CSV file not found. Adding default medicines.")
            medicines = [
                Medicine(name="Paracetamol", description="Pain reliever and fever reducer", price=5.99, manufacturer="ABC Pharma"),
                Medicine(name="Amoxicillin", description="Antibiotic used to treat bacterial infections", price=12.50, manufacturer="XYZ Pharmaceuticals"),
                Medicine(name="Ibuprofen", description="Nonsteroidal anti-inflammatory drug", price=7.25, manufacturer="Health Solutions"),
                Medicine(name="Aspirin", description="Blood thinner and pain reliever", price=4.99, manufacturer="MediCorp"),
                Medicine(name="Loratadine", description="Antihistamine for allergy relief", price=8.75, manufacturer="AllergyRelief Inc."),
                Medicine(name="Omeprazole", description="Proton pump inhibitor for acid reflux", price=15.99, manufacturer="Digestive Health"),
                Medicine(name="Atorvastatin", description="Statin medication for cholesterol", price=22.50, manufacturer="Heart Health Inc."),
                Medicine(name="Metformin", description="Oral diabetes medication", price=9.99, manufacturer="Diabetes Care"),
                Medicine(name="Lisinopril", description="ACE inhibitor for high blood pressure", price=11.25, manufacturer="CardioMed"),
                Medicine(name="Albuterol", description="Bronchodilator for asthma", price=18.75, manufacturer="Respiratory Solutions"),
                Medicine(name="Sertraline", description="SSRI antidepressant", price=14.50, manufacturer="Mental Health Pharma"),
                Medicine(name="Levothyroxine", description="Thyroid hormone replacement", price=10.25, manufacturer="Endocrine Health"),
                Medicine(name="Simvastatin", description="Cholesterol-lowering medication", price=13.99, manufacturer="Lipid Control"),
                Medicine(name="Metoprolol", description="Beta-blocker for hypertension", price=8.50, manufacturer="Heart Care"),
                Medicine(name="Amlodipine", description="Calcium channel blocker", price=9.75, manufacturer="BP Solutions"),
            ]
            
            db.session.add_all(medicines)
            db.session.commit()
            
            print("Database initialized with sample medicines.")
        # Count and display the number of medicines in the database
        medicine_count = Medicine.query.count()
        print(f"Total medicines in database: {medicine_count}")
        print("Database initialization complete!")
        
        
if __name__ == "__main__":
    init_db()


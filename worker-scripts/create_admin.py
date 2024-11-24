import sys
import os

## connection_string = (
#        "DRIVER={ODBC Driver 17 for SQL Server};SERVER=(localdb)\\MSSQLLocalDB;DATABASE=BeerDB;Trusted_Connection=yes"
#    )
#    encoded_string = urllib.parse.quote_plus(connection_string)


# Add the 'app' directory to sys.path (relative to this script's directory)
app_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../app'))
print(f"Adding {app_dir} to sys.path")  # Debugging line to check the path
sys.path.append(app_dir)
print(sys.path)

# Import the app and db
try:
    from app import create_app, db
    from app.models import User
except ModuleNotFoundError as e:
    print(f"Error importing app: {e}")
    sys.exit(1)

def create_admin_user():
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', password='admin')  # Use the hashed password here
        db.session.add(admin)
        db.session.commit()
        print("Admin user created successfully!")
    else:
        print("Admin user already exists!")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():  # Ensure we are using the app context
        create_admin_user()

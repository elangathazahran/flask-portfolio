from app import create_app, db
from app.models import Portfolio  # Import model

app = create_app()

with app.app_context():
    db.create_all()  # Ini buat bikin semua tabel berdasarkan model

if __name__ == "__main__":
    app.run(debug=True)

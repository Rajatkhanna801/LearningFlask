# LearningFlask
Create a Book library management systemc using Flask.

# Steps to integrate PostgreSQL with flask project.
1. Install the requirements 
==> pip install Flask-SQLAlchemy psycopg2-binary
2. Create a models.py file inside application directory.
3. Import the models.py file inside app.py file.
4. Create config file to read the database credentials from .env file and import the config in app.py file.
5. Install flask migration to manage database migrations.
==> pip install Flask-Migrate
6. Run the following command to reflect changes in database
==> flask db init (create the directory of migration inside application)
==> flask db migrate ()
==> flask db upgrade (reflect changes in database)
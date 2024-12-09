from flask import Flask, render_template, request, redirect, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import ForeignKey
import pandas as pd
from werkzeug.utils import secure_filename
import os
from flask import flash

app = Flask(__name__)
app.secret_key = '5f4e3f7b123456abcd789xyz'
app.config['SECRET_KEY'] = '5f4e3f7b123456abcd789xyz'
app.config['DEBUG'] = True



# Define upload folder 
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure the folder exists before file upload
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hosteldata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Hostel Table

# Models
class Hostel(db.Model):
    __tablename__ = 'Hostel'  
    h_id = db.Column(db.Integer, primary_key=True)  
    hname = db.Column(db.String(100), nullable=True)
    warden = db.Column(db.String(100), nullable=False)
    nrooms = db.Column(db.Integer, nullable=False)
    nstudents = db.Column(db.Integer, nullable=False)
    h_type = db.Column(db.String(10), nullable=False)
    vacant_rooms = db.Column(db.Integer, nullable=False)  

    # def __repr__(self):
    #     return f'Hostel {self.h_id}: {self.hname}'



class HostelA(db.Model):
    __tablename__ = 'hostel_A'
    id = db.Column(db.Integer, primary_key=True)
    h_id = db.Column(db.Integer, ForeignKey('Hostel.h_id'), nullable=True)
    student_name = db.Column(db.String(50), nullable=True)
    roll_num = db.Column(db.String(20), nullable=True)  # Remove unique=True
    room_num = db.Column(db.Integer, nullable=True)
    floor = db.Column(db.Integer, nullable=True)
    batch = db.Column(db.String(10), nullable=True)
    branch = db.Column(db.String(50), nullable=True)


class HostelB(db.Model):
    __tablename__ = 'hostel_B'
    id = db.Column(db.Integer, primary_key=True)
    h_id = db.Column(db.Integer, ForeignKey('Hostel.h_id'), nullable=True)
    student_name = db.Column(db.String(50), nullable=True)
    roll_num = db.Column(db.String(20), nullable=True)  #remove unique constraint
    room_num = db.Column(db.Integer, nullable=True)
    floor = db.Column(db.Integer, nullable=True)
    batch = db.Column(db.String(10), nullable=True)
    branch = db.Column(db.String(50), nullable=True)

class HostelC(db.Model):
    __tablename__ = 'hostel_C'
    id = db.Column(db.Integer, primary_key=True)
    h_id = db.Column(db.Integer, ForeignKey('Hostel.h_id'), nullable=True)
    student_name = db.Column(db.String(50), nullable=True)
    roll_num = db.Column(db.String(20), nullable=True)
    room_num = db.Column(db.Integer, nullable=True)
    floor = db.Column(db.Integer, nullable=True)
    batch = db.Column(db.String(10), nullable=True)
    branch = db.Column(db.String(50), nullable=True)

class HostelD(db.Model):
    __tablename__ = 'hostel_D'
    id = db.Column(db.Integer, primary_key=True)
    h_id = db.Column(db.Integer, ForeignKey('Hostel.h_id'), nullable=True)
    student_name = db.Column(db.String(50), nullable=True)
    roll_num = db.Column(db.String(20), nullable=True)
    room_num = db.Column(db.Integer, nullable=True)
    floor = db.Column(db.Integer, nullable=True)
    batch = db.Column(db.String(10), nullable=True)
    branch = db.Column(db.String(50), nullable=True)

class HostelE(db.Model):
    __tablename__ = 'hostel_E'
    id = db.Column(db.Integer, primary_key=True)
    h_id = db.Column(db.Integer, ForeignKey('Hostel.h_id'), nullable=True)
    student_name = db.Column(db.String(50), nullable=True)
    roll_num = db.Column(db.String(20), nullable=True)
    room_num = db.Column(db.Integer, nullable=True)
    check_in_date = db.Column(db.Date, nullable=True)  
    check_out_date = db.Column(db.Date, nullable=True)  # Nullable date

class HostelF(db.Model):
    __tablename__ = 'hostel_F'
    id = db.Column(db.Integer, primary_key=True)
    h_id = db.Column(db.Integer, ForeignKey('Hostel.h_id'), nullable=False)
    student_name = db.Column(db.String(50), nullable=True)
    roll_num = db.Column(db.String(20),nullable=True)
    room_num = db.Column(db.Integer, nullable=True)
    floor = db.Column(db.Integer, nullable=True)
    batch = db.Column(db.String(10), nullable=True)
    branch = db.Column(db.String(50), nullable=True)




@app.before_request
def add_data():
    # Check if data already exists to avoid duplicates
    if Hostel.query.count() == 0:
        # Data for Hostel A to Hostel F with 240 rooms each
        hostels_data = [
            {
                'h_id': 1,
                'hname': 'Hostel A',
                'warden': 'Mr. Smith',
                'nrooms': 240,  # Updated number of rooms
                'nstudents': 45,
                'h_type': 'A',
                'vacant_rooms': 5
            },
            {
                'h_id': 2,
                'hname': 'Hostel B',
                'warden': 'Ms. Johnson',
                'nrooms': 240,  # Updated number of rooms
                'nstudents': 55,
                'h_type': 'B',
                'vacant_rooms': 5
            },
            {
                'h_id': 3,
                'hname': 'Hostel C',
                'warden': 'Dr. Roberts',
                'nrooms': 240,  # Updated number of rooms
                'nstudents': 65,
                'h_type': 'C',
                'vacant_rooms': 5
            },
            {
                'h_id': 4,
                'hname': 'Hostel D',
                'warden': 'Mr. White',
                'nrooms': 240,  # Updated number of rooms
                'nstudents': 75,
                'h_type': 'D',
                'vacant_rooms': 5
            },
            {
                'h_id': 5,
                'hname': 'Hostel E',
                'warden': 'Ms. Brown',
                'nrooms': 240,  # Updated number of rooms
                'nstudents': 85,
                'h_type': 'E',
                'vacant_rooms': 5
            },
            {
                'h_id': 6,
                'hname': 'Hostel F',
                'warden': 'Dr. Green',
                'nrooms': 240,  # Updated number of rooms
                'nstudents': 95,
                'h_type': 'F',
                'vacant_rooms': 5
            }
        ]

        # Loop through the data and create hostel objects
        for hostel_data in hostels_data:
            hostel = Hostel(
                h_id=hostel_data['h_id'],
                hname=hostel_data['hname'],
                warden=hostel_data['warden'],
                nrooms=hostel_data['nrooms'],
                nstudents=hostel_data['nstudents'],
                h_type=hostel_data['h_type'],
                vacant_rooms=hostel_data['vacant_rooms']
            )

            # Add the data to the session
            db.session.add(hostel)

        # Commit the changes to the database
        db.session.commit()


# Function to create the database
def create_db():
    with app.app_context():
        db.create_all()


# Views
@app.route('/', methods=['GET'])
def index():
    # Just render the page with the form, no POST handling here anymore
    hostels = Hostel.query.all()  # Fetching all hostels
    return render_template("index.html", hostels=hostels)


#FUNCTION TO ALLOCATE ROOMS TO STUDENTS

@app.route('/allocate_rooms', methods=['POST'])
def allocate_rooms():
    file = request.files.get('csv_file')

    # Check if the file exists and is a valid CSV
    if not file or not file.filename.endswith('.csv'):
        flash("Invalid file format. Please upload a CSV file.", "error")
        return redirect('/')
    
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Parse the CSV using pandas
    try:
        data = pd.read_csv(file_path)
        expected_columns = {'id', 'name', 'roll', 'batch', 'branch', 'hostel_id', 'room_number'}
        if not expected_columns.issubset(set(data.columns)):
            flash("CSV file is missing required columns.", "error")
            return redirect('/')
        
        for _, row in data.iterrows():
            hostel_id = row.get('hostel_id')
            hostel_table = None

            # Determine which hostel table to use based on hostel_id
            if hostel_id == 1:
                hostel_table = HostelA
            elif hostel_id == 2:
                hostel_table = HostelB
            elif hostel_id == 3:
                hostel_table = HostelC
            elif hostel_id == 4:
                hostel_table = HostelD
            elif hostel_id == 5:
                hostel_table = HostelE
            else:
                hostel_table = HostelF

            if hostel_table:
                # Check if the student name is null
                student_name = row['name']
                if student_name == 'null':
                    student_entry = hostel_table.query.filter_by(room_num=row['room_number']).first()
                    if student_entry:
                        # Mark room as vacant
                        student_entry.student_name = 'null'
                        student_entry.batch = None
                        student_entry.branch = None
                        student_entry.roll_num = None
                    else:
                        # Create a new vacant room entry
                        student_entry = hostel_table(
                            h_id=hostel_id,
                            student_name='null',
                            roll_num=None,
                            room_num=row['room_number'],
                            floor=(row['room_number'] // 100),
                            batch=None,
                            branch=None
                        )
                        db.session.add(student_entry)
                else:
                    # Add or update a room allocation
                    student_entry = hostel_table(
                        h_id=hostel_id,
                        student_name=student_name,
                        roll_num=row['roll'],
                        room_num=row['room_number'],
                        floor=(row['room_number'] // 100),
                        batch=row['batch'],
                        branch=row['branch']
                    )
                    db.session.add(student_entry)

        db.session.commit()
        flash("Rooms allocated successfully!", "success")
        return redirect('/')

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect('/')
       





# MANUAL ROOM ALLOCATION OF VACANT ROOM 

@app.route('/allocate-room', methods=['POST'])
def allocate_room():
    hostel_id = request.form.get('hostel_id')  # Get the hostel ID from the user input
    room_number = request.form.get('room_number')
    student_name = request.form.get('student_name')
    batch = request.form.get('batch')
    branch = request.form.get('branch')
    roll_num = request.form.get('roll_num')

    # Determine which hostel table to use based on hostel_id
    hostel_table = None
    if hostel_id == '1':  # Ensure hostel_id is a string or cast as needed
        hostel_table = HostelA
    elif hostel_id == '2':
        hostel_table = HostelB
    elif hostel_id == '3':
        hostel_table = HostelC
    elif hostel_id == '4':
        hostel_table = HostelD
    elif hostel_id == '5':
        hostel_table = HostelE
    elif hostel_id == '6':  
        hostel_table = HostelF

    # Check if the hostel table is valid
    if hostel_table:


        # Update the room allocation only for vacant rooms
        room = hostel_table.query.filter_by(room_num=room_number, student_name=None).first()
        if room:
            room.student_name = student_name
            room.batch = batch
            room.branch = branch
            room.roll_num = roll_num
            db.session.commit()
            flash(f"Room {room_number} successfully allocated to {student_name}!", "success")
        else:
            flash(f"Room {room_number} is not vacant or does not exist.", "error")

    else:
        flash("Invalid hostel ID provided.", "error")

    return redirect('/')

@app.route('/deallocate-rooms', methods=['POST'])
def deallocate_rooms():
    hostel_id = request.form.get('hostel_id')  # Get the hostel ID from user input
    batch = request.form.get('batch')  # Get the batch to deallocate

    # Determine which hostel table to use based on hostel_id
    hostel_table = None
    if hostel_id == '1':
        hostel_table = HostelA
    elif hostel_id == '2':
        hostel_table = HostelB
    elif hostel_id == '3':
        hostel_table = HostelC
    elif hostel_id == '4':
        hostel_table = HostelD
    elif hostel_id == '5':
        hostel_table = HostelE
    elif hostel_id == '6':
        hostel_table = HostelF

    # Check if the hostel table is valid
    if hostel_table:
        # Find all rooms assigned to the given batch and deallocate them
        rooms_to_deallocate = hostel_table.query.filter_by(batch=batch).all()

        if rooms_to_deallocate:
            for room in rooms_to_deallocate:
                room.student_name = None
                room.batch = None
                room.branch = None
                room.roll_num = None
            db.session.commit()
            flash(f"All rooms for batch {batch} in Hostel {hostel_id} have been deallocated.", "success")
        else:
            flash(f"No rooms found for batch {batch} in Hostel {hostel_id}.", "error")
    else:
        flash("Invalid hostel ID provided.", "error")

    return redirect('/')



@app.route('/search-room', methods=['GET', 'POST'])
def search_room():
    if request.method == 'POST':
        # Get the search type, value, and hostel ID from the form
        search_type = request.form.get('search_type')
        search_value = request.form.get('search_value')
        hostel_id = request.form.get('hostel_id')

        # Determine which hostel table to query based on hostel_id
        hostel_table = None
        if hostel_id == '1':
            hostel_table = HostelA
        elif hostel_id == '2':
            hostel_table = HostelB
        elif hostel_id == '3':
            hostel_table = HostelC
        elif hostel_id == '4':
            hostel_table = HostelD
        elif hostel_id == '5':
            hostel_table = HostelE
        elif hostel_id == '6':
            hostel_table = HostelF
        else:
            flash("Invalid hostel ID provided!", "error")
            return redirect('/search-room')

        # Determine the filter condition based on the search type
        if search_type == 'name':
            result = hostel_table.query.filter_by(student_name=search_value).first()
        elif search_type == 'roll':
            result = hostel_table.query.filter_by(roll_num=search_value).first()
        else:
            flash("Invalid search type selected!", "error")
            return redirect('/search-room')

        # Check if a room was found
        if result:
            room_details = {
                "hostel_name": hostel_table.__tablename__,
                "room_number": result.room_num,
                "student_name": result.student_name,
                "batch": result.batch,
                "branch": result.branch,
                "roll_num": result.roll_num,
            }
            return render_template('room_grid.html', room_details=room_details)
        else:
            flash(f"No room found for {search_type}: {search_value} in Hostel ID {hostel_id}.", "error")
            return redirect('/search-room')




from datetime import date

@app.route('/allocate_room_e', methods=['POST'])
def allocate_room_e():
    try:
        room_number = request.form.get('room_number')
        student_name = request.form.get('student_name')
        roll_num = request.form.get('roll_num')
        check_in_date = request.form.get('check_in_date')
        check_out_date = request.form.get('check_out_date')
        today = date.today()

        # Convert string dates to Python date objects
        from datetime import datetime
        check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d').date()

        # Query for room availability dynamically
        expired_rooms = HostelE.query.filter(HostelE.check_out_date < today).all()
        for room in expired_rooms:
            room.student_name = None
            room.roll_num = None
            room.check_in_date = None
            room.check_out_date = None
        db.session.commit()

        room = HostelE.query.filter_by(room_num=room_number, student_name=None).first()

        if room:
            # Update the room allocation
            room.student_name = student_name
            room.roll_num = roll_num
            room.check_in_date = check_in_date
            room.check_out_date = check_out_date
            db.session.commit()
            flash(f"Room {room_number} successfully allocated to {student_name}!", "success")
        else:
            flash(f"Room {room_number} is not vacant or does not exist in Hostel E.", "error")

    except Exception as e:
        # Handle unexpected errors
        flash(f"An error occurred while allocating the room: {str(e)}", "error")

    return redirect('/')



    
@app.route('/student-details/<room_num>')
def student_details(room_num):
    student = HostelE.query.filter_by(room_num=room_num).first()
    if student:
        return render_template('studentdetails.html', student=student)
    else:
        flash("No details found for this room.", "error")
        return redirect('/')



@app.route('/hostels.html')
def show_hostels():
    hostels = Hostel.query.all()
    return render_template("hostels.html", hostels=hostels)

@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/hostel2.html')
def hostel_b():
    
    hostel_b_data = HostelB.query.all()
    # Calculating room statistics
    total_rooms = len(hostel_b_data)  # Total number of rooms
    occupied_rooms = sum(1 for room in hostel_b_data if room.student_name is not None)  # Occupied rooms
    vacant_rooms = total_rooms - occupied_rooms  # Vacant rooms
    
    
    return render_template("hostel2.html", hostel_b_data=hostel_b_data,total_rooms=total_rooms,
        vacant_rooms=vacant_rooms,
        occupied_rooms=occupied_rooms )


@app.route('/hostel3.html')
def hostel_c():
    
    hostel_c_data = HostelC.query.all()
    
    return render_template("hostel3.html", hostel_c_data=hostel_c_data)



@app.route('/hostel4.html')
def hostel_d():
    
    hostel_d_data = HostelD.query.all()
    
    return render_template("hostel4.html", hostel_d_data=hostel_d_data)




@app.route('/hostel5.html')
def hostel5():
    hostel_e_data = HostelE.query.all()

    # Calculating room statistics
    total_rooms = len(hostel_e_data)  # Total number of rooms
    occupied_rooms = sum(1 for room in hostel_e_data if room.student_name is not None)  # Occupied rooms
    vacant_rooms = total_rooms - occupied_rooms  # Vacant rooms

    return render_template(
        "hostel5.html",
        hostel_e_data=hostel_e_data,
        total_rooms=total_rooms,
        vacant_rooms=vacant_rooms,
        occupied_rooms=occupied_rooms
    )


@app.route('/hostel6.html')
def hostel6():

    hostel_f_data = HostelF.query.all()
    total_rooms = len(hostel_f_data)  # Total number of rooms
    occupied_rooms = sum(1 for room in hostel_f_data if room.student_name is not None)  # Occupied rooms
    vacant_rooms = total_rooms - occupied_rooms  # Vacant rooms

    return render_template("hostel6.html", hostel_f_data=hostel_f_data, total_rooms=total_rooms,
        vacant_rooms=vacant_rooms,
        occupied_rooms=occupied_rooms)


@app.route('/contact.html')
def contact():

    return render_template('contact.html')

@app.route('/hostel1.html')
def hostel_a():

    hostel_a_data = HostelA.query.all()
    # Calculating room statistics
    total_rooms = len(hostel_a_data)  # Total number of rooms
    occupied_rooms = sum(1 for room in hostel_a_data if room.student_name is not None)  # Occupied rooms
    vacant_rooms = total_rooms - occupied_rooms  # Vacant rooms
    
    return render_template("hostel1.html", hostel_a_data=hostel_a_data,total_rooms=total_rooms,
        vacant_rooms=vacant_rooms,
        occupied_rooms=occupied_rooms)

@app.route('/index.html')
def homepage():

    return render_template("index.html")




# Run the application
if __name__ == "__main__":
    create_db()  # Create the database tables
    app.run(debug=True)




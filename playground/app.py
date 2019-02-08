from flask import Flask, render_template



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/roster/<string:grade_view>")
def roster(grade_view):
    s1 = ('Sophomore','Richard', 'A')
    s2 = ('Junior', 'Imaya', 'B')
    s3 = ('Freshmen', 'Emma', 'A-')
    s4 = ('Senior', 'Tiffany', 'B+')
    s5 = ('Sophomore', 'Liz', 'C+')
    s6 = ('Senior', 'Mel', 'F')
    s7 = ('Junior', 'Ray', 'C')
    class_roster = [s1, s2, s3, s4, s5, s6, s7]
    return render_template("roster.html", grade_view = grade_view, class_roster =class_roster)

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    #student_name = student_name
    return render_template("welcome.html", student_name = student_name)

if __name__ == "__main__":
    app.run()

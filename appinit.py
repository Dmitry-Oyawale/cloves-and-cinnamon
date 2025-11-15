from config import Config

from app import create_app, db
from app.main.models import Major, ResearchTopic, Language, Course
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

app = create_app(Config)
app.config['SECRET_KEY'] = 'REPLACE_LATER'

@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'sqlo': sqlo, 'db': db, 'Major': Major, 'Interest': ResearchTopic, 'Language': Language, 'Course': Course}

majors = ["CS", "RBE", "ME", "ECE", "AE", "DS", "MATH"]
interests = ["ML", "HPC", "AI", "Cybersecurity", "KDD", "Graphics"]
languages = ["C", "C++", "Python", "Haskell", "Java", "JavaScript", "Lisp", "Rust"]
courses = ["CS1004", "CS2011", "CS2102", "CS2201", "CS3013", "CS3133", "CS3431", "CS3516", "CS3733", "CS4233", "CS4001", "CS4002", "CS4003"]

@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()

# fill in db with some things

@sqla.event.listens_for(Major.__table__, 'after_create')
def add_majors(*args, **kwargs):
    query = sqla.select(Major)
    if db.session.scalars(query).first() is None:
        majorsDict = [{"name":majors[i]} for i in range(len(majors))]
        # print(majorsDict)  # debugging
        for t in majorsDict:
            db.session.add(Major(name=t["name"]))
        db.session.commit()

@sqla.event.listens_for(ResearchTopic.__table__, 'after_create')
def add_interests(*args, **kwargs):
    query = sqla.select(ResearchTopic)
    if db.session.scalars(query).first() is None:
        interestsDict = [{"name":interests[i]} for i in range(len(interests))]
        for t in interestsDict:
            db.session.add(ResearchTopic(name=t["name"]))
        db.session.commit()

@sqla.event.listens_for(Language.__table__, 'after_create')
def add_languages(*args, **kwargs):
    query = sqla.select(Language)
    if db.session.scalars(query).first() is None:
        languagesDict = [{"name":languages[i]} for i in range(len(languages))]
        for t in languagesDict:
            db.session.add(Language(name=t["name"]))
        db.session.commit()

@sqla.event.listens_for(Course.__table__, 'after_create')
def add_courses(*args, **kwargs):
    query = sqla.select(Course)
    if db.session.scalars(query).first() is None:
        coursesDict = [{"name":courses[i], "coursenum": courses[i]} for i in range(len(courses))]
        for t in coursesDict:
            db.session.add(Course(name=t["name"], coursenum=t["coursenum"]))
        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
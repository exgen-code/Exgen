import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Table, BigInteger, Time, Boolean, text
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# sort this out later
Base = declarative_base()
engine = create_engine('mysql://username:password@localhost/Database') #Ask steffan for username, password and database. Dont want this public on github
conn = engine.connect()
trans = conn.begin()

class User(Base):
    __tablename__ = "User"
    UserID = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    UserName = Column(String(128), nullable=False, unique=True)
    Hash = Column(String(128), nullable=False)
    Salt = Column(String(128), nullable=False)
    Type = Column(Integer, nullable=False)
    Professor = relationship("Professor")
    Student = relationship("Student")
    Answered = relationship("Answered")

class Professor(Base):
    __tablename__ = "Professor"
    ProfessorID = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    ProfessorName = Column(String(128), nullable=False)
    ProfessorInfo = Column(String(128))

    UserID = Column(ForeignKey('User.UserID'), primary_key=False, nullable=False, index=True)
    User = relationship('User')

class Student(Base):
    __tablename__ = "Student"
    StudentID = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)

    UserID = Column(ForeignKey('User.UserID'), primary_key=False, nullable=False, index=True)
    User = relationship('User')

class Module(Base):
    __tablename__ = "Module"
    ModuleID = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    ModuleName = Column(String(128), nullable=False)
    ModuleDescription = Column(String(128))
    ModuleCode = Column(Integer, unique=True, nullable=False)
    Exam = relationship('Exam')

class Exam(Base):
    __tablename__ = "Exam"
    ExamID = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    Title = Column(String(32), nullable=false)
    Description = Column(String(128))
    Enabled = Column(Boolean, nullable=False)

    ModuleID = Column(ForeignKey('Module.ModuleID'), primary_key=False, nullable=False, index=True)
    Module = relationship('Module')

class Question(Base):
    __tablename__ = "Question"
    QuestionTemplateID = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    LaTeX = Column(String(128), nullable=False)
    SolutionCode = Column(String(128), nullable=False)
    Enabled = Column(Boolean, nullable=False)

class Variable(Base):
    __tablename__ = "Variable"
    VariableID = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    VariableName = Column(String(32), nullable=False)
    VariableValue = Column(Integer, nullable=False)

class Answered(Base):
    __tablename__ = "Answered"
    QuestionID = Column(Integer, autoincrement=True, primary_key=True, unique=True, nullable=False)
    Correct = Column(Boolean, nullable=False)

    UserID = Column(ForeignKey('User.UserID'), primary_key=False, nullable=False, index=True)
    User = relationship("User")

t_Student_Module = Table(
    'Student_Module', metadata,
    Column('StudentID', ForeignKey('Student.StudentID'), primary_key=True, nullable=False, index=True),
    Column('ModuleID', ForeignKey('Module.ModuleID'), primary_key=True, nullable=False, index=True),
    Column('CourseRep', Boolean, nullable=False)
)

t_Professor_Module = Table(
    'Professor_Module', metadata,
    Column('ProfessorID', ForeignKey('Professor.ProfessorID'), primary_key=True, nullable=False, index=True),
    Column('ModuleID', ForeignKey('Module.ModuleID'), primary_key=True, nullable=False, index=True),
    Column('HeadProfessor', Boolean, nullable=False)
)

t_Exam_Question = Table(
    'Exam_Question', metadata,
    Column('ExamID', ForeignKey('Exam.ExamID'), primary_key=True, nullable=False, index=True),
    Column('QuestionTemplateID', ForeignKey('Question.QuestionTemplateID'), primary_key=True, nullable=False, index=True)
)

t_Variable_Question = Table(
    'Variable_Question', metadata,
    Column('VariableID', ForeignKey('Variable.VariableID'), primary_key=True, nullable=False, index=True),
    Column('QuestionTemplateID', ForeignKey('Question.QuestionTemplateID'), primary_key=True, nullable=False, index=True),
    Column('QuestionID', ForeignKey('Answered.QuestionID'), primary_key=True, nullable=False, index=True)
)

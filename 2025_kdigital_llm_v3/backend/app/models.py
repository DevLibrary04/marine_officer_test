# /app/models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

import enum

class GuchulSetTypeEnum(str, enum.Enum):
    gigwansa = "기관사"
    hanghaesa = "항해사"
    sohyeong = "소형선박조종사"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(45), unique=True, index=True)
    password = Column(String(255))
    chats = relationship("Chat", back_populates="user")

class Exam(Base):
    __tablename__ = "exams"
    id = Column(Integer, primary_key=True, index=True)
    # license_type = Column(String(50), nullable=False)
    license_type = Column(String(50), nullable=False)
    grade = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    inning = Column(Integer, nullable=False)
    subjects = relationship("Subject", back_populates="exam", cascade="all, delete-orphan")

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey("exams.id"))
    name = Column(String(100), nullable=False)
    exam = relationship("Exam", back_populates="subjects")
    questions = relationship("Question", back_populates="subject", cascade="all, delete-orphan")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    question_number = Column(Integer, nullable=False)
    question_text = Column(Text, nullable=False)
    option_a = Column(Text)
    option_b = Column(Text)
    option_c = Column(Text)
    option_d = Column(Text)
    correct_answer = Column(String(10), nullable=False)
    image_ref = Column(String(255), nullable=True)
    subject = relationship("Subject", back_populates="questions")
    
class Chat(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())
    user = relationship("User", back_populates="chats")
    chat_turns = relationship("ChatTurn", back_populates="chat", cascade="all, delete-orphan")
    
class ChatTurn(Base):
    __tablename__ = "chat_turns"
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chat.id"))
    prompt = Column(Text)
    response = Column(Text)
    image_path = Column(String(255), nullable=True)
    chat = relationship("Chat", back_populates="chat_turns")
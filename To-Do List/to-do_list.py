from sqlalchemy import create_engine
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


class ToDoList:

    def __init__(self, task=None):
        self.task = task

    def today_tasks(self):
        rows = session.query(Table).all()
        if rows:
            print('Today:')
            for task in rows:
                print(str(task.id) + '.', task.task)
        else:
            print("""Today:
Nothing to do!""")
        print('')

    def add_task(self):
        new_task = Table(task=self.task)
        session.add(new_task)
        session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    while True:
        print("""1) Today's tasks
2) Add task
0) Exit""")
        command = int(input())
        if command == 1:
            todo = ToDoList()
            todo.today_tasks()
        elif command == 2:
            task = input('Enter task\n')
            todo = ToDoList(task)
            todo.add_task()
            print('The task has been added!\n')
        elif command == 0:
            print('Bye!')
            exit()

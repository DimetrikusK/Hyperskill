from sqlalchemy import create_engine
import sqlite3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
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

    def __init__(self, task=None, my_date=None):
        self.task = task
        if my_date:
            my_date = my_date.split('-')
            self.deadlines = datetime(int(my_date[0]), int(my_date[1]), int(my_date[2]))

    def today_tasks(self):
        today = datetime.today()
        rows = session.query(Table).filter(Table.deadline == today.date()).all()
        count = 1
        if rows:
            for task in rows:
                print(f'{count}. {task}')
                count += 1
        else:
            print('Nothing to do!\n')

    def week_task(self):
        today = datetime.today()
        week = today.date() + timedelta(days=6)
        day = today.date()
        rows = session.query(Table).order_by(Table.deadline).\
            filter(Table.deadline >= today.date(), Table.deadline <= week).all()
        count = 1
        for i in range(7):
            if rows and day == rows[0].deadline:
                print(day.strftime('%A %d %b:'))
                for task in rows:
                    if day == task.deadline:
                        print(f'{count}. {task}')
                        count += 1
                rows = rows[1:]
                count= 1
                print('')
            else:
                print(day.strftime('%A %d %b:'))
                print('Nothing to do!\n')
            day += timedelta(days=1)

    def all_tasks(self):
        rows = session.query(Table).order_by(Table.deadline).all()
        count = 1
        print('All tasks:')
        if rows:
            for task in rows:
                day = task.deadline.strftime('%d')
                print(f'{count}. {task.task}. {int(day)} {task.deadline.strftime("%b")}')
                count += 1
        else:
            print("Nothing to do!\n")

    def add_task(self):
        new_task = Table(task=self.task, deadline=self.deadlines.date())
        session.add(new_task)
        session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    todo = ToDoList()
    while True:
        print("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit""")
        command = int(input())
        if command == 1:
            print('Today', datetime.today().strftime('%b %d:'))
            todo.today_tasks()
        elif command == 2:
            todo.week_task()
        elif command == 3:
            todo.all_tasks()
        elif command == 4:
            task = input('Enter task\n')
            my_date = input('Enter deadline\n')
            todo = ToDoList(task, my_date)
            todo.add_task()
            print('The task has been added!\n')
        elif command == 0:
            print('Bye!')
            exit()

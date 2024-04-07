import sqlalchemy

# 6. Создать питоновский файл Sqlite_task.py . Создать таблицу Users определив поля( id: первичный ключ,
# first_name,last_name:строки длинной в 50 символов, age: целое число). Создать “движок” для подключения
# SQLite и создать таблицу через Base.metadata.create_all(engine)


from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.first_name!r}, fullname={self.last_name!r}, age={self.age!r})"


engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)

# 7. Создать сессию и добавить в базу 5 разных пользователей.
with Session(engine) as session:
    testuser = User(
        first_name="TestUser1",
        last_name="TestLastName1",
        age=15,
    )
    testusertwo = User(
        first_name="TestUser1",
        last_name="TestLastName1",
        age=15,
    )

    patrick = User(first_name="patrick", last_name="Patrick Star", age=14)
    rick = User(first_name="rick", last_name="Patrick Rick", age=12)
    james = User(first_name="James", last_name="Cameron", age=20)
    session.add_all([testuser, testusertwo, patrick, rick, james])
    session.commit()

# 8. Создать сессию и вывести первых 3 пользователей отсортированных по убыванию возроста

stmt = select(User).order_by(User.age.desc()).limit(3)
for user in session.scalars(stmt):
    print(f'{user.first_name} {user.last_name}: {user.age}')

# 9. Создать сессию и вывести  пользователей по имени “James”

stmt = select(User).where(User.first_name.like("%James%"))
for user in session.scalars(stmt):
    print(f'{user.first_name} {user.last_name}: {user.age}')





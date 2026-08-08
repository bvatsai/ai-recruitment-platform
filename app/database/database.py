from __future__ import annotations
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "postgresql://postgres:Ai9651@localhost:5432/enterprise_ai_recruitment"

engine = create_engine(DATABASE_URL)    #creates a new SQLAlchemy engine instance using the provided database URL. The engine is responsible for managing the connection to the PostgreSQL database specified in the URL. It handles the communication between the application and the database, allowing for executing SQL queries and managing transactions.

class Base(DeclarativeBase):            #This class serves as the base class for all SQLAlchemy models in the application. It inherits from DeclarativeBase, which is a special class provided by SQLAlchemy that allows for defining database models using a declarative syntax. By inheriting from this base class, all models defined in the application will have access to the necessary functionality for interacting with the database, such as mapping to tables and defining relationships between models.
    pass

SessionLocal = sessionmaker(            #This line creates a session factory using the sessionmaker function from SQLAlchemy. The session factory is configured with the engine created earlier, which allows it to create new database sessions that are connected to the PostgreSQL database. The autoflush and autocommit parameters are set to False, meaning that changes made to the session will not be automatically flushed to the database and that transactions will not be automatically committed. This allows for more control over when changes are persisted to the database.
    bind=engine,
    autoflush=False,
    autocommit=False
)

def get_session():                      #This function is a generator that provides a database session to the caller. It creates a new session using the SessionLocal class, which is a session factory configured with the database engine. The session is yielded to the caller, allowing them to perform database operations within a context. After the caller is done using the session, it is closed in the finally block to ensure proper cleanup and release of resources.
    session = SessionLocal()
    try:
        yield session                   #This line yields the session object to the caller, allowing them to use it for database operations. The caller can perform queries, insertions, updates, and deletions using this session. Once the caller is done with the session, control will return to the finally block where the session will be closed to free up resources and ensure proper cleanup.
    finally:
        session.close()                 #This line closes the session after the caller is done using it. Closing the session is important to release any resources held by the session and to ensure that the connection to the database is properly closed. This helps prevent resource leaks and ensures that the application can efficiently manage database connections.
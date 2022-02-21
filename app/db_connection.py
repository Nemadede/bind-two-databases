from sqlalchemy import create_engine


user_engine = create_engine("mysql://username:password@127.0.0.1:3306/users_bind")
business_engine = create_engine("mysql://username:password@127.0.0.1:3306/business_bind")




# businessSession = sessionmaker(autoflush=True, autocommit=True, bind=business_engine)

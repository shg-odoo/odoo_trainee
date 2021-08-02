import psycopg2

connection = psycopg2.connect(user = "postgres",
                              password = "postgres",
                              host = "localhost",
                              port = "5432",
                              database = "postgres")

print("connected...")

cursor=connection.cursor()
cursor.exexute(""

# CREATE TABLE Items
# (
#     NAME TEXT
#     PRICE TEXT
# )


""
)

# connection.commit()
# print("sucess...")
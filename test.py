import os
import mysql.connector
from datetime import datetime

# Database connection configuration
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_NAME = os.environ.get('DB_NAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_PORT = 3306

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            port=DB_PORT
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

def fetch_tweets(cursor, offset=0, limit=5):
    query = """
    SELECT t.tid, t.tweet, t.date, u.username
    FROM tweets t
    JOIN users u ON t.user_id = u.id
    ORDER BY t.date DESC
    LIMIT %s OFFSET %s
    """
    cursor.execute(query, (limit, offset))
    return cursor.fetchall()

def display_tweets(tweets):
    for tweet in tweets:
        tid, content, date, username = tweet
        print(f"\n{'=' * 50}")
        print(f"Tweet ID: {tid}")
        print(f"User: {username}")
        print(f"Date: {date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Content: {content}")
        print(f"{'=' * 50}")

def main():
    connection = connect_to_database()
    if not connection:
        return

    cursor = connection.cursor()
    offset = 0
    limit = 5

    while True:
        tweets = fetch_tweets(cursor, offset, limit)
        display_tweets(tweets)

        if len(tweets) < limit:
            print("\nNo more tweets to display.")
            break

        choice = input("\nEnter 'n' for next 5 tweets, 'p' to post a new tweet, or 'q' to quit: ").lower()

        if choice == 'n':
            offset += limit
        elif choice == 'p':
            print("Creating a new post... (feature not implemented yet)")
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()

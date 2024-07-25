# cmd-microblog

A command-line interface for viewing microblog posts from a MariaDB database.

## Setup

1. Install required packages: `pip install mysql-connector-python`.
2. Set environment variables: `DB_HOST`, `DB_USER`, `DB_NAME`, and `DB_PASSWORD`.
3. Run the script: `python test.py`.

## Database Schema

The program assumes the following schema:
- `tweets` table: `tid`, `tweet`, `date`, `uid`
- `users` table: `uid`, `username`

Adjust the SQL query in `fetch_tweets()` if your schema differs.

## Troubleshooting

If you encounter "Access denied" errors:
1. Verify credentials and database host in environment variables.
2. Ensure the database user has proper permissions for remote access.
3. Check firewall settings and MariaDB configuration for remote connections.

import psycopg2
from datetime import datetime, date
from typing import List, Dict, Union
from psycopg2.extras import RealDictCursor

def extract_rows_by_date(
    db_params: Dict[str, str],
    table_name: str,
    target_date: Union[str, datetime, date],
    date_column: str = "Date"
) -> List[Dict]:
    """
    Extract all rows from a PostgreSQL table matching a specific date.

    Parameters:
    -----------
    db_params : dict
        Dictionary containing database connection parameters:
        {
            'dbname': 'your_database',
            'user': 'your_user',
            'password': 'your_password',
            'host': 'your_host',
            'port': 'your_port'
        }
    table_name : str
        Name of the table to query
    target_date : str or datetime or date
        The date to search for. Can be:
        - string in format 'YYYY-MM-DD'
        - datetime object
        - date object
    date_column : str
        Name of the date column in the table (default: "Date")

    Returns:
    --------
    List[Dict]
        List of dictionaries where each dictionary represents a row

    Raises:
    -------
    psycopg2.Error: If there's a database error
    ValueError: If the date format is invalid
    """
    # Convert target_date to string if it's a datetime or date object
    if isinstance(target_date, (datetime, date)):
        target_date = target_date.strftime('%Y-%m-%d')
    elif isinstance(target_date, str):
        # Validate date format
        try:
            datetime.strptime(target_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in format 'YYYY-MM-DD'")
    else:
        raise ValueError("target_date must be a string, datetime, or date object")

    try:
        # Connect to the database
        conn = psycopg2.connect(**db_params)
        
        # Use RealDictCursor to return results as dictionaries
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            # Create the SQL query using parameters to prevent SQL injection
            query = f'SELECT * FROM {table_name} WHERE DATE("Date") = %s'
            
            # Execute the query with the target date
            cur.execute(query, (target_date,))
            
            # Fetch all matching rows
            results = cur.fetchall()
            
            return [dict(row) for row in results]

    except psycopg2.Error as e:
        raise Exception(f"Database error: {str(e)}")
    
    finally:
        if 'conn' in locals():
            conn.close()

# Example usage
if __name__ == "__main__":
    # Database connection parameters
    db_params = {
        'dbname': 'your_database',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',
        'port': '5432'
    }
    
    # Example calls
    try:
        # Using a string date
        rows = extract_rows_by_date(
            db_params=db_params,
            table_name="your_table",
            target_date="2024-01-17"
        )
        print(f"Found {len(rows)} rows")
        
        # Using a datetime object
        from datetime import datetime
        today = datetime.now()
        rows = extract_rows_by_date(
            db_params=db_params,
            table_name="your_table",
            target_date=today
        )
        print(f"Found {len(rows)} rows for today")

    except Exception as e:
        print(f"Error: {str(e)}")
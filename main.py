# main.py
import time
from config import session
from src.trading import watchlist

def main():
    try:
        session_creation_time = None
        cst, x_security_token = None, None

        while True:
            current_time = time.time()
            if session_creation_time is None or (current_time - session_creation_time) > 240:  # Create session every 4 minutes
                cst, x_security_token = session.create_session()
                session_creation_time = current_time


            watchlist.get_watchlist(69124495674647, cst, x_security_token)


    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
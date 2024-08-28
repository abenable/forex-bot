import os
import time
from config import session
from src.trading import watchlist, positions
from src import account

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_session():
    """Create a new session and return session tokens and the creation timestamp."""
    cst, x_security_token = session.create_session()
    return cst, x_security_token, time.time()

def main_loop():
    session_creation_time = None
    cst, x_security_token = None, None

    while True:
        current_time = time.time()

        # Re-create the session if it's the first run or if more than 4 minutes have passed
        if session_creation_time is None or (current_time - session_creation_time) > 240:
            cst, x_security_token, session_creation_time = create_session()

        try:
            account_info = account.get_account_info(cst, x_security_token)
            # Fetch positions and watchlist data
            pos_data = positions.get_all_positions(cst, x_security_token)
            watchlist_data = watchlist.get_watchlist(69124495674647, cst, x_security_token)

            # Clear the console before printing new data
            clear_console()

            # Print account info
            account.print_account_info(account_info)
            print('\n')

            # Print positions and watchlist data
            positions.print_all_positions(pos_data)

            print('\n')
            watchlist.print_watchlist(watchlist_data)
            
        except Exception as e:
            # Catch and display any exceptions without stopping the loop
            print(f"An error occurred: {e}")

        # Pause for 1 second to prevent a tight loop
        time.sleep(1)

def main():
    while True:
        try:
            main_loop()
        except KeyboardInterrupt:
            print("Program terminated by user.")
            break
        except Exception as e:
            print(f"Main loop crashed with error: {e}. Restarting in 5 seconds...")
            time.sleep(5)  # Wait before restarting

if __name__ == "__main__":
    main()

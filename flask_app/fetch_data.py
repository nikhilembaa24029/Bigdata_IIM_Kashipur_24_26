import happybase
import env
from datetime import datetime
import time

# Connect to HBase
HOST = env.HBASE_HOST
PORT = env.HBASE_PORT


def fetch_latest_data(table_name):
    connection = None
    try:
        # Create connection
        connection = happybase.Connection(HOST, port=PORT)
        table = connection.table(table_name)

        # Scan the table and retrieve the latest data
        # `scan` returns all rows, which can be sorted by timestamp
        rows = table.scan(columns=[b'price:close', b'time:timestamp'])

        latest_data = None
        latest_timestamp = None

        for row_key, data in rows:
            # Convert timestamp from bytes to string, then to datetime
            timestamp_str = data[b'time:timestamp'].decode('utf-8')
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

            # Get the value of price:close
            close_price = float(data[b'price:close'].decode('utf-8'))

            # Update the latest data based on the timestamp
            if latest_timestamp is None or timestamp > latest_timestamp:
                latest_data = {
                    "close": close_price,
                    "timestamp": timestamp
                }
                latest_timestamp = timestamp

        if latest_data:
            # print(f"Latest Data: {latest_data}")
            return latest_data
        else:
            print("No data found.")
            return None

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None
    finally:
        # Close the connection if it exists
        if connection:
            connection.close()


# Example: Fetch the latest data every second
if __name__ == "__main__":
    table_name = "pred_stream"
    while True:
        data = fetch_latest_data(table_name)
        if data:
            print(f"Close Price: {data['close']}, Timestamp: {data['timestamp']}")

        # Wait one second before fetching new data
        time.sleep(1)

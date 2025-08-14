from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'
DB_NAME = 'your_db_name'

@app.route('/add_data', methods=['POST'])
def add_data():
    try:
        data = request.get_json()

        if not data or 'temperature' not in data or 'humidity' not in data:
            return jsonify({'error': 'Invalid or missing data'}), 400

        temperature = data['temperature']
        humidity = data['humidity']

        # Connect to MySQL database
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()

        # Insert data into table
        insert_query = "INSERT INTO sensor_data (temperature, humidity) VALUES (%s, %s)"
        cursor.execute(insert_query, (temperature, humidity))
        connection.commit()

        return "Data Added", 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'connection' in locals(): connection.close()

if __name__ == '__main__':
    # Run on all available interfaces so ESP32 can connect
    app.run(host='0.0.0.0', port=5000)

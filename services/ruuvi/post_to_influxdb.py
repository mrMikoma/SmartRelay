"""
from ruuvitag-sensor example: https://github.com/ttu/ruuvitag-sensor/blob/master/examples/post_to_influxdb.py
"""

from influxdb import InfluxDBClient
from ruuvitag_sensor.ruuvi import RuuviTagSensor

client = InfluxDBClient(host="localhost", port=8086, database="ruuvi")


def write_to_influxdb(received_data):
    mac = received_data[0]
    payload = received_data[1]

    # dataFormat = payload["data_format"] if ("data_format" in payload) else None
    # fields = {}
    # fields["temperature"] = payload["temperature"] if ("temperature" in payload) else None
    # fields["humidity"] = payload["humidity"] if ("humidity" in payload) else None
    # fields["pressure"] = payload["pressure"] if ("pressure" in payload) else None
    # fields["accelerationX"] = payload["acceleration_x"] if ("acceleration_x" in payload) else None
    # fields["accelerationY"] = payload["acceleration_y"] if ("acceleration_y" in payload) else None
    # fields["accelerationZ"] = payload["acceleration_z"] if ("acceleration_z" in payload) else None
    # fields["batteryVoltage"] = payload["battery"] / 1000.0 if ("battery" in payload) else None
    # fields["txPower"] = payload["tx_power"] if ("tx_power" in payload) else None
    # fields["movementCounter"] = payload["movement_counter"] if ("movement_counter" in payload) else None
    # fields["measurementSequenceNumber"] = (
    #     payload["measurement_sequence_number"] if ("measurement_sequence_number" in payload) else None
    # )
    # fields["tagID"] = payload["tagID"] if ("tagID" in payload) else None
    # fields["rssi"] = payload["rssi"] if ("rssi" in payload) else None
    # json_body = [
    #     {"measurement": "ruuvi_measurements", "tags": {"mac": mac, "dataFormat": dataFormat}, "fields": fields}
    # ]
    # client.write_points(json_body)


if __name__ == "__main__":
    RuuviTagSensor.get_data(write_to_influxdb)

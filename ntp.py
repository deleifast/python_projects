import ntplib


def is_local_time_accurate():
    client = ntplib.NTPClient()
    try:
        response = client.request()
    except ntplib.NTPException:
        return False
    return response.offset < 1

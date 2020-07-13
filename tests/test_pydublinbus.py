from pydublinbus.pydublinbus import DublinBusRTPI
from unittest.mock import Mock
import unittest

EXAMPLE_API_RESPONSE = {
    "errorcode": "0",
    "errormessage": "",
    "numberofresults": 3,
    "results": [
        {
            "additionalinformation": "",
            "arrivaldatetime": "02/07/2020 12:07:59",
            "departuredatetime": "02/07/2020 12:07:59",
            "departureduetime": "1",
            "destination": "Maynooth",
            "destinationlocalized": "Maigh Nuad",
            "direction": "Outbound",
            "duetime": "1",
            "lowfloorstatus": "no",
            "monitored": "true",
            "operator": "bac",
            "operatortype": "1",
            "origin": "Merrion Square",
            "originlocalized": "Cearnóg Mhuirfean",
            "route": "67",
            "scheduledarrivaldatetime": "02/07/2020 12:05:00",
            "scheduleddeparturedatetime": "02/07/2020 12:05:00",
            "sourcetimestamp": "02/07/2020 12:05:15",
        },
        {
            "additionalinformation": "",
            "arrivaldatetime": "02/07/2020 12:09:42",
            "departuredatetime": "02/07/2020 12:09:42",
            "departureduetime": "2",
            "destination": "Leixlip",
            "destinationlocalized": "Leixlip",
            "direction": "Outbound",
            "duetime": "2",
            "lowfloorstatus": "no",
            "monitored": "true",
            "operator": "bac",
            "operatortype": "1",
            "origin": "Merrion Square",
            "originlocalized": "Cearnóg Mhuirfean",
            "route": "66B",
            "scheduledarrivaldatetime": "02/07/2020 12:12:00",
            "scheduleddeparturedatetime": "02/07/2020 12:12:00",
            "sourcetimestamp": "02/07/2020 12:05:15",
        },
        {
            "additionalinformation": "",
            "arrivaldatetime": "02/07/2020 12:19:42",
            "departuredatetime": "02/07/2020 12:19:42",
            "departureduetime": "12",
            "destination": "Leixlip",
            "destinationlocalized": "Leixlip",
            "direction": "Outbound",
            "duetime": "12",
            "lowfloorstatus": "no",
            "monitored": "true",
            "operator": "bac",
            "operatortype": "1",
            "origin": "Merrion Square",
            "originlocalized": "Cearnóg Mhuirfean",
            "route": "67",
            "scheduledarrivaldatetime": "02/07/2020 12:05:00",
            "scheduleddeparturedatetime": "02/07/2020 12:05:00",
            "sourcetimestamp": "02/07/2020 12:05:15",
        },
    ],
    "stopid": "312",
    "timestamp": "02/07/2020 12:06:50",
}


EXPECTED_OUTPUT_NO_ROUTE_FILTER = [
    {"due_in": "1", "route": "67"},
    {"due_in": "2", "route": "66B"},
    {"due_in": "12", "route": "67"},
]

EXPECTED_OUTPUT_ROUTE_FILTER = [
    {"due_in": "1", "route": "67"},
    {"due_in": "12", "route": "67"},
]

EXAMPLE_API_RESPONSE_ERROR_1 = {
    "errorcode": "1",
    "errormessage": "No Results",
    "numberofresults": 0,
    "results": "",
}

EXPECTED_OUTPUT_ERROR_1 = []


def test_raw_rtpi_data_is_dict():
    dublinbus = DublinBusRTPI("312")
    response = dublinbus.raw_rtpi_data()
    assert isinstance(response, dict)


def test_bus_timetable_without_route():
    dublinbus = DublinBusRTPI("312")
    dublinbus.raw_rtpi_data = Mock(return_value=EXAMPLE_API_RESPONSE)
    assert dublinbus.bus_timetable() == EXPECTED_OUTPUT_NO_ROUTE_FILTER


def test_bus_timetable_with_route():
    dublinbus = DublinBusRTPI("312", "67")
    dublinbus.raw_rtpi_data = Mock(return_value=EXAMPLE_API_RESPONSE)
    assert dublinbus.bus_timetable() == EXPECTED_OUTPUT_ROUTE_FILTER


def test_bus_timetable_no_results():
    dublinbus = DublinBusRTPI("312", "67")
    dublinbus.raw_rtpi_data = Mock(return_value=EXAMPLE_API_RESPONSE_ERROR_1)
    assert dublinbus.bus_timetable() == EXPECTED_OUTPUT_ERROR_1


if __name__ == "__main__":
    unittest.main()

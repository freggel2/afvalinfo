import logging
from datetime import timedelta

SENSOR_TYPES = {
    "gft": ["GFT", "mdi:recycle"],
    "kerstboom": ["Kerstboom", "mdi:recycle"],
    "papier": ["Papier", "mdi:recycle"],
    "pbd": ["PBD", "mdi:recycle"],
    "restafval": ["Restafval", "mdi:recycle"],
    "takken": ["Takken", "mdi:recycle"],
    "textiel": ["Textiel", "mdi:recycle"],
    "trash_type_today": ["Today", "mdi:recycle"],
    "trash_type_tomorrow": ["Tomorrow", "mdi:recycle"],
}

SENSOR_LOCATIONS_TO_URL = {
    "trashapi": [
        "http://trashapi.azurewebsites.net/trash?Location={0}&ZipCode={1}&HouseNumber={2}&HouseNumberSuffix={3}"
    ]
}

MONTH_TO_NUMBER = {
    "jan": "01",
    "feb": "02",
    "mrt": "03",
    "apr": "04",
    "mei": "05",
    "jun": "06",
    "jul": "07",
    "aug": "08",
    "sep": "09",
    "okt": "10",
    "nov": "11",
    "dec": "12",
    "januari": "01",
    "februari": "02",
    "maart": "03",
    "april": "04",
    "mei": "05",
    "juni": "06",
    "juli": "07",
    "augustus": "08",
    "september": "09",
    "oktober": "10",
    "november": "11",
    "december": "12",
}

NUMBER_TO_MONTH = {
    1: "januari",
    2: "februari",
    3: "maart",
    4: "april",
    5: "mei",
    6: "juni",
    7: "juli",
    8: "augustus",
    9: "september",
    10: "oktober",
    11: "november",
    12: "december",
}

CONF_CITY = "city"
CONF_LOCATION = "location"
CONF_POSTCODE = "postcode"
CONF_STREET_NUMBER = "streetnumber"
CONF_STREET_NUMBER_SUFFIX = "streetnumbersuffix"
CONF_DATE_FORMAT = "dateformat"
CONF_TIMESPAN_IN_DAYS = "timespanindays"
CONF_LOCALE = "locale"
CONF_ID = "id"
CONF_NO_TRASH_TEXT = "notrashtext"
SENSOR_PREFIX = "Afvalinfo "
ATTR_LAST_UPDATE = "last_update"
ATTR_HIDDEN = "hidden"
ATTR_IS_COLLECTION_DATE_TODAY = "is_collection_date_today"
ATTR_DAYS_UNTIL_COLLECTION_DATE = "days_until_collection_date"
ATTR_YEAR_MONTH_DAY_DATE = "year_month_day_date"
ATTR_FRIENDLY_NAME = "friendly_name"

_LOGGER = logging.getLogger(__name__)

MIN_TIME_BETWEEN_UPDATES = timedelta(hours=1)

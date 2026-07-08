MACHINES = [
    {
        "id": "m-press-01",
        "lineCode": "LINE-A",
        "name": "Press 01",
        "location": "Plant 2 / Bay 4",
        "status": "critical",
        "sensorCount": 4,
        "alertCount": 2,
        "latestIngestAt": "2026-07-08T09:18:12+09:00",
    },
    {
        "id": "m-cnc-07",
        "lineCode": "LINE-B",
        "name": "CNC Mill 07",
        "location": "Plant 2 / Bay 9",
        "status": "warning",
        "sensorCount": 5,
        "alertCount": 1,
        "latestIngestAt": "2026-07-08T09:18:16+09:00",
    },
    {
        "id": "m-oven-03",
        "lineCode": "LINE-C",
        "name": "Curing Oven 03",
        "location": "Plant 1 / Heat Cell",
        "status": "online",
        "sensorCount": 3,
        "alertCount": 0,
        "latestIngestAt": "2026-07-08T09:18:11+09:00",
    },
]

SENSORS = [
    {"id": "s-vib-press-01", "machineId": "m-press-01", "metricKey": "vibration", "unit": "mm/s", "status": "critical", "latestValue": 9.8, "normalMin": 0, "normalMax": 6.2, "quality": "good"},
    {"id": "s-temp-press-01", "machineId": "m-press-01", "metricKey": "bearing_temp", "unit": "C", "status": "warning", "latestValue": 82.1, "normalMin": 20, "normalMax": 78, "quality": "late"},
    {"id": "s-amp-press-01", "machineId": "m-press-01", "metricKey": "current", "unit": "A", "status": "online", "latestValue": 41.5, "normalMin": 20, "normalMax": 48, "quality": "good"},
    {"id": "s-vib-cnc-07", "machineId": "m-cnc-07", "metricKey": "spindle_vibration", "unit": "mm/s", "status": "warning", "latestValue": 5.7, "normalMin": 0, "normalMax": 5.4, "quality": "good"},
    {"id": "s-temp-oven-03", "machineId": "m-oven-03", "metricKey": "chamber_temp", "unit": "C", "status": "online", "latestValue": 176.4, "normalMin": 160, "normalMax": 190, "quality": "good"},
]

RULES = [
    {"id": "r-001", "sensorId": "s-vib-press-01", "metricKey": "vibration", "operator": "gt", "threshold": 6.2, "windowSec": 30, "enabled": True, "updatedAt": "2026-07-08T08:54:00+09:00"},
    {"id": "r-002", "sensorId": "s-temp-press-01", "metricKey": "bearing_temp", "operator": "gt", "threshold": 78, "windowSec": 60, "enabled": True, "updatedAt": "2026-07-08T08:20:00+09:00"},
    {"id": "r-003", "sensorId": "s-temp-oven-03", "metricKey": "chamber_temp", "operator": "lt", "threshold": 160, "windowSec": 120, "enabled": False, "updatedAt": "2026-07-07T17:10:00+09:00"},
]

ANOMALY_EVENTS = [
    {"id": "a-924", "sensorId": "s-vib-press-01", "machineName": "Press 01", "startedAt": "2026-07-08T09:12:00+09:00", "endedAt": None, "maxValue": 9.8, "status": "open"},
    {"id": "a-917", "sensorId": "s-temp-press-01", "machineName": "Press 01", "startedAt": "2026-07-08T08:44:00+09:00", "endedAt": "2026-07-08T08:51:00+09:00", "maxValue": 84.2, "status": "closed"},
]

#!python2
# NOTE: I have written this code before.
# https://github.com/cmoscardi/bus_kalman/blob/master/kalman.ipynb
import pandas as pd
import requests
import unicodecsv as csv

# defining constants for ease-of-use
# NOTE: Lowercase deliberate. I made a stylistic choice here because these
# constants are based on my flatten_dict function.
lng_key = "MonitoredVehicleJourney_VehicleLocation_Longitude"
lat_key = "MonitoredVehicleJourney_VehicleLocation_Latitude"
bearing_key="MonitoredVehicleJourney_Bearing"
direction_key="MonitoredVehicleJourney_DirectionRef"
progress_key='MonitoredVehicleJourney_ProgressRate'
line_key=u'MonitoredVehicleJourney_LineRef'
dist_from_base_key = "MonitoredVehicleJourney_MonitoredCall_Extensions_Distances_CallDistanceAlongRoute"
dist_to_next_stop_key = u'MonitoredVehicleJourney_MonitoredCall_Extensions_Distances_DistanceFromCall'
timestamp_key = "RecordedAtTime"
join_key = "MonitoredVehicleJourney_FramedVehicleJourneyRef_DatedVehicleJourneyRef"

line_name = "MonitoredVehicleJourney_PublishedLineName"
#NOTE: see README for explanation of why this is equivalent to OnwardCalls
human_distance = "MonitoredVehicleJourney_MonitoredCall_Extensions_Distances_PresentableDistance"
stop_name = "MonitoredVehicleJourney_MonitoredCall_StopPointName"


MTA_API_BASE = "http://bustime.mta.info/api/siri/vehicle-monitoring.json"
def _flatten_dict(root_key, nested_dict, flattened_dict):
    for key, value in nested_dict.iteritems():
        next_key = root_key + "_" + key if root_key != "" else key
        if isinstance(value, dict):
            _flatten_dict(next_key, value, flattened_dict)
        else:
            flattened_dict[next_key] = value
    return flattened_dict
    
def nyc_current(key, bus):
    #NOTE: DetailLevel is actually unnecessary for MonitoredCall
    params = {"key": key,
              "LineRef": bus,
              "VehicleMonitoringDetailLevel": "calls"}
    resp = requests.get(MTA_API_BASE, params=params).json()
    info = resp['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    return pd.DataFrame([_flatten_dict('', i, {}) for i in info])


def print_ass1(bus_df):
    """
    Your program should output the following to the console:
    the bus name,
    the number of vehicles
    their current position
    """
    bus_name = bus_df[line_name].unique()[0]
    num_vehicles = len(bus_df)
    positions = bus_df[[lat_key, lng_key]].iterrows()
    print "Line: {}, # vehicles: {}".format(bus_name, num_vehicles)
    print "positions:"
    for _, (lat, lng) in positions:
        print "{},{}".format(lat, lng)

def print_ass2(bus_df, fname=None):
    """
    Output:
    Latitude,Longitude,Stop Name,Stop Status
    40.755489,-73.987347,7 AV/W 41 ST,at stop
    40.775657,-73.982036,BROADWAY/W 69 ST,approaching
    40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
    40.764998,-73.980416,N/A,N/A
    40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
    40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
    40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
    """
    ass2_info = [("Latitude", lat_key),
                 ("Longitude", lng_key),
                 ("Stop Name", stop_name),
                 ("Stop Status", human_distance)]
    bus_df[[k[0] for k in ass2_info]] = bus_df[[k[1] for k in ass2_info]]
    out_csv = bus_df[[k[0] for k in ass2_info]].fillna("N/A")\
                                               .to_csv(index=False)
    with open(fname, "w+") as out_f:
        out_f.write(out_csv)


def main(key, bus, out_f=None):
    bus_df = nyc_current(key, bus)
    if out_f:
      print_ass2(bus_df, out_f)
    else:
      print_ass1(bus_df)
    

ASS1_FNAME = "show_bus_locations_clm633.py"
ASS2_FNAME = "get_bus_info_clm633.py"
ASS1_USAGE = "Usage: python {} [API_KEY] [BUS_LINE]".format(__file__)
ASS2_USAGE = "Usage: python {} [API_KEY] [BUS_LINE] [OUT_FILENAME]".format(__file__)


if __name__ == "__main__":
    import sys
    try:
        fname = sys.argv[0]
        if fname == ASS1_FNAME:
            key, bus = sys.argv[1:3]
            out_f = None
        else:
            key, bus, out_f = sys.argv[1:4]
    except ValueError as e:
        print >>sys.stderr, (ASS1_USAGE if fname == ASS1_FNAME else ASS2_USAGE)
        sys.exit(1)

    main(key, bus, out_f)

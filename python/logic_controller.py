#!/usr/bin/env python3

def fetch_smalltable_rows(table_handle: smalltable.Table,
                          keys: Sequence[Union[bytes, str]],
                          require_all_keys: bool = False,
                         ) -> Mapping[bytes, Tuple[str]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
      table_handle:
        An open smalltable.Table instance.
      keys:
        A sequence of strings representing the key of each table row to
        fetch.  String keys will be UTF-8 encoded.
      require_all_keys:
        Optional; If require_all_keys is True only rows with values set
        for all keys will be returned.

    Returns:
      A dict mapping keys to the corresponding table row data
      fetched. Each row is represented as a tuple of strings. For
      example:

      {b'Serak': ('Rigel VII', 'Preparer'),
       b'Zim': ('Irk', 'Invader'),
       b'Lrrr': ('Omicron Persei 8', 'Emperor')}

      Returned keys are always bytes.  If a key from the keys argument is
      missing from the dictionary, then that row was not found in the
      table (and require_all_keys must have been False).

    Raises:
      IOError: An error occurred accessing the smalltable.
    """

class SampleClass:
    """Summary of class here.

    Longer class information....
    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""

from pathlib import Path
from argparse import ArgumentParser
from output_pb2 import OutputMessage
from queue import PriorityQueue
from enum import Enum
import sys

class Color(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3

class ObjectLabel(Enum):
    CAR = 1
    PEDESTRIAN = 2
    CYCLIST = 3
    MISC = 4

class Intersection:
    """Contains functionality for detecting and controlling traffic flow.

    Attributes:
        lanes: 
            Array of LaneInfo objects.
        traffic_q: 
            Reverse priority queue for lanes to be emptied.
    """

    class LaneInfo:
        """Holds a set of data about each lane.

        Attributes:
            dir: 
                Direction of the lane.
            is_striaght: 
                Boolean value for if lane allows traffic to travel straight.
            is_left:
                Boolean value for if lane allows traffic to turn left.
            is_right:
                Boolean value for if lane allows traffic to turn right.
            num_cars:
                Number of cars detected in the lane.
            bounds:
                BoundingArea object describing bounds of the lane.
            lane_time:
                How long it takes for the lane to be emptied.
        """
        
        class BoundingArea:
            """Holds bounding values of lane

            Attributes:
                x_min:
                    Minimum x coordinate value (meters).
                x_max:
                    Maxium x coordinate value (meters).
                y_min:
                    Minimum y coordinate value (meters).
                y_max:
                    Maximum y coordinate value (meters).
            """
            # x and y are the coords of the center of the lane
            def __init__(self, x, y, lane_dims):
                """
                TODO
                """

                self.x_min = x - (lane_dims.width/2)
                self.x_max = x + (lane_dims.width/2)
                self.y_min = y - (lane_dims.height/2)
                self.y_max = y + (lane_dims.height/2)

        def __init__(self, lane_info):
            self.dir = lane_info[dir]
            self.is_straight = lane_info[is_straight]
            self.is_left = lane_info[is_left]
            self.is_right = lane_info[is_right]
            #self.zone_id
            self.num_cars = 0
            self.bounds = self.BoundingArea(
                lane_info[x], 
                lane_info[y], 
                lane_info[lane_dims])
            self.lane_time = 0

        #   @returns caluclated time to empty the lane
        def calc_lane_time():
            # TODO: add advanced calculation on lane time given # of cars
            # ( (number of cars * length of the car) + (3*lanewidth) + 
            # (2*width of zebra crossing) ) / Constant velocity at the intersection
            self.lane_time = self.num_cars

    class ReversePriorityQueue(PriorityQueue):
        def __init__(self, q):
            self.priq = q
        
        def put(self, tup):
            newtup = tup[0] * -1, tup[1]
            self.priq.put(newtup)

        def get(self):
            tup = self.priq.get()
            newtup = tup[0] * -1, tup[1]
            return newtup

        def empty(self):
            return self.priq.empty()
    
    def __init__(self, lane_info):
        # TODO:
        self.lanes = {}
        # loop over lane information JSON for all lane info
            # append a new lane to LaneInfo lanes dictionary
            # self.lanes[lane_info[i][dir]] = (new LaneInfo(lane_info)
        q = PriorityQueue()
        self.traffic_q = self.ReversePriorityQueue(q)
    
    #   @param lanes_arr is an array of lanes 
    #   @param zone_id is the id of the zone
    #   @returns boolean indicating whether a reqested lane has been configured
    def is_valid_lane(zone_id):
        # iterate over all the lanes configured.
        # compare zone_id
        return 0


    #   @param output is the OutputMessage object parsed from a binary file
    #   @param lanes_arr array of current lanes
    #   @param obj_id 
    #   @param zone_id
    #   @returns whether an object is in a particular lane
    def is_in_lane(output, lanes_arr, obj_id, zone_id):
        if ~is_valid_lane(lanes_arr, zone_id): # check if valid lane
            sys.exit("Error: Invalid lane entry. Lane does not exist. Exiting.")
        else:
            for zone in output.region_of_interest: # iterate over configured regions
                if(zone.id == zone_id):
                    for obj in zone.object_ids:
                        if(obj.id== obj_id):
                            return True
            return False

    def obj_lane(obj):
        # if statements comparing obj coord to lane bounds
        # return lane OR -1 for no_lane

    def add_to_lanes_info(obj):
        # add car to lane
        # TODO: try , catch block?
        lane = obj_lane(obj)
        if(lane == -1):
            return
        # lanes[lane].num_cars++
    
    #   @param  bag_dir is a path to a directory with bin files from a ROS bag
    #   @param  num_files is an integer equal to the number of files to process
    #   @returns matrix of Car objects
    def get_car_objs(bag_dir, num_files):
        p = Path('../binary_files')
        if(p.exists() is not True):
            sys.exit("Error: No ../binary_files folder.")
        bin_paths = []
        # objs_matrix = []
        for dir in p.iterdir():
            if str(dir) == bag_dir:
                row = []
                bin_paths = list(p.glob('**/*.bin')) # gen list of paths
                i = 0
                for bin_file in range(0, num_files): # parse the number of files specified
                    output = parse_output_file(bin_paths[bin_file])
                    row = []
                    for obj in output.objects:
                        # TODO: add methods for considering other objects detected
                        if(obj.label == ObjectLabel.CAR):
                            self.add_to_lanes_info(obj)

#   @param filename is the name of the binary file you want to parse
#   @returns parsed output in the form of an OutputMessage object (configured 
#   in protobuf schema file)
def parse_output_file(filename):
    with open(filename, 'rb') as f:
        output = OutputMessage()
        output.ParseFromString(f.read())
        return output

#   @returns a list of Lane objects corresponding to the lanes that were configured as
#   regions of interest in SENSR
#   @param output is the translated binary output (return 
#   value of the function parse_output_file()
#   TODO: customize based on how zones are configured in SENSR
def populate_lanes(output):
    try:
        regions = output.region_of_interest
    except AttributeError:
        sys.exit("Error: There are no regions of interest configured in SENSR-S.")
    lanes_arr = []
    for zone in output.region_of_interest:
        dir = ''
        turn_dir = False
        if zone.id == 0:
           dir = 'None'
           turn_dir = False
        elif zone.id == 1: # Northbound, straight
           dir = 'North'
           turn_dir = False
        elif zone.id == 2: # Northbound, left
           dir = 'North'
           turn_dir = True
        elif zone.id == 3: # Southbound, straight
           dir = 'South'
           turn_dir = False
        elif zone.id == 4: # Southbound, left
           dir = 'South'
           turn_dir = True
        elif zone.id == 5: # Eastbound, straight
           dir = 'East'
           turn_dir = False
        elif zone.id == 6: # Eastbound, left
           dir = 'East'
           turn_dir = True
        elif zone.id == 7: # Westbound, straight
           dir = 'West'
           turn_dir = False
        elif zone.id == 8: # Westbound, left
           dir = 'West'
           turn_dir = True
        lanes_arr.append(Lane(dir, turn_dir))
    return lanes_arr

#   @param object is a protobuf object returned from SENSR
#   @returns whether an object has reliable tracking info
def is_reliable_tracking(object):
    try:
        if object.track.tracking_reliable == True:
            return 1
        elif  object.track.tracking_reliable == False:
            return 0
    except AttributeError:
        print(f'Tracking reliable field not set for Object #{object.id}')
        return -1

#   @param dict is a dictionary with keys = traffic directions and 
#   values = number of cars in each lane
#   @returns a list of the signal value each second
def get_sig_list(dict):
    
    sigs = Signals()
    signal_cycle = []
    while not my_q.empty():
        next_item = my_q.get()
        time = next_item[0]
        lane = next_item[1]
        if(lane == 'Eastbound'):
            sigs.set_state(EB_GR)
            sigs.NEXT_STATE = EB_Y
        elif(lane == 'Westbound'):
            sigs.set_state(WB_GR)
            sigs.NEXT_STATE = WB_Y
        elif(lane == 'Southbound'):
            sigs.set_state(SB_GR)
            sigs.NEXT_STATE = SB_Y
        elif(lane == 'Northbound'):
            sigs.set_state(NB_GR)
            sigs.NEXT_STATE = NB_Y
        for count in range(0, time):
            signal_cycle.append(sigs.STATE)
        sigs.set_state(sigs.NEXT_STATE)
        sigs.NEXT_STATE = RESET
        for count in range(0, 2): 
            signal_cycle.append(sigs.STATE)
        sigs.set_state(sigs.NEXT_STATE)
        signal_cycle.append(sigs.STATE)
    return signal_cycle
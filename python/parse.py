#!/usr/bin/env python3
from pathlib import Path
from argparse import ArgumentParser
from output_pb2 import OutputMessage
from queue import PriorityQueue
import sys

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

RESET = 'RESET'
WB_GR = 'WB_GR'
WB_Y = 'WB_Y'
NB_GR = 'NB_GR'
NB_Y = 'NB_Y'
SB_GR = 'SB_GR'
SB_Y = 'SB_Y'
EB_GR = 'EB_GR'
EB_Y = 'EB_Y'

# 0 --> RED
# 1 --> GREEN
# 2 ---> YELLOW
class Signals:
    def __init__(self):
        self.northb_L = 0
        self.northb_S = 0
        self.northb_R = 0
        self.southb_L = 0 
        self.southb_S = 0
        self.southb_R = 0
        self.eastb_L = 0
        self.eastb_S = 0
        self.eastb_R = 0
        self.westb_L = 0 
        self.westb_S = 0 
        self.westb_R = 0
        self.STATE = 'RESET'
        self.NEXT_STATE = 'RESET'

    def set_state(self, STATE):
        if(STATE == 'RESET'):
            self.northb_L = 0
            self.northb_S = 0
            self.northb_R = 0
            self.southb_L = 0 
            self.southb_S = 0
            self.southb_R = 0
            self.eastb_L = 0
            self.eastb_S = 0
            self.eastb_R = 0
            self.westb_L = 0 
            self.westb_S = 0
            self.westb_R = 0
            self.STATE = 'RESET'
        
        elif(STATE == WB_GR):
            self.westb_S = 1
            self.STATE = 'WB_GR'
        
        elif(STATE == SB_GR):
            self.southb_S = 1
            self.STATE = 'SB_GR'
        
        elif(STATE == NB_GR):
            self.northb_S = 1
            self.STATE = 'NB_GR'

        elif(STATE == EB_GR):
            self.eastb_S = 1
            self.STATE = 'EB_GR'
        
        elif(STATE == WB_Y):
            self.westb_S = 2
            self.STATE = 'WB_Y'
        
        elif(STATE == SB_Y):
            self.southb_S = 2
            self.STATE = 'SB_Y'
        
        elif(STATE == NB_Y):
            self.northb_S = 2
            self.STATE = 'NB_Y'

        elif(STATE == EB_Y):
            self.eastb_S = 2
            self.STATE = 'EB_Y'


class Object:
    def __init__(self, type, x, y, x_vel, y_vel):
        self.type = type
        self.x_pos = x
        self.y_pos = y
        self.x_vel = x_vel
        self.y_vel = y_vel
    def __str__(self):
        return str(self.type) + " located at (" + (str(self.x_pos)) + ", " + str(self.y_pos) + ") with velocity (" + (str(self.x_vel)) + ", " + str(self.y_vel)
    def __repr__(self):
        return str(self)

class Lane:
    def __init__(self, tr_direct, is_left_turn):
        self.trd = tr_direct
        self.is_lt = is_left_turn
    def __str__(self):
        return "Direction: " + str(self.trd) + ". Left Turn Lane: " + str(self.is_lt)
    def __repr__(self):
        return str(self)


# ( (number of cars * length of the car) + (3*lanewidth) + (2*width of zebra crossing) ) / Constant velocity at the intersection
def lane_time(num_cars):
    return num_cars

def coord_to_lane(obj):
    if((obj.x_pos > 30) & (obj.y_pos > 3) & (obj.y_pos < 15)): 
        return 'Southbound'
    elif((obj.x_pos < 0) & (obj.y_pos > 0 ) & (obj.y_pos < 10)):
        return 'Northbound'
    elif((obj.x_pos > 10 ) & (obj.y_pos < 20) & (obj.y_pos < 0)):
        return 'Westbound'
    elif((obj.x_pos > 0) & (obj.x_pos < 15) & (obj.y_pos > 20)):
        return 'Eastbound'


#   @brief  Converts an label number to string describing object
#   @param  label is an integer value
#   @retval string equal to the corresponding object
# NOTE: must be customized based on how labels are configured in SENSR-S
def label_to_string(label):
    if label == 0:
        return 'Car'
    elif label == 1:
        return 'Pedestrian'
    elif label == 2:
        return 'Cyclist'
    return 'Misc'

# converts a zone number into a Lane object
# NOTE: must be customized based on how zones are configured in SENSR-S
def zone_to_Lane(zone):
   
    tr_direct = ''
    is_left_turn = False
    if zone.id == 0:
        tr_direct = 'None'
        is_left_turn = False
    elif zone.id == 1: # Northbound, straight
        tr_direct = 'North'
        is_left_turn = False
    elif zone.id == 2: # Northbound, left
        tr_direct = 'North'
        is_left_turn = True
    elif zone.id == 3: # Southbound, straight
        tr_direct = 'South'
        is_left_turn = False
    elif zone.id == 4: # Southbound, left
        tr_direct = 'South'
        is_left_turn = True
    elif zone.id == 5: # Eastbound, straight
        tr_direct = 'East'
        is_left_turn = False
    elif zone.id == 6: # Eastbound, left
        tr_direct = 'East'
        is_left_turn = True
    elif zone.id == 7: # Westbound, straight
        tr_direct = 'West'
        is_left_turn = False
    elif zone.id == 8: # Westbound, left
        tr_direct = 'West'
        is_left_turn = True
    return Lane(tr_direct, is_left_turn)

# returns whether a reqested lane has been configured
def is_valid_lane(lanes_arr, zone_id):
    for lane in lanes_arr:
        if lane == zone_id:
            return 1
    return 0

# returns parsed output from binary file
def parse_output_file(filename):
    with open(filename, 'rb') as f:
        output = OutputMessage()
        output.ParseFromString(f.read())
        return output

# returns whether an object is in a particular lane
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

# returns a list populated with lane information
# parameter output is the translated binary output (return 
# value of the function parse_output_file()
# NOTE: must be customized based on how zones are configured in SENSR-S
def populate_lanes(output):
    try:
        regions = output.region_of_interest
    except AttributeError:
        sys.exit("Error: There are no regions of interest configured in SENSR-S.")
    lanes_arr = []
    for zone in output.region_of_interest:
        
        tr_direct = ''
        is_left_turn = False
        if zone.id == 0:
           tr_direct = 'None'
           is_left_turn = False
        elif zone.id == 1: # Northbound, straight
           tr_direct = 'North'
           is_left_turn = False
        elif zone.id == 2: # Northbound, left
           tr_direct = 'North'
           is_left_turn = True
        elif zone.id == 3: # Southbound, straight
           tr_direct = 'South'
           is_left_turn = False
        elif zone.id == 4: # Southbound, left
           tr_direct = 'South'
           is_left_turn = True
        elif zone.id == 5: # Eastbound, straight
           tr_direct = 'East'
           is_left_turn = False
        elif zone.id == 6: # Eastbound, left
           tr_direct = 'East'
           is_left_turn = True
        elif zone.id == 7: # Westbound, straight
           tr_direct = 'West'
           is_left_turn = False
        elif zone.id == 8: # Westbound, left
           tr_direct = 'West'
           is_left_turn = True
        lanes_arr.append(Lane(tr_direct, is_left_turn))
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
 
#   @param  bag_dir is a path to a directory with bin files from a ROS bag
#   @param  num_files is an integer equal to the number of files to process
#   @returns matrix of Car objects
def get_car_objs(bag_dir, num_files):
    p = Path('../binary_files')
    if(p.exists() is not True):
        sys.exit("Error: No ../binary_files folder.")
    bin_paths = []
    objs_matrix = []
    for dir in p.iterdir():
        if str(dir) == bag_dir:
            row = []
            bin_paths = list(p.glob('**/*.bin')) # gen list of paths
            i = 0
            for bin_file in range(0, num_files): # outer loop
                output = parse_output_file(bin_paths[bin_file])
                row = []
                for obj in output.objects: # inner loop
                    label = label_to_string(obj.label)
                    if(label == 'Car'): 
                        row.append(Object(label, 
                            obj.bbox.position.x, 
                            obj.bbox.position.y,
                            obj.track.velocity.x,
                            obj.track.velocity.y))
                objs_matrix.append(row)
    return objs_matrix

#   @returns dict of { #cars: traffic lane } at an intersection
def get_car_count_dict():
    parser = ArgumentParser()
    parser.add_argument('foldername', type=str)
    args = parser.parse_args()

    object_matrix = get_car_objs(args.foldername, 1) # parse only 1 file (the first one)
    car_count_dict = { 'Westbound': 0, 'Eastbound': 0, 'Southbound': 0, 'Northbound': 0}
    for obj in object_matrix[0]:
        lane = coord_to_lane(obj)
        if(lane == 'Eastbound'):
            car_count_dict['Eastbound'] += 1
        elif(lane == 'Westbound'):
            car_count_dict['Westbound'] += 1
        elif(lane == 'Southbound'):
            car_count_dict['Southbound'] += 1
        elif(lane == 'Northbound'):
            car_count_dict['Northbound'] += 1
    return car_count_dict

#   @param dict is a dictionary with keys = traffic directions and 
#   values = number of cars in each lane
#   @returns a list of the signal value each second
def get_sig_list(dict):
    q = PriorityQueue()
    my_q = ReversePriorityQueue(q)
    my_q.put((lane_time(dict['Eastbound']), 'Eastbound'))
    my_q.put((lane_time(dict['Westbound']), 'Westbound'))
    my_q.put((lane_time(dict['Southbound']), 'Southbound'))
    my_q.put((lane_time(dict['Northbound']), 'Northbound'))
    
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
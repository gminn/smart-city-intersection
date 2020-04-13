#!/usr/bin/env python3
from pathlib import Path
from argparse import ArgumentParser
from output_pb2 import OutputMessage
import sys

class Object:
    def __init__(self, type, x, y, x_vel, y_vel, lane):
        self.type = type
        self.x_pos = x
        self.y_pos = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.lane = lane
    def __str__(self):
        return str(self.type) + " located at (" + (str(self.x_pos)) + ", " + str(self.y_pos) + ") with velocity (" + (str(self.x_vel)) + ", " + str(self.y_vel) + ") in lane " + str(self.lane)
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

def label_to_string(label):
    if label == 0:
        return 'Car'
    elif label == 1:
        return 'Pedestrian'
    elif label == 2:
        return 'Cyclist'
    return 'Misc'

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

# returns reqested lane has been configured
def is_vaild_lane(lanes_arr, zone_id):
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
def populate_lanes(output):
    try:
        regions = output.region_of_interest
    except AttributeError:
        sys.exit("Error: There are no regions of interest configured in SENSR-S.")
    lanes_arr = []
    for zone in output.region_of_interest:
        
        # TODO: change which ids correspond to
        # which lane directions given test data
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

# returns whether an object has reliable tracking info
def is_reliable_tracking(object):
    try:
        if object.track.tracking_reliable == True:
            return 1
        elif  object.track.tracking_reliable == False:
            return 0
    except AttributeError:
        print(f'Tracking reliable field not set for Object #{object.id}')
        return -1

# returns matrix of objects
# parameter bag_dir is a path to a directory with bin files
# from a ROS bag
def get_intersection_objs(bag_dir):
    p = Path('../binary_files')
    if(p.exists() is not True):
        sys.exit("Error: No ../binary_files folder.")
    bin_paths = []
    objs_matrix = []
    for dir in p.iterdir():
        if str(dir) == bag_dir:
            row = []
            bin_paths = list(p.glob('**/*.bin')) # gen list of paths
            for bin_file in bin_paths: # outer loop
                output = parse_output_file(bin_file)
                row = []
                for obj in output.objects: # inner loop
                    label = label_to_string(obj.label)
                    if label != 'Misc': 
                        row.append(Object(label, 
                            obj.bbox.position.x, 
                            obj.bbox.position.y,
                            obj.track.velocity.x,
                            obj.track.velocity.y,
                            label))
                objs_matrix.append(row)
    return objs_matrix

def main():
    parser = ArgumentParser()
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    
    object_matrix = get_intersection_objs(args.filename)
    print(object_matrix)

if __name__ == '__main__':
    main();
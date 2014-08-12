

# Source: http://stackoverflow.com/questions/4804005/matplotlib-figure-facecolor-background-color
# savefig('figname.png', facecolor=fig.get_facecolor(), transparent=True)


# data = numpy.random.random((200, 300)) * 100
# print "max from data = ", numpy.max(data)

import data_map
import os
import pickle
from boundary import BoundaryContinentalUnitedStates
from map import Map
import numpy

grid = data_map.DataMap2DBayArea.make_grid()
filename = "is_in_region_bay_area.pcl"

# grid = data_map.DataMap2DWisconsin.make_grid()
# filename = "is_in_region_wisconsin.pcl"


def get_is_in_region_map(filename, grid, boundary_class):
    if os.path.isfile(filename):
        print "Loading is_in_region grid"
        with open(filename, "r") as f:
            grid = pickle.load(f)
        return grid
    else:
        print "Creating is_in_region grid"
        num_latitude_divisions = len(grid.latitudes)
        num_longitude_divisions = len(grid.longitudes)

        b = boundary_class()

        for lat_index in range(num_latitude_divisions):
            print(lat_index)
            for lon_index in range(num_longitude_divisions):
                location = (grid.get_latitude_by_index(lat_index), grid.get_longitude_by_index(lon_index))
                inside = b.location_inside_boundary(location)
                grid.set_value_by_index(lat_index, lon_index, inside)

        with open(filename, "w") as f:
            pickle.dump(grid, f)

        return grid


grid = get_is_in_region_map(filename, grid, BoundaryContinentalUnitedStates)
# map = grid.make_map()


# make_map(data)
new_map = Map(grid, is_in_region_map=grid)
new_map.add_colorbar(decimal_precision=0)
new_map.set_title("linear")

new_map.add_boundary_outlines(BoundaryContinentalUnitedStates())
# new_map.set_boundary_color('m')
# new_map.set_boundary_linewidth(20)
# new_map.make_region_background_white(grid)

# new_map.set_title("sample title")
# #new_map.set_colorbar_ticks((0, .1, .5, .9, 1))
# new_map.set_number_of_colorbar_ticks(4)
# new_map.use_integer_labels(True)
#new_map.save()
new_map.blocking_show()
# new_map.save("linear.png")

# # another_map = Map(data, transformation="log")
# # another_map.add_colorbar()
# # #another_map.set_colorbar_ticks((0, 20, 50, 100))
# # another_map.set_title("logarithmic")
# # another_map.save("log.png")
#
#
# #new_data = numpy.tril(numpy.round(numpy.random.random((200, 300)) * 4, 0) * 25)
# #new_data = numpy.matrix("[10 10 10; 30 30 30; 100 100 100]")
# new_data = numpy.matrix("[10 10 10; 30 30 30; 99 99 100]")
# third_map = Map(new_data, transformation="log")
# third_map.add_colorbar(vmax=110)
# third_map.set_title("log with discrete values")
# third_map.save("log2.png")

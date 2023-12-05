#%%
import numpy as np

def generate_staggered_rotated_points(rows, columns, x_distance, y_distance,angle_degrees):
    rotation_point=(0,0)
    #points= generate_staggered_points(rows, columns, distance_between_points)
    points=generate_staggered_points(rows, columns, x_distance, y_distance)
    points_x,points_y=rotate_points_around_point(points[0], points[1], rotation_point, angle_degrees)
    return points_x,points_y
    
# def generate_staggered_points(rows, columns, distance_between_points):
#     points = []
#     for i in range(rows):
#         offset_x = 0 if i % 2 == 0 else distance_between_points / 2
#         offset_y = i * distance_between_points * 0.75  # Adjust the multiplication factor for vertical spacing
#         row_points = np.array([(j * distance_between_points + offset_x, offset_y) for j in range(columns)])
#         points.extend(row_points)
#     return np.array(points).T

def generate_staggered_points(rows, columns, x_distance, y_distance):
    points = []
    
    for i in range(rows):
        offset_x = 0 if i % 2 == 0 else x_distance / 2
        offset_y = i * y_distance * 0.75  # Adjust the multiplication factor for vertical spacing
        row_points = np.array([(j * x_distance + offset_x, offset_y) for j in range(columns)])
        points.extend(row_points)
    
    return np.array(points).T

def cartesian_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

def polar_to_cartesian(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def rotate_points_around_point(x, y, rotation_point, angle_degrees):
    # Convert rotation_point to Cartesian coordinates
    rx, ry = rotation_point
    # Convert Cartesian to polar coordinates
    r, theta = cartesian_to_polar(x - rx, y - ry)
    # Apply rotation in polar coordinates
    theta_rotated = np.radians(angle_degrees) + theta
    # Convert back to Cartesian coordinates
    x_rotated, y_rotated = polar_to_cartesian(r, theta_rotated)
    # Translate back to the original rotation point
    x_rotated += rx
    y_rotated += ry
    return x_rotated, y_rotated

# def generate_square_grid(x_distance, y_distance, num_points_x, num_points_y):
#     coordinates = []
#     for i in range(num_points_x):
#         for j in range(num_points_y):
#             x = i * x_distance
#             y = j * y_distance
#             coordinates.append((x, y))
#     return np.array(coordinates)
# def generate_square_grid(x_distance, y_distance, num_points_x, num_points_y):
#     x_vector = []
#     y_vector = []

#     for i in range(num_points_x):
#         for j in range(num_points_y):
#             x_coord = i * x_distance
#             y_coord = j * y_distance

#             x_vector.append(x_coord)
#             y_vector.append(y_coord)

#     return np.array(x_vector), np.array(y_vector)
def generate_square_grid(x_distance, y_distance, num_points_x, num_points_y):
    x_coordinates = np.arange(num_points_x) * x_distance
    y_coordinates = np.arange(num_points_y) * y_distance

    x_vector, y_vector = np.meshgrid(x_coordinates, y_coordinates, indexing='ij')
    
    return x_vector.flatten(), y_vector.flatten()

def generate_square_grid_rotated(num_points_x, num_points_y, x_distance, y_distance, angle_degrees):
    rotation_point=(0,0)
    coordinates=generate_square_grid(x_distance, y_distance, num_points_x, num_points_y)
    points_x, points_y=rotate_points_around_point(coordinates[0], coordinates[1], rotation_point, angle_degrees)
    return points_x, points_y




# %%

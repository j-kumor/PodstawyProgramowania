#zadanie 5.2

#Complete the following program code. Then, check the program for the following data:
#a = 4 --> volume = 64, surface area = 96
#a = 7 --> volume = 343, surface area = 294

###
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side**3
cube_surface_area = 6*cube_side**2
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')
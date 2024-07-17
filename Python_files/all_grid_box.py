# Python file to obtain a .pdb file with all the grid boxes to use in VMD. There is one grid box for each frame.
import fileinput
import sys

gpf_file = (sys.argv[1])
  
for line in fileinput.input(gpf_file):
    lin_str = line
    #print lin_str[0:10]
    if (lin_str[0:4] == "npts"):
        tokens = str.split( lin_str, ' ' )
        nx = int(tokens[1])
        ny = int(tokens[2])
        nz = int(tokens[3])
    if (lin_str[0:7] == "spacing"):
        tokens = str.split( lin_str, ' ' )
        space = float(tokens[1])
    if (lin_str[0:10] == "gridcenter"):
        tokens = str.split( lin_str, ' ' )
        cx = float(tokens[1])
        cy = float(tokens[2])
        cz = float(tokens[3]) 
  
lx = space * nx
ly = space * ny
lz = space * nz
hlx = lx / 2.0
hly = ly / 2.0
hlz = lz / 2.0
x0 = cx - hlx
x1 = cx + hlx
y0 = cy - hly
y1 = cy + hly
z0 = cz - hlz
z1 = cz + hlz
size = 0.4 # Size of cross-hair
cx0 = cx - size
cx1 = cx + size
cy0 = cy - size
cy1 = cy + size
cz0 = cz - size
cz1 = cz + size
cx = str(cx) + str((6- len(str(cx))) * str( 0))
cy = str(cy) + str((6- len(str(cy))) * str( 0))
cz = str(cz) + str((6- len(str(cz))) * str( 0))

cx0 = str(cx0) + str((6- len(str(cx0))) * str( 0))
cx1 = str(cx1) + str((6- len(str(cx1))) * str( 0))
cy0 = str(cy0) + str((6- len(str(cy0))) * str( 0))
cy1 = str(cy1) + str((6- len(str(cy1))) * str( 0))
cz0 = str(cz0) + str((6- len(str(cz0))) * str( 0))
cz1 = str(cz1) + str((6- len(str(cz1))) * str( 0))

x0 = str(x0) + str((6- len(str(x0))) * str( 0))
x1 = str(x1) + str((6- len(str(x1))) * str( 0))
y0 = str(y0) + str((6- len(str(y0))) * str( 0))
y1 = str(y1) + str((6- len(str(y1))) * str( 0))
z0 = str(z0) + str((6- len(str(z0))) * str( 0))
z1 = str(z1) + str((6- len(str(z1))) * str( 0))

space = str(space)

#specify path for export 
path6 = (sys.argv[2])

#export DataFrame to text file (keep header row and index column)
with open(path6, 'a') as f:
    f.write("USER  npts " + " "  + str(nx) + " " + str(ny) + " " + str(nz)+'\n')
    f.write("USER  total_npts " + " " + str((nx +1) * (ny +1) * (nz +1))+'\n')
    f.write("USER  spacing " + " " + str(space)+'\n')
    f.write("USER  gridcenter " + " " + str(cx) + " " + str(cy) + " " + str(cz) +'\n')
    f.write("ATOM      1  O1  BOX     1      "+ str(x0)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM      2  O2  BOX     1      "+ str(x0)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM      3  O3  BOX     1      "+ str(x0)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM      4  O4  BOX     1      "+ str(x0)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM      5  O5  BOX     1      "+ str(x1)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM      6  O6  BOX     1      "+ str(x1)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM      7  O7  BOX     1      "+ str(x1)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM      8  O8  BOX     1      "+ str(x1)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM      9  C1  BOX     1      "+ str(x0)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     10  C2  BOX     1      "+ str(x0)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     11  C3  BOX     1      "+ str(x0)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     12  C4  BOX     1      "+ str(x0)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     13  C5  BOX     1      "+ str(x1)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     14  C6  BOX     1      "+ str(x1)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     15  C7  BOX     1      "+ str(x1)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     16  C8  BOX     1      "+ str(x1)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     17  N1  BOX     1      "+ str(x0)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     18  N2  BOX     1      "+ str(x0)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     19  N3  BOX     1      "+ str(x0)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     20  N4  BOX     1      "+ str(x0)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     21  N5  BOX     1      "+ str(x1)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     22  N6  BOX     1      "+ str(x1)[0:6] + "  "  + str(y0)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     23  N7  BOX     1      "+ str(x1)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     24  N8  BOX     1      "+ str(x1)[0:6] + "  "  + str(y1)[0:6] + "  " +  str(z1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     25  O9  CEN     2      "+ str(cx0)[0:6] + "  "  + str(cy)[0:6] + "  " +  str(cz)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     26  O10 CEN     2      "+ str(cx1)[0:6] + "  "  + str(cy)[0:6] + "  " +  str(cz)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     27  C9  CEN     2      "+ str(cx)[0:6] + "  "  + str(cy0)[0:6] + "  " +  str(cz)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     28  C10 CEN     2      "+ str(cx)[0:6] + "  "  + str(cy1)[0:6] + "  " +  str(cz)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     29  N9  CEN     2      "+ str(cx)[0:6] + "  "  + str(cy)[0:6] + "  " +  str(cz0)[0:6] + "  1.00  0.00"+ '\n')
    f.write("ATOM     30  N10 CEN     2      "+ str(cx)[0:6] + "  "  + str(cy)[0:6] + "  " +  str(cz1)[0:6] + "  1.00  0.00"+ '\n')
    f.write("CONECT    1    5"+ '\n')
    f.write("CONECT    2    6"+ '\n')
    f.write("CONECT    3    7"+ '\n')
    f.write("CONECT    4    8"+ '\n')
    f.write("CONECT    9   11"+ '\n')
    f.write("CONECT   10   12"+ '\n')
    f.write("CONECT   13   15"+ '\n')
    f.write("CONECT   14   16"+ '\n')
    f.write("CONECT   17   18"+ '\n')
    f.write("CONECT   19   20"+ '\n')
    f.write("CONECT   21   22"+ '\n')
    f.write("CONECT   23   24"+ '\n')
    f.write("CONECT   25   26"+ '\n')
    f.write("CONECT   27   28"+ '\n')
    f.write("CONECT   29   30"+ '\n')
    f.write('END\n')

# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
#  Determines the output shape and operation count of a convulution layer
# Parameters:
#  c_in: input channel count
#  h_in: input height count
#  w_in: input width count
#  n_filt: number of filters in the convolution layer
#  h_filt: filter height count
#  w_filt: filter width count
#  s: stride of convolution filters
#  p: amount of padding on each of the four input map sides
# Output:
#  Channel count, height count, width count
#  Number of additions, number of multiplications, number of divisions
#
# Written by Lee Wallenfang

# import Python modules
import math # math module
import sys # argv

# initialize script arguments
c_in=float('nan') #input channel count
h_in=float('nan') #input height count
w_in=float('nan') #input width count
n_filt=float('nan') #number of filters in the convolution layer
h_filt=float('nan') #filter height count
w_filt=float('nan') #filter width count
s=float('nan') #stride of convolution filters
p=float('nan') #amount of padding on each of the four input map sides

# parse script arguments
if len(sys.argv)==9:
  c_in=float(sys.argv[1]) #input channel count
  h_in=float(sys.argv[2])  #input height count
  w_in=float(sys.argv[3])  #input width count
  n_filt=float(sys.argv[4])  #number of filters in the convolution layer
  h_filt=float(sys.argv[5])  #filter height count
  w_filt=float(sys.argv[6])  #filter width count
  s=float(sys.argv[7])  #stride of convolution filters
  p=float(sys.argv[8])  #amount of padding on each of the four input map sides
else:
  print(\
   'Usage: '\
   'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'\
  )
  exit()

# write script below this line
h_out = ((h_in+2*p-h_filt)/s)+1
w_out = ((w_in+2*p-w_filt)/s)+1
muls = n_filt*h_out*w_out*c_in*h_filt*w_filt
adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
c_out = c_in
divs = 0

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
# **NXL Project**
compact yet accessible display formats

`@nptnl` and `@notseanray`
#
### **the advantage**
When writing programs to generate images, formats with compression algorithms like PNG or JPG can be very difficult to work with, while the simple PPM format is very space-intensive and generally innefficient.

The NPXL improves upon the PPM format to remain easily and procedurally formatted while significantly cutting down storage space.

The PPM file is little more a list of numbers for each color value, but these values can be varying character lengths, and hence must be separated by spaces. NPXL allows more information to be encoded into a single character with hexadecimal and base-64, standardizing each color value to one character and eliminating the need for spacing.

Effectively, NPXL saves on space by encoding more information into each character and cutting space-characters in between.

A more specific NPXL format guide exists in its own file: 
[npxl-format.md](./npxl-format.md)
# ##############################################################################
# Copyright (c) 2014, Francesco Giovannini
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the {organization} nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# ##############################################################################

# DISTINGUISHABLE_COLORS: pick colors that are maximally perceptually distinct
#
# When plotting a set of lines, you may want to distinguish them by color.
# By default, Matlab chooses a small set of colors and cycles among them,
# and so if you have more than a few lines there will be confusion about
# which line is which. To fix this problem, one would want to be able to
# pick a much larger set of distinct colors, where the number of colors
# equals or exceeds the number of lines you want to plot. Because our
# ability to distinguish among colors has limits, one should choose these
# colors to be "maximally perceptually distinguishable."
#
# This function generates a set of colors which are distinguishable
# by reference to the "Lab" color space, which more closely matches
# human color perception than RGB. Given an initial large list of possible
# colors, it iteratively chooses the entry in the list that is farthest (in
# Lab space) from all previously-chosen entries. While this "greedy"
# algorithm does not yield a global maximum, it is simple and efficient.
# Moreover, the sequence of colors is consistent no matter how many you
# request, which facilitates the users' ability to learn the color order
# and avoids major changes in the appearance of plots when adding or
# removing lines.
#
# Syntax:
#   colors = distinguishable_colors(n_colors)
# Specify the number of colors you want as a scalar, n_colors. This will
# generate an n_colors-by-3 matrix, each row representing an RGB
# color triple. If you don't precisely know how many you will need in
# advance, there is no harm (other than execution time) in specifying
# slightly more than you think you will need.
#
#   colors = distinguishable_colors(n_colors,bg)
# This syntax allows you to specify the background color, to make sure that
# your colors are also distinguishable from the background. Default value
# is white. bg may be specified as an RGB triple or as one of the standard
# "ColorSpec" strings. You can even specify multiple colors:
#     bg = {'w','k'}
# or
#     bg = [1 1 1; 0 0 0]
# will only produce colors that are distinguishable from both white and
# black.
#
#   colors = distinguishable_colors(n_colors,bg,rgb2labfunc)
# By default, distinguishable_colors uses the image processing toolbox's
# color conversion functions makecform and applycform. Alternatively, you
# can supply your own color conversion function.
#
# Example:
#   c = distinguishable_colors(25);
#   figure
#   image(reshape(c,[1 size(c)]))
#
# Example using the file exchange's 'colorspace':
#   func = @(x) colorspace('RGB->Lab',x);
#   c = distinguishable_colors(25,'w',func);
def distinguishableColors(nColors, backGround)
    

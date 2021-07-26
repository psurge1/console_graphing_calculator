import math

class linear():
    def __init__(self,linear_equation):
        str_equation = str(linear_equation)
        self.raw_equation = str_equation.replace(" ","")
        str_slope = ''
        str_y_int = ''
        space = ' '
        plus_pos = 'n/a'
        minus_pos = 'n/a'
        equation_length = len(self.raw_equation)
        #m_found = False
        #b_found = False
        self.standard_equation = []
        self.point_slope_equation = []

        for character in range(equation_length):
            if self.raw_equation[character] == '=':
                equals_pos = character
            elif self.raw_equation[character] == 'y':
                y_pos = character
            elif self.raw_equation[character] == 'x':
                x_pos = character
            elif self.raw_equation[character] == '+':
                plus_pos = character
            elif self.raw_equation[character] == '-':
                minus_pos = character

        for position_one in range(equals_pos+1,x_pos):
            str_slope += str_equation[position_one]

        if plus_pos != 'n/a' and minus_pos == 'n/a':
            for position_plus in range(plus_pos+1,equation_length):
                str_y_int += str_equation[position_plus]
                self.sign = '+'
        elif minus_pos != 'n/a' and plus_pos == 'n/a':
            for position_minus in range(minus_pos,equation_length):
                str_y_int += str_equation[position_minus]
                self.sign = '-'
        elif plus_pos != 'n/a' and minus_pos != 'n/a':
            if minus_pos > plus_pos:
                for position_minus in range(minus_pos,equation_length):
                    str_y_int += str_equation[position_minus]
            elif plus_pos > minus_pos:
                str_y_int += '-'
                for position_minus in range(plus_pos+1,equation_length):
                    str_y_int += str_equation[position_minus]
            self.sign = '-'
        else:
            print('Error')

        if '/' in str_slope:
            s_n,s_d = str_slope.split('/')
            self.m = float(s_n)/float(s_d)
        else:
           self.m = float(str_slope)

        if '/' in str_y_int:
            b_n,b_d = str_y_int.split('/')
            self.b = float(b_n)/float(b_d)
        else:
           self.b = float(str_y_int)

        self.y_intercept = self.b
        self.x_intercept = (0-self.b)/self.m 

        equation_list = ['y','=',self.m,'x',self.sign,self.b]
        self.point_slope_equation = ['y',space,'=',space,self.m,'x',space,self.sign,space,self.b]
        if self.sign == '+':
            b_sign = ''
        elif self.sign == '-':
            b_sign = '-'
        self.standard_equation = [-1*self.m,'x',space,'+',space,'y',space,'=',space,b_sign,self.b]
    
    def slope(self):
        return self.m
        
    def y_int(self):
        return self.b
        
    def x_int(self):
        return self.x_intercept
    
    def point_x(self,y):
        if self.sign == '+':
            x = (y - self.b)/self.m
        elif self.sign == '-':
            x = (y + self.b)/self.m
        return x

    def point_y(self,x):
        if self.sign == '+':
            y = self.m * x + self.b
        elif self.sign == '-':
            y = self.m * x - self.b
        return y
    
    def equation(self,form='point slope'):
        ps_equation = ''
        st_equation = ''

        for item_ps in self.point_slope_equation:
            ps_equation += str(item_ps)
        for item_s in self.standard_equation:
            st_equation += str(item_s) 

        if form == 'point slope':
            return ps_equation
        elif form == 'standard':
            return st_equation
        else:
            print('Form not supported')
    
    def console_plot(self,toplot=equation,len_x=10,len_y=10,plot_fmt='plus',scale=1,description=False):
        plot_formats = {'plus':'+','point':'.','asterisk':'*','carot':'^'}
        point = plot_formats[plot_fmt]
        str_graph = f''
        str_x_unit = '_'
        str_y_unit = '|'
        graph = []
        axis = [str_y_unit]
        x_axis = [str_y_unit]

        if isinstance(scale, int):
            self.x_factor = 2*scale
            self.y_factor = scale
        else:
            print("Err: scale isn't an integer")

        for y_unit in range(len_y-1):
            for x_unit in range(len_x*2):
                axis.append(' ')
            graph.append(axis)
            axis = [str_y_unit]
            
        for unit in range(len_x):
            x_axis.append(' ')
            x_axis.append(str_x_unit)
        graph.append(x_axis)
        
        # graph code goes here
        unit_pairs = []
        for x_unit in range(math.ceil(len_x/scale)):
            point_xy = []
            potential_y_input = self.point_y(x_unit)
            potential_y = round(potential_y_input*scale)/scale

            if potential_y < math.ceil(len_y/scale):
                point_xy.append(float(x_unit))
                point_xy.append(potential_y)
                unit_pairs.append(point_xy)

        formatted_pairs = unit_pairs
        for unit_pair in range(len(unit_pairs)):
            for coordinate_pos in range(len(unit_pairs[unit_pair])):
                formatted_pairs[unit_pair][coordinate_pos] = round(unit_pairs[unit_pair][coordinate_pos]*self.y_factor)

        #print(unit_pairs)
        #print(formatted_pairs)
        #for thing in graph:
        #    print(thing)

        for coordinate_pair in formatted_pairs:
            y_coord = -(coordinate_pair[1]+1)
            x_coord = self.x_factor*coordinate_pair[0]+1
            graph[y_coord][x_coord] = point

        a = 0
        for row in graph:
            if a != 0:
                str_graph += '\n'
            for column in row:
                str_graph += column
            a += 1

        if description:
            str_graph += '\n'
            str_graph += self.properties(scale)

        return str_graph
            

    def properties(self,g_scale=None):
        prop_string = ''
        descriptions = [
            ['',self.equation()], 
            ['Slope: ',self.m],
            ['Y-int: ',self.b], 
            ['X-int: ',self.x_intercept]
            ]
        if g_scale != None and isinstance(g_scale, int):
            descriptions.append(['Graph Scale: ',g_scale])

        b = 0
        for value in descriptions:
            if b != 0:
                prop_string += '\n'
            for property in range(len(value)):
                prop_string += str(value[property])
            b += 1

        return prop_string
    

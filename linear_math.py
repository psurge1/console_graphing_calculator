class linear():
    def __init__(self,linear_equation):
        str_equation = str(linear_equation)
        self.raw_equation = str_equation.replace(" ","")
        str_slope = ''
        str_y_int = ''
        plus_pos = 'n/a'
        minus_pos = 'n/a'
        equation_length = len(self.raw_equation)

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
            print ('Error')

        self.m = float(str_slope)
        self.b = float(str_y_int)  
        self.y_intercept = self.b
        self.x_intercept = (0-self.b)/self.m  
    
    def slope(self):
        return self.m
        
    def y_int(self):
        return self.b
        
    def x_int(self):
        return self.x_intercept
    
#    def point_x(self,y):

#    def point_y(self,x):
    
    def equation(self,form='point slope'):
        space = ' '
        ps_equation = ''
        s_equation = ''
        equation_list = ['y','=',self.m,'x',self.sign,self.b]
        if form == 'point slope':
            point_slope_equation = ['y',space,'=',space,self.m,'x',space,self.sign,space,self.b]
            for item_ps in point_slope_equation:
                ps_equation += str(item_ps)
            return ps_equation
        elif form == 'standard':
            if self.sign == '+':
                b_sign = ''
            elif self.sign == '-':
                b_sign = '-'
            standard_equation = [-1*self.m,'x',space,'+',space,'y',space,'=',space,b_sign,self.b]
            for item_s in standard_equation:
                s_equation += str(item_s)
            return s_equation
        else:
            print('Form not supported')

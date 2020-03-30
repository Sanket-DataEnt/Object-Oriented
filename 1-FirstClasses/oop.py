
class Employee:

    def __init__(self, first, last, pay):  ## self = instance(can change also but usually we use conventionally)

    ## this is called as initialiser or constructor.
	## after self, we can specify what all arguments we want to paas, these are called instance variables.

        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self): #here only self argument is required, rest other arguments it will automatically take. 
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Sanket', 'Maheshwari', 50000)
emp_2 = Employee('Test', 'Employee', 60000)







    













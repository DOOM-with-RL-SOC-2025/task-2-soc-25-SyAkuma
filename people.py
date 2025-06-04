"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : int
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        # Change the city 
        if self.city==new_city:
            return False
        else:
            self.city=new_city
            return True
        # Return true if city change, successful, return false if city same as old city

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        if self.branches.size()>1:
            return False
        elif branchmap(self.branches[0]).city==branchmap(new_code).city:
            self.branches[0]=new_code
            return True
        else:
            return False
        # Change old branch to new if it is in the same city, else return false.

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary+=increment_amt
        return 





class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        possibilities={"Junior", "Senior", "Team Lead","Director"}
        if position in possibilities:
            self.position=position
        else:
            raise ValueError("Invalid Position assigned!!")
        # Only then set the position. 

    
    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        self.salary+=amt+0.1*self.salary()
        return
        
    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        possibilities={"Junior", "Senior", "Team Lead","Director"}
        if possibilities.index(self.position)<possibilities.index(position) and position in possibilities:
            self.position=position
            self.increment(self.salary*0.3)
            return True
        elif position in possibilities:
            raise ValueError("Not a Promotion")
        else:
            raise ValueError("Invalid Designation")



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
      """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to
    position : str
    def __init__(self,name, age, ID, city, branchcodes,superior,Position="Rep", salary=None ): # Complete all this! Add arguments
        super().__init__(name, age, ID, city, branchcodes, salary)
        self.superior=superior
        self.position=Position

    
    # def promote 
    def promote(self,new_pos:str)->bool:
        possibilities={"Rep", "Manager", "Head"}
        if possibilities.index(self.position)<possibilities.index(new_pos) and new_pos in possibilities:
            self.position=new_pos
            self.increment(self.salary*0.3)
            return True
        elif new_pos in possibilities:
            raise ValueError("Not a Promotion")
        else:
            raise ValueError("Invalid Designation")
    # def increment 
    def increment(self, amt:int):
        self.salary+=amt+0.05*self.salary()
        return

    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.position=="Head":
            return None
        else:
            for man in sales_roster:
                if man.ID == self.superior:
                    sup=man.name
                    return [self.superior,sup]

    def add_superior(self) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        if self.position=="Head":
            return False
        else:
            possibilities={"Rep", "Manager", "Head"}
            for man in sales_roster:
                if man.position == possibilities(possibilities.index(self.position)+1):
                    self.superior=man.ID
                    return True
            return False


    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        self.branches.append(branchmap[new_code])
        return True
    

    





    
    
import random


class NQueens():
    def __init__(self, N):
        self.N = N
        self.state = ""
        self._set_state()
       
    def __str__(self):
       return f"NQueens Board (Size: {self.N})\n{self.state}"                                            #returns a formatted string  that represents the instance 
      
    def _set_state(self):
        choice = input("Enter 'M' to set the state manually, 'R' for a random state: ").upper()            # Display menu to the user to set the state manually or generate a random state

        if choice == 'M':
            self.state = input(f"Enter the state (length should be {self.N}): ")
        elif choice == 'R':
            self.state = self.generate_random_state()
        else:
            print("Invalid. Setting random state.")
            self.state = self.generate_random_state()

        while not self._is_valid(self.state):
            print("Invalid state.Try again.") 
            self.state = self.generate_random_state() 

    def generate_random_state(self):
        return ''.join(str(random.randint(1, self.N)) for _ in range(self.N))                      # Generate a random state string with queens placed in different rows
 
   # This is an internal function that takes a state as input and return if this is a valid state or not 
    def _is_valid(self,state):
                # Check if the state is valid based on the specified criteria
        if not state.isdigit() or len(state) != self.N:
            return False

        for i in state:
            if int(i) < 1 or int(i) > self.N:
                return False

        return True

   # This is the primary function of this class.It returns the number of attacking pairs in the given state board.
  
    def _count_attacking_pairs(self, state):
                # Count the number of attacking pairs in the given state
        attacking_pairs = 0

        for i in range(self.N):
            for j in range(i + 1, self.N):
                if state[i] == state[j] or abs(i - j) == abs(int(state[i]) - int(state[j])): # Check if queens are in the same row or diagonals
                    
                    attacking_pairs += 1

        return attacking_pairs
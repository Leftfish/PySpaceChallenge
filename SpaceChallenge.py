import random


class Item:
    """ Simulates payload """ 
    def __init__(self):
        self.name = ""
        self.weight = 10.0


class Rocket:
    """ Simulates generic rockets which never fail"""

    def __init__(self):
        self.cost = 10.0
        self.cur_weight = 8000
        self.max_weight = 10000
        self.prob_launch_fail = 0.0
        self.prob_land_fail = 0.0

    def launch(self):
        """ Indicates if the launch was successful """

        return True
    
    def land(self):
        """ Indicates if the landing was successful """

        return True

    def can_carry(self, item):
        """ Returns true if loading an Item will not make a Rocket exceed maximum weight. 
        Return false otherwise """

        return ((self.cur_weight + item.weight) <= self.max_weight)

    def carry(self, item):
        """ Updates current weight of a Rocket if Item was loaded """

        self.cur_weight += item.weight

class U1(Rocket):
    """ Simulates U1 rockets """

    def __init__(self):
        self.cost = 100000000.0
        self.cur_weight = 10000
        self.max_weight = 18000
        self.prob_launch_fail = 5.0
        self.prob_land_fail = 1.0

    def launch(self):
        """ Indicates if launch was successful. Generates a random number 0-100.
        Then compares with probabilty of failure which is 5% * (cargo carried / cargo limit)
        where cargo includes the rocket empty weight. """

        chance = random.randint(0,100)
        return ((self.prob_launch_fail * (self.cur_weight/self.max_weight)) <= chance)
    
    def land(self):
        """ Indicates if landing was successful. Generates a random number 0-100.
        Then compares with probabilty of failure which is 1% * (cargo carried / cargo limit)
        where cargo includes the rocket empty weight. """

        chance = random.randint(0,100)
        return ((self.prob_land_fail * (self.cur_weight/self.max_weight)) <= chance)

class U2(Rocket):
    """ Simulates U2 rockets """

    def __init__(self):
        self.cost = 120000000.0
        self.cur_weight = 18000
        self.max_weight = 29000
        self.prob_launch_fail = 4.0
        self.prob_land_fail = 8.0

    def launch(self):
        """ Indicates if launch was successful. Generates a random number 0-100.
        Then compares with probabilty of failure which is 4% * (cargo carried / cargo limit)
        where cargo includes the rocket empty weight. """

        chance = random.randint(0,100)
        return ((self.prob_launch_fail * (self.cur_weight/self.max_weight)) <= chance)
    
    def land(self):
        """ Indicates if landing was successful. Generates a random number 0-100.
        Then compares with probabilty of failure which is 8% * (cargo carried / cargo limit)
        where cargo includes the rocket empty weight. """

        chance = random.randint(0,100)
        return ((self.prob_land_fail * (self.cur_weight/self.max_weight)) <= chance)

class Simulation:
    """ Simulates payload loading and space missions """

    def __init__(self):
        print("Simulation initiated. Awaiting payload and rocket data.")
    
    def load_items(self, pathname):
        """ Reads payload from a text file. 
        Assumes each line is payload_name=weight where weight must be int. 
        Returns a list of Items. """

        payload_manifest = []

        try:
            file = open(pathname,'r')
            for line in file:
                new_item = Item()
                new_item.weight = int(line.split('=')[1].rstrip())
                payload_manifest.append(new_item)
            return payload_manifest
        
        except Exception as e:
            print("File with payload manifest not found (or worse). Details: " + str(e.args))

    def load_rockets(self, payload, rocket_type = ""):
        """ Creates and fills rockets with payload until the manifest is empty.
        Returns list of Rockets. If 100+ launches would be needed, returns an empty list """

        new_rockets = []
        try:
            while len(payload) > 0:
                if rocket_type == "u1":
                    new_vehicle = U1()
                elif rocket_type == "u2":
                    new_vehicle = U2()
                else:
                    new_vehicle = Rocket()
                
                if len(new_rockets) > 100:
                    new_rockets = []
                    print("You would need more than 100 launches. Redesign the vehicle or rethink the payload structure.")
                    return new_rockets

                for item in payload[:]:
                    if new_vehicle.can_carry(item):
                        new_vehicle.carry(item)
                        payload.remove(item)

                new_rockets.append(new_vehicle)

            # print(str(len(new_rockets)) + " rockets were successfully loaded.")
            return new_rockets
        
        except Exception as e:
            print("Unable to prepare launch vehicles: " + str(e.args))
            return []

    def run_simulation(self,vehicles):
        """ Simulates rocket launches and landings.
        Launch is repeated in case of failure. Cost of each launch
        is counted towards total cost of sending payload. Returns total cost. """

        total_cost = 0.0
        i = 0
        successful_missions = 0
        failed_missions = [0,0]
        
        if not vehicles:
            return 

        while i < len(vehicles):
            mission = vehicles[i]
            
            if mission.launch() and mission.land():
                i += 1
                successful_missions += 1
                total_cost += mission.cost
            elif not mission.launch():
                failed_missions[0] += 1
                total_cost += mission.cost
            else:
                failed_missions[1] += 1
                total_cost += mission.cost
        
        # print("Total cost: " + '{:20,.2f}'.format(total_cost)) 
        # print(str(successful_missions) + " successful missions")
        # print(str(sum(failed_missions)) + " failures (" + str(failed_missions[0]) + " launch, "  + str(failed_missions[1]) + " landing)")

        return total_cost

def main():
    sim = Simulation()
    manifest = sim.load_items("phase-1.txt")
    vehicles = sim.load_rockets(manifest,"u1")
    print("Total cost for U1 rockets in Phase 1: " + str(sim.run_simulation(vehicles)))
    
if __name__ == "__main__":
    main()
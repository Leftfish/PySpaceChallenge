import SpaceChallenge as SC
from statistics import mean

avg_totalcost_u1 = [0.0,0.0]
avg_totalcost_u2 = [0.0,0.0]
sim = SC.Simulation()

def run_one_sim(manifest_pathname,rocket_type):
    manifest = sim.load_items(manifest_pathname)
    vehicles = sim.load_rockets(manifest,rocket_type)
    return sim.run_simulation(vehicles)

def run_x_sims(manifest_pathname,rocket_type,output_list,phase,x):
    all_results = []
    for n in range(1,x):
        all_results.append(run_one_sim(manifest_pathname,rocket_type))
    output_list[phase-1] = mean(all_results)

## Change x to change the number of simulations.

x = 1000

print("Running " + str(x) + " simulations for each rocket type and Phase...")

run_x_sims("phase-1.txt","u1",avg_totalcost_u1,1,x)
run_x_sims("phase-1.txt","u2",avg_totalcost_u2,1,x)
run_x_sims("phase-2.txt","u1",avg_totalcost_u1,2,x)
run_x_sims("phase-2.txt","u2",avg_totalcost_u2,2,x)

print("Average total cost if U1 rockets are used:" + 
'\n' + '{:20,.2f}'.format(avg_totalcost_u1[0]) + 
" for Phase 1" + '\n' + '{:20,.2f}'.format(avg_totalcost_u1[1]) + " for Phase 2")

print("Average total cost if U2 rockets are used:" + 
'\n' + '{:20,.2f}'.format(avg_totalcost_u2[0]) + 
" for Phase 1" + '\n' + '{:20,.2f}'.format(avg_totalcost_u2[1]) + " for Phase 2")
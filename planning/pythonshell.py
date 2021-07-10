import subprocess
# import execution.execution
# import classes.ground_robot
# import classes.gantry_robot

def plan(planner_folder):

    # root directory of the planner
    # planner_folder = '/home/brenda/Desktop/popf-tif-clp/planner/debug/popf'


    # Shon's Test file path
    planner_folder = '/home/luna/Desktop/popf-tif-clp/planner/debug/popf'
    # planner_folder = '/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf'


    # domain file
    domain_file = planner_folder + '/rwa2-domain.pddl'
    # problem file
    problem_file = planner_folder + '/rwa2-problem.pddl'
    # planner binary to execute on domain and problem files
    planner = f'{planner_folder}/popf3-clp {domain_file} {problem_file}'

    # bash command execution from Python
    planner_cmd = ['bash', '-c', planner]
    process = subprocess.Popen(planner_cmd, stdout=subprocess.PIPE)

    for line in process.stdout:
        print(line)
        if "b'0" in str(line):
            result = str(line)[str(line).find('(') + 1:str(line).find(')')]
            print(result)
    process.wait()


    system_tracker = {"bins": {"red battery": {"parts": "3", "location": "1"}, "blue battery": {"parts": "2", "location": "2"},
                          "blue sensor": {"parts": "1", "location": "3"}, "green regulator": {"parts": "5", "location": "4"}},
                 "agv": {"selected": "agv2", "current station": 'as1', "remaining stations": ('agv1', 'agv3', 'agv4')},
                 "kit":  {"red battery": "2", "blue battery": "2", "blue sensor": "1", "green regulator": "1"},
                 "kit total": "6"}

    # gnd = classes.ground_robot.Ground('Shon', 2.0, ['s', 'a'], 1.0, 'NIST')
    # gnt = classes.gantry_robot.Gantry('Shon', 2.0, ['s', 'a'], 1.0, 2.0, 10, 11, 'NIST')
    # execution.execution.execute_plan(result, gnd, gnt, system_tracker)

    # print(process.returncode)

if __name__ == '__main__':

    # root directory of the planner
    # planner_folder = '/home/brenda/Desktop/popf-tif-clp/planner/debug/popf'


    # Shon's Test file path
    planner_folder = '/home/luna/Desktop/popf-tif-clp/planner/debug/popf'
    # planner_folder = '/home/so

    plan(planner_folder)
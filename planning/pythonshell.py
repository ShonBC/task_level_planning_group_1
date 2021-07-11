import subprocess

def plan(planner_folder):
    """[summary]

    Args:
        planner_folder ([type]): [description]

    Returns:
        [type]: [description]
    """

    # domain file
    domain_file = planner_folder + '/rwa2-domain.pddl'
    # problem file
    problem_file = planner_folder + '/rwa2-problem.pddl'
    # planner binary to execute on domain and problem files
    planner = f'{planner_folder}/popf3-clp {domain_file} {problem_file}'

    # bash command execution from Python
    planner_cmd = ['bash', '-c', planner]
    process = subprocess.Popen(planner_cmd, stdout=subprocess.PIPE)

    moves = []
    for line in process.stdout:
        # print(line)
        if "b'0" in str(line):
            result = str(line)[str(line).find('(') + 1:str(line).find(')')]
            # print(result)
            moves.append(result)
    process.wait()

    # print(process.returncode)

    return moves
   

if __name__ == '__main__':

    # root directory of the planner
    # planner_folder = '/home/brenda/Desktop/popf-tif-clp/planner/debug/popf'


    # Shon's Test file path
    planner_folder = '/home/luna/Desktop/popf-tif-clp/planner/debug/popf'
    # planner_folder = '/home/souvik/Documents/ENPM809E/Resources/L8-Task_Level_Planning/popf-tif-clp/planner/debug/popf'


    plan(planner_folder)
import subprocess

# root directory of the planner
planner_folder = '/home/brenda/Desktop/popf-tif-clp/planner/debug/popf'
# domain file
domain_file = planner_folder + '/rwa2-domain.pddl'
# problem file
problem_file = planner_folder + '/rwa2-updated-problem.pddl'
# planner binary to execute on domain and problem files
planner = f'{planner_folder}/popf3-clp {domain_file} {problem_file}'


if __name__ == '__main__':
    # bash command execution from Python
    planner_cmd = ['bash', '-c', planner]
    process = subprocess.Popen(planner_cmd, stdout=subprocess.PIPE)

    for line in process.stdout:
        print(line)
        if "b'0" in str(line):
            result = str(line)[str(line).find('(') + 1:str(line).find(')')]
            print(result)
    process.wait()

    # print(process.returncode)
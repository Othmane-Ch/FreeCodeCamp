import re


def arithmetic_arranger(problems, solve=False):
    #   ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    #    32      3801      45      123 \n+ 698    -    2    + 43    +  49\n-----    ------    ----    -----
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for problem in problems:
        # look for operation
        if re.search("[^\s0-9+-]", problem):
            if re.search("[/]",problem) or re.search("[*]",problem):
                return "Error: Operator must be '+' or '-'."
            else :
              return "Error: Numbers must only contain digits."
        operand1 = problem.split()[0]
        operation = problem.split()[1]
        operand2 = problem.split()[2]
        result = ""
        if operation == '+':
            result = str(int(operand1) + int(operand2))
        elif operation == '-':
            result = str(int(operand1) - int(operand2))
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        length = max(len(operand1), len(operand2)) + 2
        l1 = str(operand1).rjust(length)
        l2 = operation+ str(operand2).rjust(length - 1)
        l3 = ''
        for i in range(length):
            line3 += '-'

        l4 = result.rjust(length)
        if problem != problems[-1]:
            line1 += l1 + '    '
            line2 += l2 + '    '
            line3 += l3 + '    '
            line4 += l4 + '    '
        else :
          line1 += l1
          line2 += l2
          line3 += l3
          line4 += l4
    if solve:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
    else:
        arranged_problems = line1 + '\n' + line2 + '\n' + line3
    return arranged_problems


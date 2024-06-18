def arithmetic_arranger(problems, show_answers=False):
    result = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        operation = problem.split(' ')
        operand_1 = operation[0]
        operator = operation[1]
        operand_2 = operation[2]
        if operator not in ["+", "-"]:
            return ("Error: Operator must be '+' or '-'.")
        if (len(operand_1) and len(operand_2))>4:
            return 'Error: Numbers cannot be more than four digits.'
        if (not operand_1.isdigit()) or (not operand_2.isdigit()):
            return 'Error: Numbers must only contain digits.' 

        if len(operand_2)>len(operand_1):
            space = len(operand_2)+1
        else:
            space = len(operand_1)+1
        bottom_row = operator+operand_2.rjust(space)
        
        underline = '-'*len(bottom_row)
        top_indent = ' '*abs(len(operand_1)-len(bottom_row))
        top_row = top_indent+operand_1
        solution = eval(problem)
        answer = str(solution)
        ans_indent = ' '*abs(len(answer)-len(bottom_row))
        ans_row = ans_indent+str(solution)
        if show_answers:
            arranged_problem = [top_row,bottom_row,underline,ans_row]
            result.append(arranged_problem)
            transposed = list(zip(*result))
            horizontal_layout = ['    '.join(lines) for lines in transposed]
        else:
            arranged_problem = [top_row,bottom_row,underline]
            result.append(arranged_problem)
            transposed = list(zip(*result))
            horizontal_layout = ['    '.join(lines) for lines in transposed]

    return '\n'.join(horizontal_layout)

# print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
# print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"], True)}')
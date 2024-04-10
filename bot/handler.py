import database

# function or class
# string (input message) -> string (output message)

# if input message (command) is openings <company-name> 
    # go to database fetch company deets, return as string

# implement some list of commands

def leetcode_getProblems(args:list[str]):
    try:
        List = database.LeetScraper.GetProblemLinks(args[1])
        if len(args) == 3:
            return '\n'.join([List[i] for i in range(int(args[2]))])
        elif len(args) == 2:
            return '\n'.join([List[i] for i in range(min(10, len(List)))])
        else:
            return "Error: Either too many or too less parameter"
    except Exception as e:
        print(e)
        return "Error"
    
def leetcode_getQuestion(args:list[str]):
    try:
        if len(args) == 2:
            return database.LeetScraper.GetQuestion(args[1])
        else:
            return "Error: Either too many or too less parameter"
    except Exception as e:
        print(e)
        return "Error"

def leetcode_getAnswer(args: list[str]):
    try:
        if len(args) == 2:
            return database.LeetScraper.GetAnswers(args[1])
        else:
            return "Error: Either too many or too less parameter"
    except Exception as e:
        print(e)
        return "Error"
    
def leetcode_getProblemByTag(args: list[str]):
    try:
        List = database.LeetScraper.GetProblemFromTag(args[1])
        if len(args) == 3:
            return '\n'.join([List[i] for i in range(int(args[2]))])
        elif len(args) == 2:
            return '\n'.join([List[i] for i in range(min(10, len(List)))])
        else:
            return "Error: Either too many or too less parameter"
    except Exception as e:
        print(e)
        return "Error"
    
def leetcode_getSolutionStats(args: list[str]):
    try:
        if len(args) != 4:
            return "Error: Either too many or too less parameter"
        else:
            question_url = args[1]
            language = args[2]
            solution = args[3]
            return database.LeetScraper.GetSolutionStats(question_url, language, solution)
    except Exception as e:
        print(e)
        return "Error"
    
def help(args: list[str]):
    try:
        if len(args) == 1:
            print([i+"\n" for i in commands])
        else:
            return "Error: Either too many or too less parameter"
    except Exception as e:
        print(e)
        return "Error"
    
commands = {
            "leetcode-getProblems": leetcode_getProblems,
            "leetcode-getQuestion":leetcode_getQuestion,
            "leetcode-getAnswer": leetcode_getAnswer,
            "leetcode-getProblemByTag": leetcode_getProblemByTag,
            "leetcode-getSolutionStats": leetcode_getSolutionStats,
            "help": help
            }

class QueryHandler:
    def ans_query(s: str) -> str:
        if s[0] != "!":
            return

        split_query=s[1:].split()
        
        if split_query[0] in commands:
            return commands[split_query[0]](split_query)
        else:
            return "Error! Unknown Query"

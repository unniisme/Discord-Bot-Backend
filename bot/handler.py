import database

# function or class
# string (input message) -> string (output message)

# if input message (command) is openings <company-name> 
    # go to database fetch company deets, return as string

# implement some list of commands
class QueryHandler:
    def ans_query(s: str) -> str:
        if s[0] != "!":
            return

        split_query=s[1:].split()


        # if split_query[0]=='company-openings':
        #     try:
        #         company_openings_list=database.CompanyDatabaseHandle().GetCompanyOpenings(split_query[1])
        #         return ''.join([opening+'\n'] for opening in company_openings_list)
        #     except:
        #         return "Error! Enter a company name." #returns error message with suggestion

        # elif split_query[0]=='skill-openings':
        #     skill_openings_list=database.CompanyDatabaseHandle().GetSkillOpenings(split_query[1:])
        #     return ''.join([opening+'\n'] for opening in skill_openings_list)

        # elif split_query[0]=='company-details':
        #     try:
        #         company_details=database.CompanyDatabaseHandle().GetCompanyDetails(split_query[1])
        #         return ''.join([detail+'\n'] for detail in company_details)
        #     except:
        #         return "Error! Enter a company name." #returns error message with suggestion

        if split_query[0]=="leetcode-getProblems":
            try:
                List = database.LeetScraper.GetProblemLinks(split_query[1])
                if len(split_query) == 3:
                    return '\n'.join([List[i] for i in range(int(split_query[2]))])
                elif len(split_query) == 2:
                    return '\n'.join([List[i] for i in range(min(10, len(List)))])
                else:
                    return "Error: Either too many or too less parameter"
            except Exception as e:
                print(e)
                return "Error"
        
        elif split_query[0]=="leetcode-getQuestion":
            try:
                if len(split_query) == 2:
                    return database.LeetScraper.GetQuestion(split_query[1])
                else:
                    return "Error: Either too many or too less parameter"
            except Exception as e:
                print(e)
                return "Error"

        elif split_query[0]=="leetcode-getAnswer":
            try:
                if len(split_query) == 2:
                    return database.LeetScraper.GetAnswers(split_query[1])
                else:
                    return "Error: Either too many or too less parameter"
            except Exception as e:
                print(e)
                return "Error"
            
        elif split_query[0]=="leetcode-getProblemByTag":
            try:
                List = database.LeetScraper.GetProblemFromTag(split_query[1])
                if len(split_query) == 3:
                    return '\n'.join([List[i] for i in range(int(split_query[2]))])
                elif len(split_query) == 2:
                    return '\n'.join([List[i] for i in range(min(10, len(List)))])
                else:
                    return "Error: Either too many or too less parameter"
            except Exception as e:
                print(e)
                return "Error"

        else:
            return "Error! Unknown Query"
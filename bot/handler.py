import database

# function or class
# string (input message) -> string (output message)

# if input message (command) is openings <company-name> 
    # go to database fetch company deets, return as string

# implement some list of commands
class QueryHandler:
    def ans_query(s: str) -> str:
        split_query=s.split()
        if split_query[0]=='company-openings':
            try:
                company_openings_list=database.CompanyDatabaseHandle().GetCompanyOpenings(split_query[1])
                return ''.join([opening+'\n'] for opening in company_openings_list)
            except:
                return "Error! Enter a company name." #returns error message with suggestion

        elif split_query[0]=='skill-openings':
            skill_openings_list=database.CompanyDatabaseHandle().GetSkillOpenings(split_query[1:])
            return ''.join([opening+'\n'] for opening in skill_openings_list)

        elif split_query[0]=='company-details':
            try:
                company_details=database.CompanyDatabaseHandle().GetCompanyDetails(split_query[1])
                return ''.join([detail+'\n'] for detail in company_details)
            except:
                return "Error! Enter a company name." #returns error message with suggestion

        else:
            return "Error! Unknown Query"
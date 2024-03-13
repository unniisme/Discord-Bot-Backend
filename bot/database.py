# interface for database
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from Leetcode import LeetScraper as ls 




class DataBaseHandler:
    """
    For fetching data from the database
    """

    def GetTable(table_name : str) -> dict:
        """
        Get a table given a name
        """
        return {}


class CompanyDatabaseHandle(DataBaseHandler):
    """
    For performing functions on the database.
    """

    def GetCompanyOpenings(company_name : str) -> list[str]:
        """
        Get the details of the openings in a particular company.
        """
        return []
    
    def GetSkillOpenings(skill_set : list) -> list[str]:
        """
        Get the details of the openings relevant to the provided skill set
        """
        return []
    
    def GetCompanyDetails(company_name : str) -> list[str]:
        """
        Get the details of the company asked for.
        """
        return []

class LeetScraper:

    def GetProblemLinks (companyName: str ) -> list[str]:
        return ls.get_questions_for_company(companyName)
    
    def GetProblemFromTag(tag : str) -> list[str]:
        return ls.get_questions_for_tags(tag)

    def GetQuestion (link:str) -> str:
        return ls.Get_Question(link)
    
    def GetAnswers (link:str) -> str:
        return ls.Get_Answers(link)
    
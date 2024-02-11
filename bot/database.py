# interface for database

class DataBaseHandler:
    """
    For fetching data from the database
    """

    def GetTable(table_name : str) -> dict:
        """
        Get a table given a name
        """

        # 
        return {}


class CompanyDatabaseHandle(DataBaseHandler):

    def GetOpenings(company_name : str) -> list[str]:
        return []
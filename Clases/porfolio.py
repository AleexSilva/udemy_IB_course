class InvestmentPortdolio:
    """
    Class that manage the investment of a Portfolio
    """
    def __init__(self):
        """
        iniciate a portfolio investment from an empty list
        """
        self.investment = []
    
    def add_investment(self,asset_name,capital,expected_profitability):
        """
        Add a new investment to the porfolio
        Params:
            - asset_name: Finantial instument name (ex: AAPL, BTC)
            - capital: investment capital for this asset
            - expected_profitability:  pct of expected profitability fot this asset 
        """
        # Add investment to the porfolio
        investment = {
            "Asset": asset_name,
            "capital": capital,
            "Expected_profitability": expected_profitability 
        }
        
        self.investment.append(investment)
        print(f"Investment on {asset_name}: ${capital} wiht an expected profitability: {expected_profitability}%")
        
        
    def total_profitability(self):
        """
        calculate the total expected profitability from all the portfolio 
        """
        
        total_rentability = 0
        for inv in self.investment:
            # profitability for each investment = capital * (profitability/100)
            total_rentability+= inv["capital"] * (inv['profitability']/100)
        
        print(f"Total expected profitability from the portfolio: {total_rentability:.2f} ")
class InvestmentPortdolio:
    """
    Class that manage the investment of a Portfolio
    """
    def __init__(self):
        """
        iniciate a portfolio investment from an empty list
        """
        self.investments = []
    
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
            "Capital": capital,
            "Expected_profitability": expected_profitability 
        }
        
        self.investments.append(investment)
        print(f"Investment on {asset_name}: ${capital} with an expected profitability: {expected_profitability}%")
        
        
    def total_profitability(self):
        """
        calculate the total expected profitability from all the portfolio 
        """
        
        total_rentability = 0
        for inv in self.investments:
            # profitability for each investment = capital * (profitability/100)
            total_rentability+= inv["Capital"] * (inv['Expected_profitability']/100)
        
        print(f"Total expected profitability from the portfolio: {total_rentability:.2f} ")
        
        return total_rentability
    
    def show_investments(self):
        """
        Show all the investments from the protfolio
        """
        if len(self.investments) == 0:
            print("There are no investment on the portfolio")
        else:
            print('Investment Portfolio:')
            print('\n')
            for inv in self.investments:
                print(f'- Asset: {inv['Asset']}, Capital: {inv['Capital']}, Profitability: {inv['Expected_profitability']}%')
            
# How to use: Investment Portfolio

# Instance creation:
portfolio = InvestmentPortdolio()

# Add investment
portfolio.add_investment(asset_name='AAPL', capital=1000, expected_profitability=8)
portfolio.add_investment(asset_name='GOOGL', capital=800, expected_profitability=10)
portfolio.add_investment(asset_name='BTC', capital=600, expected_profitability=20)

# Show all the investments
portfolio.show_investments()

# Expected profitability
portfolio.total_profitability()
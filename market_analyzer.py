from typing import Dict, Any
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MarketAnalyzer:
    """Analyzes market conditions and provides insights."""
    
    def __init__(self):
        self.data_collector = DataCollector()
        
    async def analyze_market(self) -> Dict[str, Any]:
        """Performs predictive analysis on collected data."""
        try:
            external_data = await self.data_collector.fetch_data("external")
            
            # Convert to DataFrame for easier manipulation
            df = pd.DataFrame(external_data["api/market/analytics"])
            
            # Calculate moving averages
            df['MA_5'] = df['price'].rolling(5).mean()
            df['MA_20'] = df['price'].rolling(20).mean()
            
            analysis = {
                "trend": "UP" if df['MA_5'][-1] > df['MA_20'][-1] else "DOWN",
                "strength": max(df['volume']) / min(df['volume'])
            }
            
            return analysis
            
        except Exception as e:
            logger.error(f"Market analysis failed: {str(e)}")
            raise
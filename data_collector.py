import aiohttp
from typing import Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataCollector:
    """Collects internal operational data and external market data."""
    
    def __init__(self):
        self.data_sources = {
            "internal": ["api/internal/operations", "api/internal/finance"],
            "external": ["api/market/analytics", "api/news/updates"]
        }
        
    async def fetch_data(self, source_type: str) -> Dict[str, Any]:
        """Fetches data from specified sources and returns parsed results."""
        try:
            session = aiohttp.ClientSession()
            collected_data = {}
            
            for endpoint in self.data_sources[source_type]:
                async with session.get(endpoint) as response:
                    if response.status == 200:
                        data = await response.json()
                        collected_data[endpoint] = data
                    else:
                        logger.error(f"Failed to fetch data from {endpoint}. Status: {response.status}")
            
            return collected_data
            
        except Exception as e:
            logger.error(f"Error in fetching data: {str(e)}")
            raise
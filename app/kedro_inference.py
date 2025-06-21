from pathlib import Path
import pandas as pd
from kedro.framework.session import KedroSession
from kedro.io import MemoryDataSet

# Find the project root directory (parent of app directory)
PROJECT_PATH = Path(__file__).resolve().parents[1]

def run_inference(user_df):
    """Run Kedro data processing pipeline on user input data.
    
    Args:
        user_df: DataFrame containing user input data
        
    Returns:
        Preprocessed DataFrame ready for the model
    """
    with KedroSession.create(project_path=PROJECT_PATH) as session:
        # Get the context to access the catalog
        context = session.load_context()
        
        # Inject user data as raw_calories
        context.catalog.add("raw_calories", MemoryDataSet(user_df))
        
        # Run the data processing pipeline
        session.run(pipeline_name="data_processing")
        
        # Load and return the preprocessed data
        return context.catalog.load("preprocessed_calories")


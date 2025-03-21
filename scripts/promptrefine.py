from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM  # Updated import
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PromptRefiner:
    """A class to handle prompt evaluation and refinement through multiple stages."""
    
    def __init__(self, model_name: str = "qwen2.5:1.5b"):
        """Initialize the LLM and prompt chains."""
        try:
            self.llm = OllamaLLM(model=model_name)  # Updated class, removed request_timeout
            self._setup_chains()
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {str(e)}")
            raise

    def _setup_chains(self):
        """Set up the prompt processing chains."""
        # Step 1: Prompt Evaluation
        self.evaluation_chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate(
                input_variables=["raw_prompt"],
                template="""
                You are an expert prompt engineer. Evaluate the following ChatGPT prompt for clarity and effectiveness:
                
                "{raw_prompt}"
                
                Provide a detailed critique including:
                - Clarity and structure: Is the prompt easy to understand and well-organized?
                - Ambiguity: Are there any vague or confusing parts?
                - Improvements: Suggest specific changes to enhance effectiveness.
                - Explanations: Briefly justify each recommendation.
                """
            )
        )

        # Step 2: Prompt Rewriting
        self.rewriting_chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate(
                input_variables=["raw_prompt", "evaluation"],
                template="""
                Based on the evaluation below, rewrite this ChatGPT prompt to improve clarity and effectiveness:
                
                Original Prompt: "{raw_prompt}"
                Evaluation: "{evaluation}"
                
                Improved Prompt:
                """
                """
                """
            )
        )

        # Step 3: Prompt Optimization
        self.optimization_chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate(
                input_variables=["rewritten_prompt"],
                template="""
                Optimize this ChatGPT prompt for maximum clarity and effectiveness:
                
                "{rewritten_prompt}"
                
                - Identify missing details or unclear aspects.
                - Suggest refinements to improve precision and intent.
                - Provide the fully optimized version.
                """
            )
        )

        # Step 4: Final Consolidation
        self.final_chain = LLMChain(
            llm=self.llm,
            prompt=PromptTemplate(
                input_variables=["optimized_prompt"],
                template="""
                Finalize this ChatGPT prompt, ensuring it is clear, structured, and effective:
                
                "{optimized_prompt}"
                
                Final Prompt:
                """
                """
                """
            )
        )

    def refine_prompt(self, raw_prompt: str) -> Optional[str]:
        """Refine the raw prompt through all stages."""
        try:
            logger.info("Starting prompt refinement process")
            
            evaluation = self.evaluation_chain.run(raw_prompt=raw_prompt)
            if not evaluation:
                raise ValueError("Evaluation stage returned empty result")
                
            rewritten_prompt = self.rewriting_chain.run(raw_prompt=raw_prompt, evaluation=evaluation)
            if not rewritten_prompt:
                raise ValueError("Rewriting stage returned empty result")
                
            optimized_prompt = self.optimization_chain.run(rewritten_prompt=rewritten_prompt)
            if not optimized_prompt:
                raise ValueError("Optimization stage returned empty result")
                
            final_prompt = self.final_chain.run(optimized_prompt=optimized_prompt)
            if not final_prompt:
                raise ValueError("Final consolidation stage returned empty result")
                
            logger.info("Prompt refinement completed successfully")
            return final_prompt.strip()
            
        except Exception as e:
            logger.error(f"Error during prompt refinement: {str(e)}")
            return None

def main():
    """Example usage of the PromptRefiner class."""
    refiner = PromptRefiner()
    raw_prompt = "Generate a CV using the user’s work experience. Make it professional and optimized for ATS."
    
    refined_prompt = refiner.refine_prompt(raw_prompt)
    if refined_prompt:
        print("Final Optimized Prompt:")
        print(refined_prompt)
    else:
        print("Failed to refine prompt. Check logs for details.")

if __name__ == "__main__":
    main()
import argparse
from chatbot import rag_chain  # Ensure you import rag_chain correctly

# Set up argument parsing
parser = argparse.ArgumentParser(description='Invoke the rag_chain with a question.')
parser.add_argument('question', type=str, help='The question to invoke rag_chain with.')

# Parse the command-line arguments
args = parser.parse_args()

# Use the provided question to invoke rag_chain
response = rag_chain.invoke(args.question)
print(response)

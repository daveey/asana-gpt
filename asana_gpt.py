import argparse
from ast import arg
import logging
import os
from reader.asana_reader import AsanaReader
from gpt_index import GPTSimpleVectorIndex

if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument(
        "--asana-token",
        type=str,
        help="Asana token.",
    )
    argparse.add_argument(
        "--workspace",
        type=str,
        required=True,
        help="Asana workspace.",
    )
    argparse.add_argument(
        "--openai-key",
        type=str,
        required=True,
        help="OpenAI API key.",
    )
    argparse.add_argument(
        "--query", type=str, required=False, help="Question for the workspace."
    )
    argparse.add_argument(
        "--chat", action="store_true", help="Chat with the workspace."
    )
    args = argparse.parse_args()
    os.environ["OPENAI_API_KEY"] = args.openai_key
    os.environ["TOKENIZERS_PARALLELISM"] = "false"

    if os.path.exists(f"index.{args.workspace}.json"):
        index = GPTSimpleVectorIndex.load_from_disk(f"index.{args.workspace}.json")
    else:
        logging.info("Index not found, creating it...")
        reader = AsanaReader(args.asana_token)
        logging.info("Downloading Projects...")
        documents = reader.load_data(workspace_id=args.workspace)
        logging.info("Creating index, this will take a while...")
        index = GPTSimpleVectorIndex(documents)
        index.save_to_disk(f"index.{args.workspace}.json")

    if args.query:
        results = index.query(args.query)
        logging.info(results)

    if args.chat:
        while True:
            query = input("Query: ")
            results = index.query(query, similarity_top_k=5)
            logging.info("=====================================")
            logging.info(results)
            logging.info("=====================================")
            for s in results.source_nodes:
                if s.extra_info and "task_id" in s.extra_info:
                    logging.info("    > " + s.extra_info.get("name"))

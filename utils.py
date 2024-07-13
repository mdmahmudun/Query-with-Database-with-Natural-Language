from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.utilities import SQLDatabase



from examples import examples

import dotenv
dotenv.load_dotenv()


llm = GoogleGenerativeAI(model="models/text-bison-001",  temperature=0.2)



def get_chain():
    db_user = 'root'
    db_password = 'root'
    db_host = 'localhost'
    db_name = 'world_layoffs'

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    to_vectorize = [" ".join(example.values()) for example in examples]

    vector_store = FAISS.from_texts(to_vectorize, embeddings, metadatas = examples)
    
    example_selector = SemanticSimilarityExampleSelector(
    vectorstore = vector_store,
    k = 2,
    )


    prompt = PromptTemplate(
        input_variables = ['Question', 'SQLQuery', 'SQLResult', 'Answer'],
        template = "\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
    )

    few_shot_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = prompt,
    prefix = _mysql_prompt,
    suffix = PROMPT_SUFFIX,
    input_variables = ['input', 'table_info', 'top_k']
    )
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=False, prompt=few_shot_prompt, return_intermediate_steps = True)

    return chain


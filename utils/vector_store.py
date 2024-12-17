from faiss import IndexFlatL2,write_index,read_index
import numpy as np
from utils.convert_embedding import GetEmbedding


class VectorStore:
    def __init__(self):
        pass

    def store_vectors(self,data:list,embedding_space_name:str = 'faiss_index.index',numpy_emb_space:str = 'embeddings.npy' ):
        try:
            embeddings = GetEmbedding(data=data).convert_emb()
            diamension = embeddings.shape[1]
            print("Diamension",diamension)
            # Create L2 distance index
            index = IndexFlatL2(diamension)

            index.add(embeddings)

            write_index(index, embedding_space_name)

            # Save embeddings to file
            np.save(numpy_emb_space, embeddings)
            return True
        except Exception as e:
            print(e)
            return False

    def get_similary_search(self,query,embedding_space_name:str = 'faiss_index.index',numpy_emb_space:str = 'embeddings.npy',K:int= 1):
        # Load the FAISS index
        index = read_index('faiss_index.index')

        # Load the embeddings
        embeddings_np = np.load('embeddings.npy')

        # Now you can perform similarity searches on the index
        query = "What is photosynthesis?"
        query_embedding = GetEmbedding([query]).convert_emb()
        query_embedding = query_embedding.detach().numpy()
        # query_embedding = np.array(query_embedding)  # Convert to numpy array
        # query_embedding = query_embedding.reshape(1, -1)
        # print("shape")
        # print(query_embedding.shape)
        # Perform search
        distances, indices = index.search(query_embedding, k = K)

        return indices




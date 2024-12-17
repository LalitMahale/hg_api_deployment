from sentence_transformers import SentenceTransformer

class GetEmbedding:
    def __init__(self,data:list):
        self.data = data
    def convert_emb(self,model_name:str = "sentence-transformers/all-MiniLM-L6-v2"):
        try:
            model = SentenceTransformer(model_name_or_path=model_name)
            embedding = model.encode(self.data, convert_to_tensor=True)
            return embedding
        except Exception as e:
            print(e)


if __name__ == "__main__":
    emb = GetEmbedding("lalit")
    print( emb)
from src.utils.utils import load_object
preprocessor = load_object('src/pipeline/artifacts/preprocessor.pkl')
print(preprocessor)  # Should print details of the transformer if loaded correctly

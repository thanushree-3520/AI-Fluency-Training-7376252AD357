
"""Load handbook Markdown files, split them, and store them in Chroma."""
import shutil
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from lc_config import DB_DIR, EMBED_PROVIDER, get_vectorstore

# Load all Markdown files from this task's data folder
data_dir = Path(__file__).parent / "data"
docs = []

for path in sorted(data_dir.glob("*.md")):
    docs.append(
        Document(
            page_content=path.read_text(encoding="utf-8"),
            metadata={"source": path.name}
        )
    )

print(f"Loaded {len(docs)} documents")

if not docs:
    raise SystemExit("ERROR: No Markdown documents found in the data folder.")

# Split documents into overlapping chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
chunks = splitter.split_documents(docs)

print(f"Split into {len(chunks)} chunks (chunk_size=300, overlap=50)")

if chunks:
    print("Example chunk ->", repr(chunks[0].page_content[:120]), chunks[0].metadata)

# Store vectors in this task folder's Chroma database
shutil.rmtree(DB_DIR, ignore_errors=True)
store = get_vectorstore()
# get_vectorstore uses the configured relative DB_DIR; see the next step
ids = store.add_documents(chunks)

print(f"Stored {len(ids)} vectors using EMBED_PROVIDER={EMBED_PROVIDER}")
print("Vector length:", len(store.embeddings.embed_query("test")))

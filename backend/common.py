import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import pdfplumber

# Load environment variables
load_dotenv()

# Configure OpenAI client with environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
openai_api_base = os.getenv("OPENAI_API_BASE")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Shared LLM instances
generator_llm = ChatOpenAI(
    model="gpt-4o-mini"
)
feedback_llm = ChatOpenAI(
    model="gpt-4o-mini"
)

def extract_resume_text(resume_path):
	"""Extract text from a PDF resume with graceful fallbacks.
	Returns empty string if extraction fails.
	"""
	if not resume_path:
		return ""
	text = ""
	# First attempt: pdfplumber
	try:
		with pdfplumber.open(resume_path) as pdf:
			for page in pdf.pages:
				text += page.extract_text() or ""
			if text.strip():
				return text
	except Exception:
		pass
	# Fallback: pypdfium2
	try:
		import pypdfium2 as pdfium
		doc = pdfium.PdfDocument(resume_path)
		for i in range(len(doc)):
			page = doc[i]
			textpage = page.get_textpage()
			text += textpage.get_text_range() or ""
			textpage.close()
			page.close()
		doc.close()
		return text
	except Exception:
		return ""

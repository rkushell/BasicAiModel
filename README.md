
-----

# Research Assistant Agent

[](https://opensource.org/licenses/MIT)

An intelligent agent powered by **LangChain** and **Google Generative AI** that automates the research process. This tool uses external APIs (DuckDuckGo, Wikipedia) to gather information and generate structured, sourced summaries on any given topic.

-----

##  Features

  - **Natural Language Queries**: Ask research questions in plain English.
  - **Multi-Source Data Fetching**: Aggregates information from:
      -  DuckDuckGo Search
      -  Wikipedia
  - **AI-Powered Summarization**: Uses Google's `gemini-1.5-flash` model to generate coherent summaries.
  - **Structured Output**: Saves results in a clean `.txt` file with the topic, a detailed summary, and a list of sources.
  - **Automated File Naming**: Automatically creates sanitized, timestamped filenames for easy organization.

-----

## Project Structure

```
.
├── .env
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── tools.py
```

-----

##  Setup and Installation

Follow these steps to get the project running locally.

**1. Clone the Repository**

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

**2. Create and Activate a Virtual Environment**

```bash
# Create the environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Set Up Environment Variables**

Create a `.env` file in the root directory of the project and add your Google API key:

```ini
# .env
GOOGLE_API_KEY="your_api_key_here"
```

-----

##  Usage

To run the research assistant, execute the main script from your terminal:

```bash
python main.py
```

You will be prompted to enter a research query. The agent will process the request, display the results in the console, and save them to a file in the project's root directory.

-----

##  Sample Run

Here’s an example of what the agent produces from a query.

### 1\. User Interaction

```
$ python main.py
Enter the research query: The future of quantum computing and its impact on cryptography
```

### 2\. Generated Output File

A new file named `research_2025-09-02_03-45-10_The-future-of-quantum-computing.txt` is created with the following content:

```
TOPIC: The future of quantum computing and its impact on cryptography

SUMMARY:
Quantum computing represents a paradigm shift from classical computing, utilizing principles of quantum mechanics like superposition and entanglement to process information. Its future development promises exponential speedups for specific computational problems, which will have a profound impact on various fields, most notably cryptography.

Current cryptographic standards, such as RSA and ECC, rely on the difficulty of factoring large numbers or solving discrete logarithm problems. These tasks are computationally infeasible for classical computers but could be solved efficiently by a sufficiently powerful quantum computer using Shor's algorithm. This capability poses a significant threat to the security of digital communications, financial transactions, and national security systems.

In response, the field of post-quantum cryptography (PQC) is actively developing new cryptographic algorithms that are secure against attacks from both classical and quantum computers. These next-generation algorithms are based on different mathematical problems, such as lattice-based, code-based, or hash-based cryptography. The transition to PQC standards is a critical and ongoing effort to ensure long-term data security in a quantum-enabled world.

SOURCES:
- https://en.wikipedia.org/wiki/Quantum_computing
- https://en.wikipedia.org/wiki/Post-quantum_cryptography
- https://www.duckduckgo.com/some-relevant-article
- https://www.duckduckgo.com/another-insightful-blog
```

-----

###  Core Dependencies

  - `langchain`
  - `langchain-google-genai`
  - `duckduckgo-search`
  - `wikipedia`
  - `pydantic`
  - `python-dotenv`

-----

### License

This project is licensed under the MIT License. See the LICENSE file for details.

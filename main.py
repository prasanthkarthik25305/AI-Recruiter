# main.py

from agents.jd_summarizer import JDSummarizer

def process_jd(file_path):
    with open(file_path, 'r') as f:
        jd_text = f.read()

    jd_agent = JDSummarizer()
    summary = jd_agent.summarize(jd_text)

    print("📄 JD Summary:")
    print(summary)

# Example call
if __name__ == "__main__":
    process_jd("./data/jds/jd1.txt")

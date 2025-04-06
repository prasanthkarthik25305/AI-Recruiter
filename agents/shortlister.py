# agents/shortlister.py

THRESHOLD = 0.35  # You can adjust this threshold as needed

def filter_matches(resume_filename, matched_jobs, threshold=THRESHOLD):
    print(f"\n🧮 Shortlisting jobs for: {resume_filename}")
    shortlisted = []

    for score, role, filename in matched_jobs:
        if score >= threshold:
            shortlisted.append((score, role, filename))

    if not shortlisted:
        print("⚠️ No matches passed the shortlisting threshold.")
    else:
        print(f"✅ {len(shortlisted)} jobs shortlisted with score >= {threshold}.")

    return shortlisted

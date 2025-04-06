import os
from agents import matcher, shortlister,scheduler
from tools import cv_parser
def process_resumes(resume_folder='data/cvs/'):
    for resume_file in os.listdir(resume_folder):
        if resume_file.endswith('.pdf'):
            resume_path = os.path.join(resume_folder, resume_file)
            print("=" * 80)
            print(f"📄 Matching for Resume: {resume_file}")
            print("=" * 80)

            # Match jobs for this resume
            matched_jobs = matcher.match_single_resume(resume_path)

            if not matched_jobs:
                print(f"⚠️ No matches found for {resume_file}\n")
                continue

            # Shortlist candidates based on filtering rules
            shortlisted = shortlister.filter_matches(resume_file, matched_jobs)

            # Schedule interviews for shortlisted candidates
            scheduler.schedule(resume_file, shortlisted)

            print("\n")
if __name__ == "__main__":
    process_resumes()

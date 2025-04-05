from flask import Blueprint, request, render_template
from .resume_parser import parse_resume
from .web_scraper import analyze_web_links
from .twitter_utils import analyze_twitter_profile
from .firestore_client import save_candidate_data  # ✅ Added import
import os

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_file = request.files.get("resume")
        web_links = request.form.get("web_links", "")
        twitter_handle = request.form.get("twitter_handle")

        results = {}

        # Process uploaded resume
        if resume_file:
            resume_path = os.path.join("uploads", resume_file.filename)
            resume_file.save(resume_path)
            results['resume'] = parse_resume(resume_path)

        # Process web links
        if web_links:
            links = [link.strip() for link in web_links.split(',') if link.strip()]
            results['web'] = analyze_web_links(links)

        # Process Twitter handle
        if twitter_handle:
            results['twitter'] = analyze_twitter_profile(twitter_handle)

        # ✅ Save to Firestore
        candidate_id = twitter_handle or "anonymous"
        save_candidate_data(candidate_id, results)

        return render_template("index.html", results=results)

    return render_template("index.html", results={})
